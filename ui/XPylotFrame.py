import tkinter
import customtkinter as ctk

class XPylotFrame(ctk.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("XPylot")
        self.geometry("1920x1080")

