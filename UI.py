from tkinter import *
from tkinter import messagebox
from method import Download
from tkinter import filedialog
from tkinter import ttk
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = ROOT_DIR + "\media"
class Window:
    def __init__(
            self,
            screen_size = '500x200',
            screen_name = "YOUTUBE DOWNLOADER"
            ):
        self.screen_size = screen_size
        self.screen_name = screen_name
        self.url = ''
        self.dirnamelocation = MEDIA_DIR
        self.start()

    def ask_dir_location(self):
        dirname = filedialog.askdirectory()
        if dirname != '':
            self.dirnamelocation = dirname
        else:
            self.dirnamelocation = MEDIA_DIR
        print(self.dirnamelocation)
        
    def reset_locationdir(self):
        self.dirnamelocation = MEDIA_DIR
        print(self.dirnamelocation)

    def Download(self):
        if self.url.get() != '':
            try:
                messagebox.showinfo("Info", "Downloading....")
                Download(self.url.get(), self.dirnamelocation)
                messagebox.showinfo("BERHASIL", "Download Berhasil")
            except:
                messagebox.showerror("ERROR","URL ERROR")
        else:
            messagebox.showwarning("Warning", "Isi URL di kotak text")

    def start(self):
        root = Tk()
        root.title(self.screen_name)
        # root.geometry(self.screen_size)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        frame = ttk.Frame(root, borderwidth=2)
        frame.grid(column=0, row=0, sticky=(N, W, E, S))

        title_label  = ttk.Label(frame,text=self.screen_name, font=("Verdana", 20))
        self.url = StringVar()
        url_input = ttk.Entry(frame, width=100, textvariable=self.url,)
        submit_btn = ttk.Button(frame, text="Download", command=self.Download)
        askdir_btn = ttk.Button(frame, text="Download location", command=self.ask_dir_location)
        reset_buton = ttk.Button(frame, text="Reset", command=self.reset_locationdir)
        
        title_label.grid(column=2, row=1, sticky=(W,E))
        url_input.grid(column=1, row=2,columnspan=2, sticky=(W,E))
        submit_btn.grid(column=3, row=2, sticky=(W,E))
        askdir_btn.grid(column=1, row=3, sticky=(W,E))
        reset_buton.grid(column=2, row=3, sticky=(W,E))

        for child in frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        url_input.focus()
        root.mainloop()

    



