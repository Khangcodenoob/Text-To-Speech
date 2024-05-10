#Đoạn 1
from tkinter import *
import tkinter as tk 
from tkinter import Label, Entry, Button ,messagebox, Toplevel
import pyttsx3
#Đoạn 2
def open_text_to_speech(username):
    def speak(text_to_speak):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        volume= engine.getProperty('rate') 
        engine.setProperty('rate', 200)
        engine.say(text_to_speak)
        engine.runAndWait()
#Đoạn 3       
    root.withdraw()    
    tts_window = Toplevel()  
    tts_window.title("Text To Speech")
    tts_window.geometry("450x350")
    root.iconbitmap('logo.ico')

    outside = LabelFrame(tts_window, text="Text To Speech", font=25, fg='red', bg='white', bd=7)
    outside.pack(padx=10, pady=10, expand="yes", fill="both")
    Label(outside, text="Text", font=15, fg='yellow', bg='black').pack(padx=10, side=tk.LEFT)

    listen = StringVar()
    entry = Entry(outside, width=30, font=25, bd=5, textvariable=listen)
    entry.pack(side=tk.LEFT)
    Button(outside, font=20, text="Enter", bg='red', fg='black', command=lambda: speak(listen.get())).pack(side=tk.RIGHT, padx=10)
    
    def on_close():
        tts_window.destroy()
        root.deiconify()
    tts_window.protocol("WM_DELETE_WINDOW", on_close)
#Đoạn 4  
    # Thêm menu (copy, paste, cut)
    def popup_menu(event):
        menu.post(event.x_root, event.y_root)

    menu = Menu(root, tearoff=0)
    menu.add_command(label="Cut", command=lambda: entry.event_generate("<<Cut>>"))
    menu.add_command(label="Copy", command=lambda: entry.event_generate("<<Copy>>"))
    menu.add_command(label="Paste", command=lambda: entry.event_generate("<<Paste>>"))

    entry.bind("<Button-3>", popup_menu)  #Liên kết sự kiện nhấp chuột phải để hiển thị menu ngữ cảnh
    tts_window.mainloop()
#Đoạn 5
def login( event = None):
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "123":
        messagebox.showinfo("Success", "Đăng nhập thành công!")
        open_text_to_speech(username)
    elif username == "admin1" and password == "123":
        messagebox.showinfo("Success", "Đăng nhập thành công!")
        open_text_to_speech(username)
    else:
        error_label.config(text="Tên đăng nhập hoặc mật khẩu không đúng!, Vui lòng nhập lại ")  
#Đoạn 6     
root = Tk()
root.title("Login")
root.geometry("300x150")
root.iconbitmap('logo.ico')

Label(root, text="Username:").pack()
username_entry = Entry(root, width=20)
username_entry.pack()

Label(root, text="Password:").pack()
password_entry = Entry(root, width=20, show="*")
password_entry.pack()

Button(root, text="Login", command=login).pack(pady=10)
error_label = Label(root, text="", fg="red")
error_label.pack()
root.bind('<Return>', login)

#Đoạn 7
engine = pyttsx3.init()
# Hàm cho cửa sổ thoát
def on_closing():
    if messagebox.askokcancel("Quit", "Bạn có chắc muốn thoát chương trình?"):
        root.destroy()
#Đoạn 8
# Khởi tạo công cụ chuyển văn bản thành giọng nói
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()


