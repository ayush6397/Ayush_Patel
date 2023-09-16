from tkinter import *
rt=Tk()
rt.title("Admission form")
rt.minsize(100,100)

Label(rt,text="Noida Institute Of Engineering And Technology",fg="black",font="blue 20 bold").grid(padx=10,pady=5,row=0,column=3)

Label(rt,text="Registration Form",fg="white",font="DubaiMedium 12 bold",bg="black").grid(padx=10,pady=5,row=2,column=3)


Label(rt,text="1. Name of the Applicant").grid(padx=20,pady=5,row=5,column=2)

nameval=StringVar()
nameentry=Entry(rt,textvariable=nameval).grid(padx=20,row=5,column=3)


Label(rt,text="2. Father's/Guardian Name").grid(padx=20,pady=5,row=7,column=2)

fatherval=StringVar()
fatherentry=Entry(rt,textvariable=fatherval).grid(padx=20,row=8,column=2)

Label(rt,text="3. Mother's Name").grid(padx=20,pady=5,row=9,column=2)

motherval=StringVar()
Entry(rt,textvariable=motherval).grid(padx=20,row=10,column=2)

Label(rt,text="4. Gender").grid(padx=20,pady=5,row=11,column=2)
val=StringVar()
val1=StringVar()
Checkbutton(text="Male",variable=val).grid(padx=20,row=12,column=2)
Checkbutton(text="Female",variable=val1).grid(padx=20,row=12,column=3)


Label(rt,text="5. Phone Number").grid(padx=20,pady=5,row=13,column=2)

phoneval=IntVar()
Entry(rt,textvariable=phoneval).grid(padx=20,row=14,column=2)

Label(rt,text="6. Email").grid(padx=20,pady=5,row=15,column=2)

email=StringVar()
Entry(rt,textvariable=email).grid(padx=20,row=16,column=2)

def submit():
    print(f"{nameval.get(),fatherval.get(),motherval,get(),phoneval.get(),email.get()}")
    with open("admission.txt","w") as f:
        f.read(f"{nameval.get(),fatherval.get(),motherval,get(),phoneval.get(),email.get()}")
Button(rt,text="submit details",command=submit).grid(padx=30,pady=5,row=17,column=3)

mainloop()
