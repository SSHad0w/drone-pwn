from tkinter import *

mainWindow = Tk()

mainWindow.geometry("700x400")


Label_title = Label(mainWindow, text = 'FlyForWarD', font=('Bahnschrift SemiLight',25))
Label_IsConnected = Label(mainWindow, text = "IsConnected", font=('Bahnschrift SemiLight',20))
TextBox_IsConnected = Entry(mainWindow, text ="N/A", font = ('serif',15))
Label_Coordinates = Label(mainWindow, text = "Coordinates", font=('Bahnschrift SemiLight',20))
TextBox_Coordinates = Entry(mainWindow, text ="N/A", font = ('serif',15))

#Placing the Label at the middle of the root window
# relx and rely should be properly set to position
# the label on root window
Label_title.place(relx = 0.2, rely = 0.1, anchor = 'center')
Label_IsConnected.place(relx = 0.2, rely = 0.3, anchor = 'center')
TextBox_IsConnected.place(relx = 0.2, rely = 0.4,anchor = 'center')
Label_Coordinates.place(relx = 0.2, rely = 0.5, anchor = 'center')
TextBox_Coordinates.place(relx = 0.2, rely = 0.6, anchor = 'center')



print("Test")
mainWindow.mainloop()

#Use to create textboxes:
#https://codeloop.org/how-to-create-textbox-in-python-tkinter/

