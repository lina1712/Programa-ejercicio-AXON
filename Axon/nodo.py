import csv
from tkinter import Button, Label, Listbox, StringVar, Tk

filename = 'Anexo_AXON.csv'

with open( filename) as file:
    csv_reader = csv.reader(file, delimiter=';')
    new_list = list(csv_reader)
    del(new_list[0])

list_of_entries = []
for x in list(range(0,len(new_list))):
    list_of_entries.append(new_list[x][0])

root = Tk()
root.geometry('600x500')
var = StringVar(value = list_of_entries)
listbox1 = Listbox(root, listvariable = var)
listbox1.grid(row=0, column=0)

def update():
    index = listbox1.curselection()[0]
    namelabel2.config(text= new_list[index][0])
    MMS_PATHlabel2.config(text= new_list[index][1])
    LDlabel2.config(text= new_list[index][2])
    LNlabel2.config(text= new_list[index][3])
    DOlabel2.config(text= new_list[index][4])
    DAlabel2.config(text= new_list[index][5])
    BDAlabel2.config(text= new_list[index][6])
    BDA1label2.config(text= new_list[index][7])
    BDA2label2.config(text= new_list[index][8])
    BDA3label2.config(text= new_list[index][9])
    return None

button1 = Button(root, text="Update", command =update)
button1.grid(row=15, column=0)
namelabel = Label(root, text="Name"). grid(row=1, column=0, sticky="w")
MMS_PATHlabel = Label(root, text="MMS PATH").grid(row=2, column=0, sticky="w")
LDlabel = Label(root, text="LD"). grid(row=3, column=0, sticky="w")
LNlabel = Label(root, text="LN"). grid(row=4, column=0, sticky="w")
DOlabel = Label(root, text="DO"). grid(row=5, column=0, sticky="w")
DAlabel = Label(root, text="DA"). grid(row=6, column=0, sticky="w")
BDAlabel = Label(root, text="BDA"). grid(row=7, column=0, sticky="w")
BDA1label = Label(root, text="BDA"). grid(row=8, column=0, sticky="w")
BDA2label = Label(root, text="BDA"). grid(row=9, column=0, sticky="w")
BDA3label = Label(root, text="BDA"). grid(row=10, column=0, sticky="w")

namelabel2 = Label(root, text="")
namelabel2.grid(row=1, column=1, sticky="w")
MMS_PATHlabel2 = Label(root, text="")
MMS_PATHlabel2.grid(row=2, column=1, sticky="w")
LDlabel2 = Label(root, text="")
LDlabel2.grid(row=3, column=1, sticky="w")
LNlabel2 = Label(root, text="")
LNlabel2.grid(row=4, column=1, sticky="w")
DOlabel2 = Label(root, text="")
DOlabel2.grid(row=5, column=1, sticky="w")
DAlabel2 = Label(root, text="")
DAlabel2.grid(row=6, column=1, sticky="w")
BDAlabel2 = Label(root, text="")
BDAlabel2.grid(row=7, column=1, sticky="w")
BDA1label2 = Label(root, text="")
BDA1label2.grid(row=8, column=1, sticky="w")
BDA2label2 = Label(root, text="")
BDA2label2.grid(row=9, column=1, sticky="w")
BDA3label2 = Label(root, text="")
BDA3label2.grid(row=10, column=1, sticky="w")


root.mainloop()
