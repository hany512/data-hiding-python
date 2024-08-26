from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import numpy as np
from PIL import Image, ImageTk
import os
import customtkinter
from imageLSB import image
from textlsb import text
from audiolsb import audio
from imagedwt import imagedwt
from audiodwt import audiodwt
from textdwt import textdwt
import wave

covimage = None  # Declare and initialize the covimage variable
class app:
    def __init__(self, master):
        self.master = master
        # Set the width and height of the window
        w=1000
        h=600
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)  #change hs/2 to hs/4 to left window up
        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        master.resizable(FALSE,FALSE)
        self.startpage()


    def startpage(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master)
        self.frame1.pack(fill='both', expand=True)
        self.image = PhotoImage(file="assets\startpage.png")
        image_label = tk.Label(self.frame1, image=self.image,bg='#d0ecfd')
        image_label.pack(pady=0)  
        tk.Label(root,text="Select your media",font=my_font3,bg='#d0ecfd').place( x =350, y =125, anchor = NW)
        customtkinter.set_default_color_theme("dark-blue") 
        # Modify the btntext button
        btnaudio = customtkinter.CTkButton(root,text = 'Spat',width=150,font=my_font3,
                  command=self.startpageLSB).place( x =270, y =450, anchor = NW)
        self.help= PhotoImage(file="assets\help.png")
        help_label = Button(root, image=self.help,bg='#54a0ff',command=self.help_dwtlsb_diff)
        help_label.place(x =510, y =450, anchor = NE)
        btnimage = customtkinter.CTkButton(root,text = 'Freq',font=my_font3,width=150,
                  command=self.startpageDWT).place( x =570, y =450, anchor = NW)
    
    def startpageLSB(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, bg='#d0ecfd')
        self.frame1.pack(fill='both', expand=True)
        self.image = PhotoImage(file="assets\startpage2.png")
        image_label = tk.Label(self.frame1, image=self.image,bg='#d0ecfd')
        image_label.pack(pady=0)  
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hideLSBtext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hideLSBaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hideLSBimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extLSBtext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extLSBaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extLSBimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_startpage)
        menubar.add_cascade(label="Help" , menu=about)
         
    
    def startpageDWT(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, bg='#d0ecfd')
        self.frame1.pack(fill='both', expand=True)
        self.image = PhotoImage(file="assets\startpage2.png")
        image_label = tk.Label(self.frame1, image=self.image,bg='#d0ecfd')
        image_label.pack(pady=0)  
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hidedwttext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hidedwtaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hidedwtimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extdwttext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extdwtaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extdwtimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_startpage)
        menubar.add_cascade(label="Help" , menu=about)
         
    def help_dwtlsb_diff(self):
        help_window = Toplevel(self.master)
        help_window.title("Help Page")

        # Set the width and height of the window
        w = 700
        h = 400
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        help_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        help_window.resizable(FALSE, FALSE)

        help_frame = Frame(help_window, bg='#347FAA')
        help_frame.pack(fill='both', expand=True)

        # Add your help content here
        tk.Label(help_frame, text="Help Content", bg='#347FAA', font=my_font3).pack(pady=20)

        

        tk.Label(help_frame,text="spat(Spatial Domain Steganography): its simplicity and low computational complexity"
         ,font=('times', 15, 'bold'),bg='#347FAA', wraplength=700).place( x =0, y =110, anchor = NW)
        

        tk.Label(help_frame,text="freq(frequency domain steganography): provides better robustness against image processing attacks and compression compared to LSB"
         ,font=('times', 15, 'bold'),bg='#347FAA', wraplength=700).place( x =0, y =210, anchor = NW)
        
        
        # Add a button to close the help window
        close_button = customtkinter.CTkButton(help_frame, text="Close", width=150, font=('Source Sans Pro', 20, 'bold'),
                                            command=help_window.destroy,bg_color='yellow')
        close_button.place( x =350, y =360, anchor = S)

    def help_startpage(self):
        help_window = Toplevel(self.master)
        help_window.title("Help Page")

        # Set the width and height of the window
        w = 700
        h = 550
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        help_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        help_window.resizable(FALSE, FALSE)

        help_frame = Frame(help_window, bg='#347FAA')
        help_frame.pack(fill='both', expand=True)

        # Add your help content here
        tk.Label(help_frame, text="Help Content", bg='#347FAA', font=my_font3).pack(pady=20)

        # Load and display the image
        self.help_image = PhotoImage(file="assets\Start_Help.png")  # Replace with the path to your image file
        tk.Label(help_frame, image=self.help_image, bg='black').place( x =0, y =100, anchor = NW)

        tk.Label(help_frame,text="Here in the file menu you will find one choice \n New : this will back you to the main page. "
         ,font=('times', 15, 'bold'),bg='#347FAA').place( x =200, y =110, anchor = NW)
        
        self.help_image2 = PhotoImage(file="assets\Start_Help2.png")  # Replace with the path to your image file
        tk.Label(help_frame, image=self.help_image2, bg='black').place( x =0, y =200, anchor = NW)

        tk.Label(help_frame,text="Here in the hide menu you will find three choice \n Text : this will go to the Hide text page.\n Audio : this will go to the Hide audio page.\n Image : this will go to the Hide image page. "
         ,font=('times', 15, 'bold'),bg='#347FAA').place( x =200, y =210, anchor = NW)
        
        self.help_image3 = PhotoImage(file="assets\Start_Help3.png")  # Replace with the path to your image file
        tk.Label(help_frame, image=self.help_image3, bg='black').place( x =0, y =350, anchor = NW)
        
        tk.Label(help_frame,text="Here in the extract menu you will find three choice \n Text : this will go to the extract text page.\n Audio : this will go to the extract audio page.\n Image : this will go to the extract image page. "
         ,font=('times', 15, 'bold'),bg='#347FAA').place( x =200, y =360, anchor = NW)

        # Add a button to close the help window
        close_button = customtkinter.CTkButton(help_frame, text="Close", width=150, font=('Source Sans Pro', 20, 'bold'),
                                            command=help_window.destroy,bg_color='yellow')
        close_button.place( x =350, y =530, anchor = S)

    def help_hide(self):
        help_window = Toplevel(self.master)
        help_window.title("Help hide Page")

        # Set the width and height of the window
        w = 700
        h = 600
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        help_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        help_window.resizable(FALSE, FALSE)

        help_frame = Frame(help_window, bg='#347FAA')
        help_frame.pack(fill='both', expand=True)

        # Add your help content here
        tk.Label(help_frame, text="Help Content", bg='#347FAA', font=my_font3).pack(pady=20)

        # Load and display the image
        self.help_image = PhotoImage(file="assets\hide.png")  # Replace with the path to your image file
        tk.Label(help_frame, image=self.help_image, bg='black').place( x =100, y =100, anchor = NW)

        tk.Label(help_frame,text="MSE(Mean Square Error):is a mathematical metric that measures \n the average squared difference between the pixel values of two images."
         ,font=('times', 15, 'bold'),bg='#347FAA').place( x =0, y =420, anchor = NW)
        
        tk.Label(help_frame,text=" PSNR(Peak Signal To Noise Ratio): is a logarithmic measure that quantifies \n the ratio between the maximum possible power of a signal."
         ,font=('times', 15, 'bold'),bg='#347FAA').place( x =0, y =480, anchor = NW)

        # Add a button to close the help window
        close_button = customtkinter.CTkButton(help_frame, text="Close", width=150, font=('Source Sans Pro', 20, 'bold'),
                                            command=help_window.destroy,bg_color='yellow')
        close_button.place( x =350, y =570, anchor = S)


    def help_extract_lsb(self):
        help_window = Toplevel(self.master)
        help_window.title("Help extract Page")

        # Set the width and height of the window
        w = 700
        h = 550
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        help_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        help_window.resizable(FALSE, FALSE)

        help_frame = Frame(help_window, bg='#347FAA')
        help_frame.pack(fill='both', expand=True)

        # Add your help content here
        tk.Label(help_frame, text="Help Content", bg='#347FAA', font=my_font3).pack(pady=20)

        # Load and display the image
        self.help_image = PhotoImage(file="assets\extract_LSB.png")  # Replace with the path to your image file
        tk.Label(help_frame, image=self.help_image, bg='black').place( x =100, y =100, anchor = NW)


        # Add a button to close the help window
        close_button = customtkinter.CTkButton(help_frame, text="Close", width=150, font=('Source Sans Pro', 20, 'bold'),
                                            command=help_window.destroy,bg_color='yellow')
        close_button.place( x =350, y =500, anchor = S)
    
    def help_extract_dwt(self):
        help_window = Toplevel(self.master)
        help_window.title("Help extract Page")

        # Set the width and height of the window
        w = 700
        h = 550
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        help_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        help_window.resizable(FALSE, FALSE)

        help_frame = Frame(help_window, bg='#347FAA')
        help_frame.pack(fill='both', expand=True)

        # Add your help content here
        tk.Label(help_frame, text="Help Content", bg='#347FAA', font=my_font3).pack(pady=20)

        # Load and display the image
        self.help_image = PhotoImage(file="assets\extract_dwt.png")  # Replace with the path to your image file
        tk.Label(help_frame, image=self.help_image, bg='black').place( x =100, y =100, anchor = NW)


        # Add a button to close the help window
        close_button = customtkinter.CTkButton(help_frame, text="Close", width=150, font=('Source Sans Pro', 20, 'bold'),
                                            command=help_window.destroy,bg_color='yellow')
        close_button.place( x =350, y =530, anchor = S)

    
        
    def hideLSBtext(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master,bg='#d0ecfd')
        self.frame1.pack(fill='both', expand=True)
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        file.add_separator()
        file.add_command(label="Save As",command=lambda:save_stego(stego_image))
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hideLSBtext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hideLSBaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hideLSBimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extLSBtext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extLSBaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extLSBimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_hide)
        menubar.add_cascade(label="Help" , menu=about)

        tk.Label(root,text="Load Cover Image:",font=my_font,bg='#d0ecfd').place( x =50, y =50, anchor = NW)
        tk.Label(root,text="Load Text File:",font=my_font,bg='#d0ecfd').place( x =50, y =125, anchor = NW)
        btncover = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_coverimage()).place( x =750, y =50, anchor = NW)
        btnaudio = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_text()).place( x =750, y =125, anchor = NW)
        
        
        but_lsb1 = customtkinter.CTkButton(root, text='Hide', font=my_font3, width=150,
                  command=lambda: hide_text_LSB()).place(x=400, y=500, anchor=NW)
        
    
    def extLSBtext(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master,bg='#d0ecfd')
        self.frame1.pack(fill='both', expand=True)
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        file.add_separator()
        file.add_command(label="Save As",command=lambda:save_text(decrypted_text_data))
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hideLSBtext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hideLSBaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hideLSBimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extLSBtext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extLSBaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extLSBimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_extract_lsb)
        menubar.add_cascade(label="Help" , menu=about)

        tk.Label(root,text="Load Stego Image:",font=my_font,bg='#d0ecfd').place( x =50, y =50, anchor = NW)
        
        btncover = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_stegoimage()).place( x =750, y =50, anchor = NW)
       
        
        but_lsb1 = customtkinter.CTkButton(root, text='Extract', font=my_font3, width=150,
                  command=lambda: extract_text_LSB(self.text_box_key.get(), self.text_box_iv.get())).place(x=400, y=500, anchor=NW)
        
        tk.Label(root,text="Secret key:",font=my_font,bg='#d0ecfd').place( x =50, y =125, anchor = NW)
        # Create the text box
        self.text_box_key = tk.Entry(root, width=45,font=my_font2)
        self.text_box_key.place(x=200,y=132)
        
        tk.Label(root,text="Secret IV:",font=my_font,bg='#d0ecfd').place( x =50, y =200, anchor = NW)
        # Create the text box
        self.text_box_iv = tk.Entry(root, width=45,font=my_font2)
        self.text_box_iv.place(x=200,y=207)

        
        
    def hidedwttext(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master,bg='#d0ecfd')
        self.frame2.pack(fill='both', expand=True)
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        file.add_separator()
        file.add_command(label="Save As",command=lambda:save_stego(stego_image))
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hidedwttext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hidedwtaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hidedwtimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extdwttext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extdwtaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extdwtimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_hide)
        menubar.add_cascade(label="Help" , menu=about)

        tk.Label(root,text="Load Cover Image:",font=my_font,bg='#d0ecfd').place( x =50, y =50, anchor = NW)
        tk.Label(root,text="Load Text File:",font=my_font,bg='#d0ecfd').place( x =50, y =125, anchor = NW)
        btncover = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_coverimage()).place( x =750, y =50, anchor = NW)
        btnaudio = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_text()).place( x =750, y =125, anchor = NW)
        but_lsb3 = customtkinter.CTkButton(root, text='Hide', font=my_font3, width=150,
                  command=lambda: hide_text_dwt()).place(x=400, y=500, anchor=NW)
        
    

        
    def extdwttext(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master,bg='#d0ecfd')
        self.frame2.pack(fill='both', expand=True)
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        file.add_separator()
        file.add_command(label="Save As",command=lambda:save_textdwt(extracted_text))
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hidedwttext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hidedwtaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hidedwtimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extdwttext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extdwtaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extdwtimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_extract_dwt)
        menubar.add_cascade(label="Help" , menu=about)

        tk.Label(root,text="Load Stego Image:",font=my_font,bg='#d0ecfd').place( x =50, y =50, anchor = NW)
        
        btncover = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_stegoimage()).place( x =750, y =50, anchor = NW)
       
        but_lsb3 = customtkinter.CTkButton(root, text='Extract', font=my_font3, width=150,
                  command=lambda: extract_text_dwt(self.text_box_key.get())).place(x=400, y=500, anchor=NW)  
        tk.Label(root,text="Secret key:",font=my_font,bg='#d0ecfd').place( x =50, y =125, anchor = NW)
        # Create the text box
        self.text_box_key = tk.Entry(root, width=45,font=my_font2)
        self.text_box_key.place(x=200,y=132)
        
    

        
    
        
        
    def hideLSBaudio(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master,bg='#d0ecfd')
        self.frame1.pack(fill='both', expand=True)
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        file.add_separator()
        file.add_command(label="Save As",command=lambda:save_stego(stego_image))
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hideLSBtext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hideLSBaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hideLSBimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extLSBtext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extLSBaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extLSBimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_hide)
        menubar.add_cascade(label="Help" , menu=about)

        tk.Label(root,text="Load Cover Image:",font=my_font,bg='#d0ecfd').place( x =50, y =50, anchor = NW)
        tk.Label(root,text="Load Audio File:",font=my_font,bg='#d0ecfd').place( x =50, y =125, anchor = NW)
        btncover = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_coverimage()).place( x =750, y =50, anchor = NW)
        btnaudio = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_Audio()).place( x =750, y =125, anchor = NW)
        
        
        but_lsb1 = customtkinter.CTkButton(root, text='Hide', font=my_font3, width=150,
                  command=lambda:hide_audio_LSB()).place(x=400, y=500, anchor=NW)
        
        
        
    
    def extLSBaudio(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master,bg='#d0ecfd')
        self.frame1.pack(fill='both', expand=True)
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        file.add_separator()
        file.add_command(label="Save As",command=lambda:save_audio(decrypted_audio_data))
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hideLSBtext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hideLSBaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hideLSBimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extLSBtext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extLSBaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extLSBimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_extract_lsb)
        menubar.add_cascade(label="Help" , menu=about)

        tk.Label(root,text="Load Stego Image:",font=my_font,bg='#d0ecfd').place( x =50, y =50, anchor = NW)
        
        btncover = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_stegoimage()).place( x =750, y =50, anchor = NW)
       
        
        
        but_lsb1 = customtkinter.CTkButton(root, text='Extract', font=my_font3, width=150,
                  command=lambda: extract_audio_LSB(self.text_box_key.get(), self.text_box_iv.get())).place(x=400, y=500, anchor=NW)
                  
        tk.Label(root,text="Secret key:",font=my_font,bg='#d0ecfd').place( x =50, y =125, anchor = NW)
        # Create the text box
        self.text_box_key = tk.Entry(root, width=45,font=my_font2)
        self.text_box_key.place(x=200,y=132)
        
        tk.Label(root,text="Secret IV:",font=my_font,bg='#d0ecfd').place( x =50, y =200, anchor = NW)
        # Create the text box
        self.text_box_iv = tk.Entry(root, width=45,font=my_font2)
        self.text_box_iv.place(x=200,y=207)

        
        
        
    def hidedwtaudio(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master,bg='#d0ecfd')
        self.frame2.pack(fill='both', expand=True)
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        file.add_separator()
        file.add_command(label="Save As",command=lambda:save_stego(stego_image))
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hidedwttext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hidedwtaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hidedwtimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extdwttext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extdwtaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extdwtimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_hide)
        menubar.add_cascade(label="Help" , menu=about)

        tk.Label(root,text="Load Cover Image:",font=my_font,bg='#d0ecfd').place( x =50, y =50, anchor = NW)
        tk.Label(root,text="Load Audio File:",font=my_font,bg='#d0ecfd').place( x =50, y =125, anchor = NW)
        btncover = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_coverimage()).place( x =750, y =50, anchor = NW)
        
        btnaudio = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_Audio()).place( x =750, y =125, anchor = NW)
        
        but_lsb3 = customtkinter.CTkButton(root, text='Hide', font=my_font3, width=150,
                  command=lambda: hide_audio_dwt()).place(x=400, y=500, anchor=NW)
        
        
        
    def extdwtaudio(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master,bg='#d0ecfd')
        self.frame2.pack(fill='both', expand=True)
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        file.add_separator()
        file.add_command(label="Save As",command=lambda:save_audiodwt(extracted_audio, audio_params))
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hidedwttext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hidedwtaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hidedwtimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extdwttext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extdwtaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extdwtimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_extract_dwt)
        menubar.add_cascade(label="Help" , menu=about)

        tk.Label(root,text="Load Stego Image:",font=my_font,bg='#d0ecfd').place( x =50, y =50, anchor = NW)
        
        btncover = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_stegoimage()).place( x =750, y =50, anchor = NW)
       
        but_lsb3 = customtkinter.CTkButton(root, text='Extract', font=my_font3, width=150,
                  command=lambda: extract_audio_dwt(self.text_box_key.get())).place(x=400, y=500, anchor=NW)
        
        tk.Label(root,text="Secret key:",font=my_font,bg='#d0ecfd').place( x =50, y =125, anchor = NW)
        # Create the text box
        self.text_box_key = tk.Entry(root, width=45,font=my_font2)
        self.text_box_key.place(x=200,y=132)
        

        
        
        
    

    def hideLSBimage(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master,bg='#d0ecfd')
        self.frame1.pack(fill='both', expand=True)
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        file.add_separator()
        file.add_command(label="Save As",command=lambda:save_stego(stego_image))
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hideLSBtext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hideLSBaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hideLSBimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extLSBtext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extLSBaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extLSBimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_hide)
        menubar.add_cascade(label="Help" , menu=about)

        tk.Label(root,text="Load Cover Image:",font=my_font,bg="#d0ecfd").place( x =50, y =50, anchor = NW)
        tk.Label(root,text="Load Image File:",font=my_font,bg="#d0ecfd").place( x =50, y =125, anchor = NW)
        btncover = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_coverimage()).place( x =750, y =50, anchor = NW)
        btnaudio = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_secretimage()).place( x =750, y =125, anchor = NW)
        
        
        but_lsb1 = customtkinter.CTkButton(root, text='Hide', font=my_font3, width=150,
                  command=lambda: hide_image_LSB()).place(x=400, y=500, anchor=NW)
        
        
        
        
    
    def extLSBimage(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master,bg='#d0ecfd')
        self.frame1.pack(fill='both', expand=True)
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        file.add_separator()
        file.add_command(label="Save As",command=lambda:save_stego(decrypted_image))
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hideLSBtext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hideLSBaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hideLSBimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extLSBtext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extLSBaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extLSBimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_extract_lsb)
        menubar.add_cascade(label="Help" , menu=about)

        tk.Label(root,text="Load Stego Image:",font=my_font,bg="#d0ecfd").place( x =50, y =50, anchor = NW)
        
        btncover = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_stegoimage()).place( x =750, y =50, anchor = NW)
       
        
        
        but_lsb1 = customtkinter.CTkButton(root, text='Extract', font=my_font3, width=150,
                  command=lambda: extract_image_LSB(self.text_box_key.get(), self.text_box_iv.get())).place(x=400, y=500, anchor=NW)
    
        tk.Label(root,text="Secret key:",font=my_font,bg='#d0ecfd').place( x =50, y =125, anchor = NW)
        # Create the text box
        self.text_box_key = tk.Entry(root, width=45,font=my_font2)
        self.text_box_key.place(x=200,y=132)
        
        tk.Label(root,text="Secret IV:",font=my_font,bg='#d0ecfd').place( x =50, y =200, anchor = NW)
        # Create the text box
        self.text_box_iv = tk.Entry(root, width=45,font=my_font2)
        self.text_box_iv.place(x=200,y=207)

        
        
        
        
    def hidedwtimage(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master,bg='#d0ecfd')
        self.frame2.pack(fill='both', expand=True)
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        file.add_separator()
        file.add_command(label="Save As",command=lambda:save_stego(stego_image))
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hidedwttext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hidedwtaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hidedwtimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extdwttext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extdwtaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extdwtimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_hide)
        menubar.add_cascade(label="Help" , menu=about)

        tk.Label(root,text="Load Cover Image:",font=my_font,bg='#d0ecfd').place( x =50, y =50, anchor = NW)
        tk.Label(root,text="Load Image File:",font=my_font,bg='#d0ecfd').place( x =50, y =125, anchor = NW)
        btncover = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_coverimage()).place( x =750, y =50, anchor = NW)
        btnaudio = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_secretimage()).place( x =750, y =125, anchor = NW)
        but_lsb3 = customtkinter.CTkButton(root, text='Hide', font=my_font3, width=150,
                  command=lambda: hide_image_DWT()).place(x=400, y=500, anchor=NW)
        
        
        
    def extdwtimage(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master,bg='#d0ecfd')
        self.frame2.pack(fill='both', expand=True)
        menubar = Menu(root)
        root.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New", command=self.startpage)
        file.add_separator()
        file.add_command(label="Save As",command=lambda:save_stego(decrypted_image))
        menubar.add_cascade(label="File" , menu=file)
        sender = Menu(menubar, tearoff=0)
        sender.add_command(label="Text",command=self.hidedwttext)
        sender.add_separator()
        sender.add_command(label="Audio",command=self.hidedwtaudio)
        sender.add_separator()
        sender.add_command(label="Image",command=self.hidedwtimage)
        menubar.add_cascade(label="Hide", menu=sender)
        reseiver = Menu(menubar, tearoff=0)
        reseiver.add_command(label="Text",command=self.extdwttext)
        reseiver.add_separator()
        reseiver.add_command(label="Audio",command=self.extdwtaudio)
        reseiver.add_separator()
        reseiver.add_command(label="Image",command=self.extdwtimage)
        menubar.add_cascade(label="Extract",menu=reseiver)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="Help", command=self.help_extract_dwt)
        menubar.add_cascade(label="Help" , menu=about)

        tk.Label(root,text="Load Stego Image:",font=my_font,bg='#d0ecfd').place( x =50, y =50, anchor = NW)
        
        btncover = customtkinter.CTkButton(root,text = 'Browse',font=my_font3,width=150,
                  command=lambda: upload_stegoimage()).place( x =750, y =50, anchor = NW)
       
        but_lsb3 = customtkinter.CTkButton(root, text='Extract', font=my_font3, width=150,
                  command=lambda: extract_image_dwt(self.text_box_key.get())).place(x=400, y=500, anchor=NW)     
        tk.Label(root,text="Secret key:",font=my_font,bg='#d0ecfd').place( x =50, y =125, anchor = NW)
        # Create the text box
        self.text_box_key = tk.Entry(root, width=45,font=my_font2)
        self.text_box_key.place(x=200,y=132)
        
        


                          
def upload_coverimage():
     global img , covimage
     f_types = [('jpg Files', '.jpg')]
     f_types2 = [('png Files', '.png')]
     f_types3 = [('bmp Files', '*.bmp')]
     covimage = filedialog.askopenfilename(filetypes=f_types+f_types2+f_types3)
     if not covimage:  # Check if no image file is selected
        messagebox.showerror("Error", "No cover image selected.")
        return
     img=Image.open(covimage)
     img_resized=img.resize((250,200)) # new width & height
     img=ImageTk.PhotoImage(img_resized)
     label = tk.Label(root, font=my_font, text=str(covimage),bg='#d0ecfd', wraplength=450).place( x=300, y=50, anchor = NW)
     b2 =tk.Label(root,image=img,bg='black') 
     b2.place( x =50, y =220, anchor = NW)


def upload_stegoimage():
     global img , stegoimage
     f_types = [('jpg Files', '.jpg')]
     f_types2 = [('png Files', '.png')]
     f_types3 = [('bmp Files', '*.bmp')]
     stegoimage = filedialog.askopenfilename(filetypes=f_types3+f_types2+f_types)
     if not stegoimage:  # Check if no image file is selected
        messagebox.showerror("Error", "No image selected.")
        return
     img=Image.open(stegoimage)
     img_resized=img.resize((250,200)) # new width & height
     img=ImageTk.PhotoImage(img_resized)
     tk.Label(root, font=my_font, text=str(stegoimage),bg='#d0ecfd', wraplength=450).place( x=300, y=50, anchor = NW)
     b2 =tk.Label(root,image=img,bg='black') 
     b2.place( x =50, y =250, anchor = NW)
     
     
def upload_secretimage():
     global secimage
     f_types = [('jpg Files', '.jpg')]
     f_types2 = [('png Files', '.png')]
     f_types3 = [('bmp Files', '*.bmp')]
     secimage = filedialog.askopenfilename(filetypes=f_types+f_types2+f_types3)
     if not secimage:  # Check if no text file is selected
        messagebox.showerror("Error", "No image selected.")
        return
     tk.Label(root, font=my_font, text=str(secimage),bg='#d0ecfd', wraplength=450).place( x=300, y=125, anchor = NW)
    
    
def upload_Audio():
     global audio_path
     audio_path = askopenfilename(filetypes=[("Audio Files", "*.wav")])
     if not audio_path:  # Check if no text file is selected
        messagebox.showerror("Error", "No audio file selected.")
        return
     tk.Label(root, font=my_font, text=str(audio_path),bg='#d0ecfd', wraplength=450).place( x=300, y=125, anchor = NW)

def upload_text():
     global text_path
     text_path = askopenfilename(filetypes=[("text files", "*.txt")])
     if not text_path:  # Check if no text file is selected
        messagebox.showerror("Error", "No text file selected.")
        return
     tk.Label(root, font=my_font, text=str(text_path),bg='#d0ecfd', wraplength=450).place( x=250, y=125, anchor = NW)
     
def save_stego(img):
    f_types2 = [('png Files', '.png')]
    f_types3 = [('bmp Files', '*.bmp')]
    file_path = filedialog.asksaveasfilename(filetypes=f_types3+f_types2,defaultextension=".bmp")
    img.save(file_path)
    messagebox.showinfo("save", "Image saved succesfully")
    
def save_text(text):
    file_path = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")), defaultextension=".txt")
    with open(file_path, "wb") as f:
        f.write(text)
    messagebox.showinfo("save", "Text saved succesfully")

def save_textdwt(text):
    file_path = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")), defaultextension=".txt")
    with open(file_path, "w") as f:
        f.write(text)
    messagebox.showinfo("save", "Text saved succesfully")

def save_audio(audio):
    file_path = filedialog.asksaveasfilename(filetypes=[("WAV files", "*.wav")], defaultextension=".wav")
    with open(file_path, 'wb') as f:
        f.write(audio)
    messagebox.showinfo("save", "Audio saved succesfully")

def save_audiodwt(audio,audio_params):
     file_path = filedialog.asksaveasfilename(filetypes=[("WAV files", "*.wav")], defaultextension=".wav")
     with wave.open(file_path, 'wb') as wav:
        wav.setparams(audio_params)
        wav.writeframes(audio)
     messagebox.showinfo("save", "Audio saved succesfully")
    
def show_stego(img):
    global stego_img
    img_resized = img.resize((250, 200))
    stego_img = ImageTk.PhotoImage(img_resized)
    b2 = tk.Label(root, image=stego_img,bg='black')
    b2.place(x=350, y=220, anchor=NW)

def show_secret(img):
    global secret_img
    img_resized = img.resize((250, 200))
    secret_img = ImageTk.PhotoImage(img_resized)
    b2 = tk.Label(root, image=secret_img,bg='black')
    b2.place(x=350, y=250, anchor=NW)

def PSNR(original, compressed):
    global mse_value , psnr_value
    
    # Convert to NumPy arrays
    img1 = Image.open(original).convert('RGB')
    img1_array = np.array(img1, dtype=np.float64)
    img2_array = np.array(compressed, dtype=np.float64)

    # Calculate MSE
    mse_value = np.mean((img1_array - img2_array) ** 2)

    # Calculate PSNR
    if mse_value == 0:
        psnr_value = float('inf')
    else:
        max_pixel = 255.0
        psnr_value = 20 * np.log10(max_pixel / np.sqrt(mse_value))

    # Round MSE and PSNR to 5 decimal places
    mse_value = round(mse_value, 5)
    psnr_value = round(psnr_value, 5)

    tk.Label(root,text="MSE:",font=my_font,bg='#d0ecfd').place( x =700, y =300, anchor = NW)
    tk.Label(root, font=my_font, text=mse_value,bg='white').place( x=800, y=300, anchor = NW)
    tk.Label(root,text="PSNR:",font=my_font,bg='#d0ecfd').place( x =700, y =350, anchor = NW)
    tk.Label(root, font=my_font, text=psnr_value,bg='white').place( x=800, y=350, anchor = NW)
    return mse_value, psnr_value

 

def hide_text_LSB():
        global stego_image

        if not covimage or not text_path:  # Check if either cover image or text file is missing
            messagebox.showerror("Error", "Cover image or text file is missing.")
            return
    
    
        # Load the secret text file
        with open(text_path, 'rb') as f:
            secret_text_data = f.read()

        # Load the cover image
        
        cover_image = Image.open(covimage).convert('RGB')

        # Use the correct key and initialization vector (IV) for your encryption
        key = os.urandom(32)  # This should be your actual key
        iv = os.urandom(16)  # This should be your actual IV

        messagebox.showinfo("save", "please save your key")
        
        key_path = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")), defaultextension=".txt")
        with open(key_path, 'w') as f:
            f.write('Key: ' + str(key.hex()) + '\n' + '\n')
            f.write('IV: ' + str(iv.hex()))
        
        messagebox.showinfo("save", "your key saved succesfully \nplease wait untill process finish")
        
        # Encrypt the secret text
        encrypted_text_data = text.encrypt_text(secret_text_data, key, iv)


        # Define the flag to indicate the end of the secret data
        flag = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        try:
         # Hide the encrypted secret text data in the cover image
         stego_image = text.hide_data_in_image(cover_image, encrypted_text_data, flag)
        except ValueError:
         messagebox.showerror("Error", "possibly due to invalid cover image.")
         return

        

        # Save the stego image and show the data
        show_stego(stego_image)
        PSNR(covimage,stego_image)
        messagebox.showinfo("hide", "text hide succesfully")

    
def extract_text_LSB(key1, iv1):
    global decrypted_text_data

    # Check if key and iv are provided
    if not key1 or not iv1:
        messagebox.showerror("Error", "Key or IV not provided!")
        return

    messagebox.showinfo("extract", "please wait until process finish")

    flag = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Load the cover image
    stego = Image.open(stegoimage).convert('RGB')
    # Extract the encrypted secret text data from the stego image
    extracted_encrypted_text_data = text.extract_data_from_image(stego, flag)
    key = bytes.fromhex(key1)
    iv = bytes.fromhex(iv1)
    try:
        # Decrypt the extracted encrypted text data
        decrypted_text_data = text.decrypt_text(extracted_encrypted_text_data, key, iv)
    except ValueError:
        messagebox.showerror("Error", "Decryption failed - possibly due to invalid key or IV.")
        return

    messagebox.showinfo("extract", "Text extracted successfully")
    return decrypted_text_data



def hide_text_dwt():
    global stego_image

    if not covimage or not text_path:  # Check if either cover image or text file is missing
            messagebox.showerror("Error", "Cover image or text file is missing.")
            return
    
    # Load cover image
    cover_image = np.array(Image.open(covimage))

    # Input text and flag
    with open(text_path, 'r') as f:
        secret_text = f.read().strip()
    flag = "FLAG_END"

    # Generate a random AES key
    key = os.urandom(32)
    
    messagebox.showinfo("save", "please save your key")

    key_path = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")), defaultextension=".txt")
    with open(key_path, 'w') as f:
        f.write('Key: ' + str(key.hex()))
    
    
    messagebox.showinfo("save", "your key saved succesfully \nplease wait untill process finish")


    # Convert text to binary format
    binary_text = textdwt.text_to_binary(secret_text, flag, key)
    
    try:
        # Hide text in the cover image
     stego_image = textdwt.hide_text_in_image(cover_image, binary_text, 0) # 0 for R, 1 for G, 2 for B
    except ValueError:
        messagebox.showerror("Error", "Cover image and binary text have incompatible dimensions. \n try another cover image.")
        return
    
    # Save the stego image
    stego_image = Image.fromarray(stego_image)

    show_stego(stego_image)
    PSNR(covimage,stego_image)
    messagebox.showinfo("hide", "text hide succesfully")
    return stego_image

def extract_text_dwt(key1):
    global extracted_text

    # Check if key and iv are provided
    if not key1 :
        messagebox.showerror("Error", "Key not provided!")
        return

    messagebox.showinfo("extract", "please wait untill process finish")

    # Load stego image
    stego_image = np.array(Image.open(stegoimage))
    flag = "FLAG_END"
    key=bytes.fromhex(key1)
    # Extract text from stego image
    try:
        # Decrypt the extracted encrypted text data
        extracted_text = textdwt.extract_text_from_image(stego_image, 0, flag, key)  # 0 for R, 1 for G, 2 for B
    except ValueError:
        messagebox.showerror("Error", "Decryption failed - possibly due to invalid key.")
        return
    
    
    messagebox.showinfo("hide", "text extract succesfully")

    return extracted_text
    
    
def hide_audio_LSB():
    global stego_image

    if not covimage or not audio_path:  # Check if either cover image or text file is missing
        messagebox.showerror("Error", "Cover image or audio file is missing.")
        return
    
    with open(audio_path, 'rb') as f:
        secret_audio_data = f.read()

    # Load the cover image
    
    cover_image = Image.open(covimage).convert('RGB')

    # Use the correct key and initialization vector (IV) for your encryption
    key = os.urandom(32)  # This should be your actual key
    iv = os.urandom(16)   # This should be your actual IV

    messagebox.showinfo("save", "please save your key")

    key_path = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")), defaultextension=".txt")
    with open(key_path, 'w') as f:
        f.write('Key: ' + str(key.hex()) + '\n' + '\n')
        f.write('IV: ' + str(iv.hex()))
            
    messagebox.showinfo("save", "your key saved succesfully \nplease wait untill process finish")
    
    # Encrypt the secret audio
    encrypted_audio_data = audio.encrypt_audio(secret_audio_data, key, iv)

    # Define the flag to indicate the end of the secret data
    flag = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    try:
        # Hide the encrypted secret audio data in the cover image
     stego_image = audio.hide_data_in_image(cover_image, encrypted_audio_data, flag)
    except ValueError:
        messagebox.showerror("Error", "Possibly due to invalid cover image.")
        return


    

    
    show_stego(stego_image)
    PSNR(covimage,stego_image)
    messagebox.showinfo("hide", "Audio hide succesfully")
      
    
def extract_audio_LSB(key1,iv1):
    global decrypted_audio_data

    # Check if key and iv are provided
    if not key1 or not iv1:
        messagebox.showerror("Error", "Key or IV not provided!")
        return

    messagebox.showinfo("extract", "please wait untill process finish")

    stego_image = Image.open(stegoimage).convert('RGB')
    
    # Define the flag to indicate the end of the secret data
    flag = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    # Extract the encrypted secret audio data from the stego image
    extracted_encrypted_audio_data = audio.extract_data_from_image(stego_image, flag)
    key=bytes.fromhex(key1)
    iv=bytes.fromhex(iv1)
    # Decrypt the extracted encrypted audio data
    try:
        # Decrypt the extracted encrypted text data
        decrypted_audio_data = audio.decrypt_audio(extracted_encrypted_audio_data, key, iv)
    except ValueError:
        messagebox.showerror("Error", "Decryption failed - possibly due to invalid key or IV.")
        return
    

    messagebox.showinfo("extract", "audio extracted succesfully")

def hide_audio_dwt():
    global stego_image

    if not covimage or not audio_path:  # Check if either cover image or text file is missing
        messagebox.showerror("Error", "Cover image or audio file is missing.")
        return
    
    # Load cover image
    cover_image = Image.open(covimage)
    cover_image = np.array(cover_image)

    # Input audio file and flag
    audio_file = audio_path
    flag = "FLAG_END"

    # Generate a random AES key
    key = os.urandom(32)
    
    messagebox.showinfo("save", "please save your key")

    key_path = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")), defaultextension=".txt")
    with open(key_path, 'w') as f:
        f.write('Key: ' + str(key.hex()) )
    
    messagebox.showinfo("save", "your key saved succesfully \nplease wait untill process finish")

    # Convert audio to binary format
    binary_audio = audiodwt.audio_to_binary(audio_file, flag, key)

    try:
        # Hide audio in the cover image
     stego_image = audiodwt.hide_audio_in_image(cover_image, binary_audio, 0)  # 0 for R, 1 for G, 2 for B
    except ValueError:
        messagebox.showerror("Error", messagebox.showerror("Error", "Cover image and binary text have incompatible dimensions. \n try another cover image."))
        return

    # Save the stego image
    stego_image = Image.fromarray(stego_image)

    show_stego(stego_image)
    PSNR(covimage,stego_image)
    messagebox.showinfo("hide", "file saved")
    
    return stego_image

def extract_audio_dwt(key1):
    global extracted_audio,audio_params
    
    # Check if key and iv are provided
    if not key1 :
        messagebox.showerror("Error", "Key not provided!")
        return

    messagebox.showinfo("extract", "please wait untill process finish")

    # Load stego image
    stego_image = np.array(Image.open(stegoimage))
    flag = "FLAG_END"
    key=bytes.fromhex(key1)
    # Extract audio from stego image
    try:
        # Decrypt the extracted encrypted text data
        extracted_audio, audio_params = audiodwt.extract_audio_from_image(stego_image, 0, flag, key)   # 0 for R, 1 for G, 2 for B
    except ValueError:
        messagebox.showerror("Error", "Decryption failed - possibly due to invalid key.")
        return

    messagebox.showinfo("extract", "Audio extracted succesfully")

    return extracted_audio, audio_params
    

def hide_image_LSB():
    global stego_image

    if not covimage or not secimage:  # Check if either cover image or text file is missing
        messagebox.showerror("Error", "Cover image or secret image is missing.")
        return
    # Load the secret image
    secret_image = Image.open(secimage).convert('RGB')

    # Load the cover image
    cover_image = Image.open(covimage).convert('RGB')

    # Use the correct key and initialization vector (IV) for your encryption
    key = os.urandom(32)  # This should be your actual key
    iv = os.urandom(16)   # This should be your actual IV

    messagebox.showinfo("save", "please save your key")

    key_path = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")), defaultextension=".txt")
    with open(key_path, 'w') as f:
        f.write('Key: ' + str(key.hex()) + '\n' + '\n')
        f.write('IV: ' + str(iv.hex()))

    messagebox.showinfo("save", "your key saved succesfully \nplease wait untill process finish")

    # Convert the secret image to bytes
    secret_image_data = image.image_to_bytes(secret_image)

    # Encrypt the secret image
    encrypted_image_data = image.encrypt_image(secret_image_data, key, iv)

    # Define the flag to indicate the end of the secret data
    flag = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    try:
        # Hide the encrypted secret image data in the cover image
     stego_image = image.hide_data_in_image(cover_image, encrypted_image_data, flag)
    except ValueError:
        messagebox.showerror("Error", "possibly due to invalid cover image.")
        return

    
    

    show_stego(stego_image)
    PSNR(covimage,stego_image)
    messagebox.showinfo("hide", "image hide succesfully")


def extract_image_LSB(key1,iv1):
    global decrypted_image

    # Check if key and iv are provided
    if not key1 or not iv1:
        messagebox.showerror("Error", "Key or IV not provided!")
        return

    messagebox.showinfo("extract", "please wait untill process finish")
    stego_image = Image.open(stegoimage).convert('RGB')
    # Define the flag to indicate the end of the secret data
    flag = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    # Extract the encrypted secret image data from the stego image
    extracted_encrypted_image_data = image.extract_data_from_image(stego_image, flag)
    key=bytes.fromhex(key1)
    iv=bytes.fromhex(iv1)
    # Decrypt the extracted encrypted image data
    try:
        # Decrypt the extracted encrypted text data
        decrypted_image_data = image.decrypt_image(extracted_encrypted_image_data, key, iv)
    except ValueError:
        messagebox.showerror("Error", "Decryption failed - possibly due to invalid key or IV.")
        return
    
    # Convert the decrypted image bytes back to an image
    decrypted_image = image.bytes_to_image(decrypted_image_data)

    show_secret(decrypted_image)
    messagebox.showinfo("extract", "image extracted succesfully")

def hide_image_DWT():
    global stego_image

    if not covimage or not secimage:  # Check if either cover image or text file is missing
        messagebox.showerror("Error", "Cover image or secret image is missing.")
        return

    # Load cover image
    cover_image = np.array(Image.open(covimage))

    # Input secret image file
    secret_image_file = secimage

    # Generate an AES key
    key = os.urandom(32)

    messagebox.showinfo("save", "please save your key")
    
    key_path = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")), defaultextension=".txt")
    with open(key_path, 'w') as f:
        f.write('Key: ' + str(key.hex()) + '\n' + '\n')

    messagebox.showinfo("save", "your key saved succesfully \nplease wait untill process finish")
        

    # Convert secret image to binary format
    binary_image = imagedwt.image_to_binary(secret_image_file, key)

    try:
        # Hide secret image in the cover image
     stego_image1 = imagedwt.hide_image_in_image(cover_image, binary_image, 0)  # 0 for R, 1 for G, 2 for B
    except ValueError:
        messagebox.showerror("Error", messagebox.showerror("Error", "Cover image and binary text have incompatible dimensions. \n try another cover image."))
        return

    

    # Save the stego image
    stego_image = Image.fromarray(np.uint8(stego_image1))

    show_stego(stego_image)
    PSNR(covimage,stego_image)
    messagebox.showinfo("hide", "image hide succesfully")

    return stego_image

def extract_image_dwt(key1):
    global decrypted_image

    # Check if key and iv are provided
    if not key1 :
        messagebox.showerror("Error", "Key not provided!")
        return
    
    messagebox.showinfo("extract", "please wait untill process finish")
    
    stego_image = np.array(Image.open(stegoimage))

    key=bytes.fromhex(key1)
    # Extract secret image from stego image
    try:
        # Decrypt the extracted encrypted text data
        extracted_image = imagedwt.extract_image_from_image(stego_image, 0, key)  # 0 for R, 1 for G, 2 for B
    except ValueError:
        messagebox.showerror("Error", "Decryption failed - possibly due to invalid key.")
        return
    

    # Save extracted image to a file
    decrypted_image = Image.fromarray(np.uint8(extracted_image))

    show_secret(decrypted_image)
    messagebox.showinfo("extract", "image extracted succesfully")

    return decrypted_image
         
my_font=('times', 20, 'bold')
my_font2=('times', 15, 'bold')
my_font3=('Source Sans Pro', 30, 'bold')
root = Tk()
root.title("SCIS")
app(root)
root.mainloop()