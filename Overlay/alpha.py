from tkinter import *
import win32com.client
import tkinter


#Get Active instance of PPT

PPTApp = win32com.client.GetActiveObject("PowerPoint.Application")

#Get Active presentation, must be active as presentation

PPTPresentation = PPTApp.ActivePresentation

def changeSlides(arg):
    if arg == "Next":
        PPTPresentation.SlideShowWindow.View.Next()
    if arg == "Prev":
        PPTPresentation.SlideShowWindow.View.Previous()


#Entry point to PPT Object Controls, create new instance
# app = win32com.client.Dispatch("PowerPoint.Application")

#Object containing open ppt containing objCOM, direct handle on "presentation" object level in VBA
#https://learn.microsoft.com/en-us/office/vba/api/overview/library-reference/reference-object-library-reference-for-office
#https://learn.microsoft.com/en-us/office/vba/api/overview/powerpoint
# class ppt:
#     def __init__(self):
#         self.objCOM = app.Presentations.Open(FileName="path_to_file",    WithWindow=1)


root = Tk()
root.title('LIDAR Overlay')
root.geometry("500x500")


root.wm_attributes("-topmost", 1)
root.attributes('-alpha',0.5)

#anything set to red will become transparent
root.wm_attributes('-transparentcolor','red')
# 
trans_frame = Frame(root,bg="red")
trans_frame.pack(fill = BOTH, expand = True)

back_button = tkinter.Button(trans_frame, width=25, height = 5, text = "Prev", command=lambda: changeSlides("Prev"))
back_button.pack()

next_button = Button(trans_frame, width=25, height = 5, text = "Next",command=lambda: changeSlides("Next"))
next_button.pack()

root.mainloop()