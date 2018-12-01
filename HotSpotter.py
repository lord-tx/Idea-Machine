# Program Name: Hot-SPOTTER v1.0.0
# Author: Johnpaul Muoneme
# Note: Commented out code are as a result of possible
#       editing or replacement as the programmer may
#       wish. This is just a Beta version, use carefully.

import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
import HoverInfo as tt
import os
from tkinter import messagebox as mbox
import ctypes
import sys

# Initial


class interface(object):
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Hot-SPOTTER')
        self.win.resizable(0,0)
        # self.win.minsize(400,400)
        self.buttons()
        self.Menu()
        # self.config_output()
        self.config_output2()
        self.set_ssid()
        self.set_password()
        self.win.iconbitmap(r'C:\Users\Mark Jordan\PycharmProjects\HotSpot\HotSpot.ico')

        # SSID Changer: Change the SSID of your computer.
    def set_ssid(self):
        set_box_label = ttk.Label(self.win, text="Set New SSID")
        set_box_label.grid(column=0, row=5, sticky=tk.W, columnspan=2)
        self.set_box_text = tk.StringVar
        self.set_box = ttk.Entry(self.win, textvariable=self.set_box_text)
        self.set_box.grid(column=1, row=5, columnspan=2)

    # Password Changer: Change the Password of your Hotspot
    def set_password(self):
        set_pass_label = ttk.Label(self.win, text="Set New Password")
        set_pass_label.grid(column=0, row=6, sticky=tk.W, columnspan=2)
        self.set_pass_text = tk.StringVar
        self.set_pass = ttk.Entry(self.win, textvariable=self.set_pass_text)
        self.set_pass.grid(column=1, row=6, columnspan=2)

    # Tooltips x HoverInfo
    # def hoverinfo(self):
    #     tt.createToolTip(self.set_password, 'Enter Password Here (Together).')
    #     tt.createToolTip(self.set_ssid, 'Enter New SSID in text format.')
    #     tt.createToolTip(self.scr, 'Output is displayed here.')

    # This was the supposed output file for the Commands

    # def config_output(self):
    #     self.config_text = tk.StringVar
    #     self.config_input = ttk.Entry(self.win, textvariable=self.config_text)
    #     self.config_input.grid(column=0, columnspan=4, row=4, sticky=tk.NSEW)

    def config_output2(self):
        self.scr = scrolledtext.ScrolledText(self.win, width=20, height=15, wrap=tk.WORD)
        self.scr.grid(column=0, row=4, sticky='WE', columnspan=5)
        # self.hover = tt.createToolTip(self.scr, 'Output is displayed here.')
        # self.scr.configure(text=self.stat1)

    def action_start(self):
        # ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        stat = os.popen('netsh wlan start hostednetwork').read()
        self.scr.insert(tk.INSERT, stat)
        # os.popen("F:\\start.bat")

    # The use of 'os.popen' as negated to 'os.system' use is subject
    # to no debate as output to scrolled text is necessary
    def action_stop(self):
        stat = os.popen('netsh wlan stop hostednetwork').read()
        self.scr.insert(tk.INSERT, stat)

    # The use of 'os.popen' as negated to 'os.system' use is subject
    # to no debate as output to scrolled text is necessary
    def action_details(self):
        # TODO: Try to redirect the output of both stat1 and stat2 to a Widget
        stat1 = os.popen('netsh wlan show hostednetwork').read()
        stat2 = os.popen('netsh wlan show hostednetwork setting=security').read()
        status = stat1 + stat2
        # print(status)
        self.scr.insert(tk.INSERT, status)

    # The use of 'os.popen' as negated to 'os.system' use is subject
    # to no debate as output to scrolled text is necessary
    def action_configure_ssid(self):
        stat = os.popen(('netsh wlan set hostednetwork ssid = %s' % (self.set_box.get()))).read()
        self.scr.insert(tk.INSERT, stat)

    # The use of 'os.popen' as negated to 'os.system' use is subject
    # to no debate as output to scrolled text is necessary
    def action_configure_pass(self):
        stat = os.popen(('netsh wlan set hostednetwork key = %s keyUsage=persistent' % (self.set_pass.get()))).read()
        self.scr.insert(tk.INSERT, stat)

    # TODO: Complete research and implementation on this clear function

    def buttons(self):

        self.start = ttk.Button(text='Start', width=18, command=self.action_start)
        self.start.grid(column=0, row=2, sticky=tk.NSEW)

        self.stop = ttk.Button(text='Stop', width=10, command=self.action_stop)
        self.stop.grid(column=1, row=2, sticky=tk.W)

        self.details = ttk.Button(text='Details', width=10, command=self.action_details)
        self.details.grid(column=2, row=2, sticky=tk.W)

        self.clear = ttk.Button(text='Clear', width=10, command=lambda: self.scr.delete(1.0, tk.END))
        self.clear.grid(column=3, row=2, sticky=tk.W)

        self.configure_ssid = ttk.Button(text='Configure SSID', width=20, command=self.action_configure_ssid)
        self.configure_ssid.grid(column=3, row=5, sticky=tk.NSEW, columnspan=2)

        self.configure_pass = ttk.Button(text='Configure Password', width=20, command=self.action_configure_pass)
        self.configure_pass.grid(column=3, row=6, sticky=tk.NSEW, columnspan=2)

        self.exit = ttk.Button(text='Exit', width=15, command=self._quit)
        self.exit.grid(column=4, row=2, sticky=tk.W)

    def _quit(self):
        answer = mbox.askyesnocancel('Exit', 'Do you wish to exit Hot-Spotter?')
        if answer == 1:
            self.win.quit()
            self.win.destroy()
            exit()
        elif answer == 0:
            mbox.showinfo('Stay with Us', 'Okey Dokey!')

    def about(self):
        mbox.showinfo("About", "Hot-Spotter\nVersion 1.0.0\nThe Idea Machine - Scripts\n2018")

    def Menu(self):
        self.menubar = Menu(self.win)
        self.win.config(menu=self.menubar)

        # Add menu items
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self._quit)
        self.menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about)
        self.menubar.add_cascade(label="Help", menu=helpmenu)


inter = interface()
inter.win.mainloop()
