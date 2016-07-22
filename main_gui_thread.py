import sys
from Tkinter import *

class File(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.create_widgets()
        self.pack(expand=YES, fill=BOTH)
    def create_widgets(self):
        """
        Entry, button  and a display of structure
        :return:
        """
        lab_path = Label(self, text="File Path")
        ent  = Entry(self)
        accept = Button(self, text="Accept")
        cancel = Button(self, text="Cancel")
        txt = Text(self, insertborderwidth=1)
        lab_path.pack()
        ent.pack()
        txt.pack()
        accept.pack()
        cancel.pack()

class YT_gui(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self, parent)
        self.create_widgets()
        self.pack(expand=YES, fill=BOTH)

    def create_widgets(self):
        ent = Entry(self)
        button = Button(self, text="hello")
        button.pack()
        ent.pack()
        print ""

    def install_ytdl(self):
        #Check if already installed
        from subprocess import Popen
        res = Popen(['youtube-dl'])
        res_re = re.find(r'^not installed$')
        if res_re:
            return True
        else:
            #Get OS and try to install
            curr_os = sys.platform
            if 'darwin' in curr_os:
                Popen(['pip', 'install', 'youtube-dl'])
            elif 'linux' in curr_os:
                Popen(['sudo', 'apt-get','install', 'youtube-dl'])
            elif 'win32' in curr_os:
                #Pending
                print "installation on win32 is not yet available"
                #Popen(['pip', 'install', 'youtube-dl'])


def main(argv):
    fl = File()
    fl.mainloop()
    yt = YT_gui()
    yt.mainloop()



if __name__ == '__main__':
    main(sys.argv[1:])