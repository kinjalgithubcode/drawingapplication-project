import tkinter
from tkinter import*
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab #used to save image file on local computer

#creating a Tkinter Window GUI

class Draw():
    def __init__(self,root):
        self.root=root
        self.root.title("Drawing Application")
        self.root.geometry("1320x700+0+0")
        self.root.configure(background="white")
        self.root.resizable(0,0)#use for can not increase or decrease size of window

#variables for pointer and Eraser
        self.pointer="black"
        self.eraser_color="white"

        title_lbl = Label(self.root,text = "Drawing Application in Python",font = ("arial",25,"bold"),bg = "black",fg = "orange")
        title_lbl.place(x = 90,y = 15,width = 900,height = 35)
        

#Widgets for Tkinter Window

#Pick a color for drawing from color pannel
        self.pick_color=LabelFrame(self.root,text='Colors',font=('arial',15),bd=5,relief=RIDGE,bg="white")
        self.pick_color.place(x=0,y=40,width=85,height=180)
        
        colors=['blue','red','green','orange','violet','black','yellow','purple','pink','gold','brown','indigo']
        i=j=0
        for color in colors:
            Button(self.pick_color,bg=color,bd=2,relief=RIDGE,width=4,command=lambda col=color:self.select_color(col)).grid(row=i,column=j)
            i+=1
            if i==6:
                i=0
                j=1   
#Erase Button and its properties
        self.eraser_btn=Button(self.root,text="Eraser",bd=4,bg='white',command=self.eraser,width=10,relief=RIDGE)
        self.eraser_btn.place(x=0,y=220)
        
#Reset Button to clear the entier screen
        self.clear_screen=Button(self.root,text="clear",bd=4,bg='white',command=lambda:self.background.delete('all'),width=10,relief=RIDGE)
        self.clear_screen.place(x=0,y=250)

#Save Button to saving the image in local computer
        self.save_btn=Button(self.root,text="Save",bd=4,bg='white',command=self.save_drawing,width=10,relief=RIDGE)
        self.save_btn.place(x=0,y=280)

#Background Button for choosing color of the canvas
        self.bg_btn=Button(self.root,text="Canvas",bd=4,bg='white',command=self.canvas_color,width=10,relief=RIDGE)
        self.bg_btn.place(x=0,y=310)

        self.new_btn=Button(title_lbl,text="New",bd=4,bg='green',fg='white',command=self.new,width=10,relief=RIDGE)
        self.new_btn.place(x=0,y=0)

        self.exit_btn=Button(title_lbl,text="Exit",bd=4,bg='green',fg='white',command=self.iexit,width=10,relief=RIDGE)
        self.exit_btn.place(x=813,y=0)

#Creating a Scale for pointer and eraser size
        self.pointer_frame=LabelFrame(self.root,text='size',bd=5,bg='white',font=('arial',15,'bold'),relief=RIDGE)
        self.pointer_frame.place(x=0,y=339,height=200,width=85)

        self.pointer_size=Scale(self.pointer_frame,orient=VERTICAL,from_=48,to=0,length=168)
        self.pointer_size.set(1)
        self.pointer_size.grid(row=0,column=1,padx=15)

#Defining a background color for the Canvas
        self.background=Canvas(self.root,bg='white',bd=5,relief=GROOVE,height=477,width=900)
        self.background.place(x=85,y=50)

#Bind the background Canvas with mouse click
        self.background.bind("<B1-Motion>",self.paint)

#Functions are defined here
    def paint(self,event):
        x1,y1=(event.x-2),(event.y-2)
        x2,y2=(event.x+2),(event.y+2)

        self.background.create_oval(x1,y1,x2,y2,fill=self.pointer,outline=self.pointer,width=self.pointer_size.get())
        

#Paint Function for Drawing the lines on Canvas
    def select_color(self,col):
        self.pointer=col

#Function for defining the eraser
    def eraser(self):
        self.pointer=self.eraser_color
        
#Function for choosing the background color of the canvas
    def canvas_color(self):
        color=colorchooser.askcolor()
        self.background.configure(background=color[1])
        self.eraser_color=color[1]

    def new(self):
        self.background=Canvas(self.root,bg='white',bd=5,relief=GROOVE,height=477,width=900)
        self.background.place(x=85,y=50)

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Drawing Application","Are you sure exit this project",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return
    


#Function for saving the image file in local computer
    def save_drawing(self):
        try:
            #self.background update()
            file_ss=filedialog.asksaveasfilename(defaultextension='jpg')
            #print(file_ss)
            x=self.root.winfo_rootx()+self.background.winfo_x()
            #print(x,self.background.winfo_x())
            y=self.root.winfo_rooty()+self.background.winfo_x()
            #print(y)

            x1=x+self.background.winfo_width()
            #print(x1)
            y1=y+self.background.winfo_height()
            #print(y1)
            ImageGrab.grab().crop((x,y,x1,y1)).save(file_ss)
            messagebox.showinfo('Screenshot Successfully Saved as'+str(file_ss))
        except:
            print("Error in saving the screenshot")
             
            
        
        
if __name__ =="__main__":
    root=Tk()
    p=Draw(root)
    root.mainloop()#use for holding the GUI page
