from tkinter import *

app = Tk()

app.title('SEaD v0.0')
app.geometry('500x300')
app.minsize(500, 300)
app.maxsize(500, 300)

bEncode = Button(app, text='Encode')
bEncode.place(x=35, y=220, width=150)

bDecode = Button(app, text='Decode')
bDecode.place(x=315, y=220, width=150)

txtBox = Text(app)
txtBox.place(x=20, y=40, width=460, height=150)

app.mainloop()
