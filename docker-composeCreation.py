from tkinter import *
import tkinter as tk
from tkinter import filedialog

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("480x240")
        self.title("Developer Environment Builder")
        self.VSCodeExtensionCheck = tk.IntVar(self)
        self.VSCodeID = tk.StringVar(self)
        self.createWidgets()

    def createWidgets(self):
        self.VSCodeLabelFrame = tk.LabelFrame(self,text='VS Code Extenions')
        self.VSCodeLabelFrame.grid(row=0,column=0)
        self.VSCodeExtensionCheckButton = tk.Checkbutton(self.VSCodeLabelFrame,text='Include VS Code Extensions?',variable=self.VSCodeExtensionCheck,onvalue=1,offvalue=0,command=self.VSCodeExtensionSelect)
        self.VSCodeExtensionCheckButton.grid(row=0,column=0,sticky='w')
        self.devEnvironmentCreateButton = tk.Button(text='Create Yaml for Dev Environment!',command=self.confirmationCreation)
        self.devEnvironmentCreateButton.grid(row=1,column=0)
    def VSCodeExtensionSelect(self):
        if self.VSCodeExtensionCheck.get() == 1:
            self.VSCodeIDEntry = tk.Entry(self.VSCodeLabelFrame,textvariable=self.VSCodeID)
            self.VSCodeIDEntry.grid(row=2,column=0)
            self.VSCodeIDLabel = tk.Label(self.VSCodeLabelFrame,text='Enter the VS Code Extension ID')
            self.VSCodeIDLabel.grid(row=1,column=0)
            self.VSCodeIDAdd = tk.Button(self.VSCodeLabelFrame,text='Add Extension',command=self.VSCodeIDGet)
            self.VSCodeIDAdd.grid(row=2,column=1)
        elif self.VSCodeExtensionCheck.get() == 0:
            self.VSCodeIDEntry.destroy()
            self.VSCodeIDLabel.destroy()
            self.VSCodeIDAdd.destroy()
    def VSCodeIDGet(self):
        self.VSCodeExtensionList = []
        self.VSCodeExtensionList.append('{}'.format(self.VSCodeID.get()))
    def confirmationCreation(self):
        self.confirmationWindow = Toplevel(self)
        self.confirmationWindow.title("Confirmation of Creation")
        self.confirmationWindow.geometry("200x200")
        self.confirmationLabel = tk.Label(self.confirmationWindow,text='{}'.format(self.VSCodeExtensionList))
        self.confirmationLabel.grid(row=0,column=0)
if __name__=="__main__":
    app = Menu()
    app.mainloop()
