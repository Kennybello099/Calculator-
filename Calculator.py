#__author__ = 'Bello Ahmad'
from tkinter import *
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.value = StringVar()


        self.value1 = Label(self, text="Type value1:", font="helvetica 10", height=4)
        self.value1.grid(row=1, column=0, sticky=E)
        self.entry1 = Entry(self, width=10)
        self.entry1.grid(row=1, column=1, sticky=W)

        self.value2 = Label(self, text="Type value2:", font="helvetica 10", height=6)
        self.value2.grid(row=2, column=0, sticky=E)
        self.entry2 = Entry(self, width=10)
        self.entry2.grid(row=2, column=1, sticky=W)

        self.label3 = Label(self, text="Result:", font="helvetica 10", height=9)
        self.label3.grid(row=18, column=0, sticky=E)
        self.result = Entry(self, width=15, bg="yellow")
        self.result.grid(row=18, column=1, sticky=W)

        self.plus = Button(self, text= "+", command=self.add, bg="green", fg="white", font="helvetica 10 bold",
                                                                                                        height=0,
                                                                                                        width=3)
        self.plus.grid(row=17, column=14, )

        self.minus = Button(self, text= "-", command=self.sub, bg="green", fg="white", font="helvetica 10 bold",
                                                                                                        height=0,
                                                                                                        width=3)
        self.minus.grid(row=17, column=18)

        self.multiply = Button(self, text= "*", command=self.mul, bg="green", fg="white", font="helvetica 10 bold",
                                                                                                            height=0,
                                                                                                            width=3)
        self.multiply.grid(row=17, column=22)

        self.divide = Button(self, text= "/", command=self.div, bg="green", fg="white", font="helvetica 10 bold",
                                                                                                        height=0,
                                                                                                        width=3)
        self.divide.grid(row=17, column=26)

        self.cleary = Button(self, text= "clr", command=self.clear, bg="green", fg="white", font="helvetica 10 bold",
                                                                                                            height=0,
                                                                                                            width=3)
        self.cleary.grid(row=17, column=28)

    def add(self):
        v1 = self.entry1.get()
        v2 = self.entry2.get()
        kenny = int(v1)+int(v2)
        self.result.insert(0, kenny)

    def sub(self):
        v1 = self.entry1.get()
        v2 = self.entry2.get()
        kenny = int(v1)-int(v2)
        self.result.insert(0, kenny)

    def mul(self):
        v1 = self.entry1.get()
        v2 = self.entry2.get()
        kenny = int(v1)*int(v2)
        self.result.insert(0, kenny)

    def div(self):
        v1 = self.entry1.get()
        v2 = self.entry2.get()
        kenny = int(v1)/int(v2)
        self.result.insert(0, kenny)


    def clear(self):
        self.result.delete(0, END)

        if (self.value.get() == "+"):
            return kenny

        elif (self.value.get() =="-"):
            return kenny
        elif (self.value.get() =="*"):
            return kenny
        elif (self.value.get() =="/"):
            return kenny
        elif (self.value.get() =="clr"):
            return kenny


window = Tk()
window.title("Calculator")
window.geometry('400x445')
app = Application(window)
app.mainloop()





