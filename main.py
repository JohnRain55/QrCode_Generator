from tkinter import *
import qrcode

root = Tk()
root.title("Qr generator")
root.geometry("1000x550")
root.config(bg="dark red")
root.resizable(False, False)


def generate():
    name = title.get()
    text = entry.get()
    qr = qrcode.make(text)
    qr.save("Qrcode/" + str(name) + ".png")


Label(root, text="Title", fg="white", bg="dark red", font=15).place(x=50, y=170)

title = Entry(root, width=13, font="arial 15")
title.place(x=50, y=200)

entry = Entry(root, width=28, font="arial 15")
entry.place(x=50, y=250)

Button(root, text="Generate", width=20, height=2, bg="white", fg="dark red", command=generate).place(x=50, y=300)
root.mainloop()
