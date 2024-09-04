from tkinter import*
# buttom cummant
def getvalues ():
    print (namevalues.get())
    print (rollvalues.get())
    print (addvalues.get())
    print (namevalues.get())


root = Tk()
root.geometry("600x450")

tit= Label(root,text= "cv from", fg="black",font="comicsansms 15 bold" ,bg= "white" ,).grid(row=0,column=3)


# create names
name = Label (root,text="Name :")
roll= Label (root,text="Roll :")
add= Label (root,text="Add :")
gender= Label (root,text="Gender :")

# packing names
name.grid(row=1,column=0)
roll.grid(row=2,column=0)
add.grid(row=3,column=0)
gender.grid(row=4,column=1)

# names entries value type

namevalues = StringVar()
rollvalues = IntVar()
addvalues = StringVar()
gendervalues = IntVar()
gendervalues2 = IntVar()

# entries 

nameentry = Entry (root,textvariable=namevalues,relief=SUNKEN)
rollentry = Entry (root,textvariable=rollvalues)
addentry = Entry (root,textvariable=addvalues)

# entries packing 

rollentry.grid(row=2,column=2)
nameentry.grid(row=1,column=2)
addentry.grid(row=3,column=2)

# buttom for summit
Button(root,text="summit" , command=getvalues).grid(row=5,column=1)
# check box
gender = Checkbutton(text="male", variable=gendervalues).grid(row=4,column=2)
gender1 = Checkbutton(text="famale", variable=gendervalues2).grid(row=4,column=3)

root.mainloop()