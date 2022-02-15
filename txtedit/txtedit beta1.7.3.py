from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import os
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import *

import sys
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Browser')
        self.setWindowIcon(QIcon('icons/penguin.png'))
        self.resize(900, 600)
        self.show()
        self.browser = QWebView()
        url = 'http://blog.csdn.net/roger_lzh'
        self.browser.setUrl(QUrl(url))
        self.setCentralWidget(self.browser)
        navigation_bar = QToolBar('Navigation')
        navigation_bar.setIconSize(QSize(16, 16))
        self.addToolBar(navigation_bar)
        back_button = QAction(QIcon('icons/back.png'), 'Back', self)
        next_button = QAction(QIcon('icons/next.png'), 'Forward', self)
        stop_button = QAction(QIcon('icons/cross.png'), 'stop', self)
        reload_button = QAction(QIcon('icons/renew.png'), 'reload', self)
        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        reload_button.triggered.connect(self.browser.reload)
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(reload_button)
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)
        self.browser.urlChanged.connect(self.renew_urlbar)
    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)
    def renew_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)
def newfile():
                t.delete('1.0',END)
                windows.title('标题')
def openfile():
                global filename
                filename=askopenfilename()
                if filename=='':
                                return
                with open(filename,'r') as o:
                                c=o.read()
                t.delete('1.0',END)
                t.insert(END,c)
                windows.title(filename)
def saveas():
                global filename
                g=t.get('1.0',END)
                filename=asksaveasfilename()
                if filename=='':
                                return
                with open(filename,'w') as ou:
                                ou.write(g)
                                windows.title(filename)
def save():
                global filename
                g=t.get('1.0',END)
                if filename=='标题':
                                saveas()
                else:
                                with open(filename,'w') as o:
                                                o.write(g)
def a():
                app = QApplication(sys.argv)
                window = MainWindow()
                window.show()
                app.exec_()
filename='标题'
windows=Tk()
windows.title(filename)
windows.geometry('1000x618')
m=Menu(windows)
f=Menu(m,tearoff=False)
m.add_cascade(label='文件',menu=f)
m.add_command(label='内置浏览器，来自github',command=a)
f.add_command(label='新文件',command=newfile)
f.add_command(label='打开文件',command=openfile)
f.add_command(label='保存',command=save)
f.add_command(label='另存为',command=saveas)
f.add_command(label='退出',command=windows.destroy)
windows.config(menu=m)
t=Text(windows)
t.pack(fill=BOTH,expand=True)
windows.mainloop()
