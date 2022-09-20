


    
import tkinter as tk
#from tkinter import filedialog as fd
from tkinter import *  
import tkinter.ttk as ttk
from PIL import Image, ImageTk, ImageGrab
import pyscreenshot as ImageGrab
import pygame
import win32api
import win32con
import win32gui
from tkinter.filedialog import askdirectory, asksaveasfilename
from tkinter.colorchooser import *
import sys
    
#import pyperclip3 as pc
#from io import BytesIO
  



def destroy():
    root.destroy()
 
root = tk.Tk()
root.iconbitmap(r'screen.ico')
b = tk.Button(root, text="Click to Capture screen",
    fg='red',
    bg='yellow',
    font="Arial 16",
    relief=tk.GROOVE ,
    borderwidth=10,
    command=root.destroy)
b.pack()
root.mainloop()

def grab(x, y, w, h):
    global done   
    im = ImageGrab.grab(bbox=(x, y, w, h))
    im.save('clipboard.jpg')
    done = True

pygame.init()
info = pygame.display.Info()
w = info.current_w
h = info.current_h
screen = pygame.display.set_mode((w, h), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
done = False
fuchsia = (255, 0, 128)  # Transparency color
 
# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
# win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 50, win32con.LWA_ALPHA)
 
click1 = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0
while not done:
    for event in pygame.event.get():
       
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # time.sleep(.1)
                if click1 == 0:
                    x1, y1 = pygame.mouse.get_pos()
                    click1 = 1
                elif click1 == 1:
                    x2, y2 = pygame.mouse.get_pos()
                    dx = x1 + (x2 - x1)
                    dy = y1 + (y2 - y1)
                    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_ALPHA)
                    grab(x1, y1, dx, dy)
                    click1 = 0
                    # Sh
                    # done = True
                    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 50, win32con.LWA_ALPHA)
                    x1 = 0
                    y1 = 0
                    x2 = 0
                    y2 = 0
                    #preview()
                    #count_image = int(count_image)
                    #count_image += 1
 
    screen.fill((255, 255, 255))  # Transparent background
    # show_text()
    if click1 == 0:
        mx, my = pygame.mouse.get_pos()
        dx = 5
        dy = 5
    elif click1 == 1:
        mx2, my2 = pygame.mouse.get_pos()
        x2 = mx2 - x1
        y2 = my2 - y1
 
    pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(mx, my, x2, y2))
    pygame.display.update()
if done == True:   
    pygame.quit()
    #sys.exit()
color_w="white"
im = Image.open("clipboard.jpg")
window = tk.Tk()
window.iconbitmap(r'screen.ico')
window.title("Screen Shot")
frame1 = tk.Frame(master=window, height=50, bg="light gray")
frame1.pack(fill=tk.X)
c = Canvas(master=window, width=600, height=450,bg="gray")
c.pack( side=tk.LEFT,  padx=0, pady=0, expand=True)
image = Image.open("clipboard.jpg")
bg1 = ImageTk.PhotoImage(image)
bg_size=image.size
c.configure(width=bg_size[0], height=bg_size[1])
c.create_image(0,0, image = bg1, anchor=NW)
c.image = bg1
            
def change_color_b():
    global color_w
    colors = askcolor(title="Tkinter Color Chooser")
    window.configure(bg=colors[1])
    color_w = colors[1]
    c.configure(bg=color_w)
    
    return color_w

def save_as_jpg():
        print(c.winfo_rootx(), c.winfo_x())
        filepath = asksaveasfilename(
            defaultextension="jpg",
            filetypes=[("Формат JPG", "*.jpg"),])
        if not filepath:
            return
        
        with open(filepath, "w") as output_file:
            box = (c.winfo_rootx(),c.winfo_rooty(),c.winfo_rootx()+c.winfo_width(),c.winfo_rooty() + c.winfo_height())
            grab = ImageGrab.grab(bbox = box)
            grab.save(output_file)
            
        window.title(f"Простий графічний редактор - {filepath}")

menubar = Menu(window)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Експорт .jpg", command= save_as_jpg)
menubar.add_cascade(label="Файл", menu=file_menu)
window.configure(menu=menubar)


#color_lab = tk.Label(master=frame1, text="Товщина лінії: ", bg="light gray")  # створюєм назву повзунка для товщини лінії
#color_lab.pack (side='left')
brush_size = 1
color = "black"

def changeW(e):
     #change Width of pen through slider
    brush_size = e

def set_brush_size(value):
    global brush_size
    brush_size = int(value)
    return brush_size

scale1 = Scale(master=frame1,orient=HORIZONTAL,length=300,from_=1,to=100,tickinterval=10,resolution=1, command=set_brush_size) # створюєм повзунок для товщини лінії
scale1.pack(side='left')

def change_color():
    global color
    colors = askcolor(title="Tkinter Color Chooser")
    window.configure(bg=colors[1])
    color = colors[1]
    return color

# функція малювання ліні
def line():
    global n
    n=0
    global x
    x=[]
    global line2
    line2=[]
    line1 = None
    global spline
    spline = False
    global line
    line = True
    global flower
    flower = False
    global polygon
    polygon = False
    global polygon_fill
    polygon_fill = False
    global oval
    oval = False
    global oval_fill
    oval_fill = False
    global text
    text = False
    class Point:
        def xy1(self,e):
            self.x1 = e.x
            self.y1 = e.y

        def poly3(self,e):
            self.x1 = e.x
            self.y1 = e.y
            self.x0 = self.x1
            self.y0 = self.y1
            if line:
                c.create_line(self.x1,self.y1,self.x1,self.y1,width=brush_size,fill=color,capstyle=ROUND)
                #print('line is...')

        def xy2(self,e):
            self.x2 = e.x
            self.y2 = e.y
            if line:
                c.create_line(self.x0,self.y0,self.x2,self.y2,width=brush_size,fill=color,capstyle=ROUND)

        def xy3(self,e):
            global line2
            global x
            global n
          
            self.x2 = e.x
            self.y2 = e.y
            if line:
                line1 = c.create_line(self.x0,self.y0,self.x2,self.y2,width=brush_size,fill=color,capstyle=ROUND)
            x.append(self.x2)
            line2.append(line1)
            n=n+1
            #print(n)
            #print(line2)

                
            if n > 1:
                c.delete(line2[n-2])
               
    p = Point()
    c.bind("<B1-Motion>", p.xy3)
    c.bind("<Button-1>",p.poly3)
    c.bind("<ButtonRelease-1>", p.xy2)

# функція виділення
def spline():
    global spline
    spline = True
    global line
    line = False
    global flower
    flower = False
    global oval
    oval = False
    global oval_fill
    oval_fill = False
    global text
    text = False
    class Point2:
        def xy1(self,e):
            if spline:
                c.create_line(self.x1,self.y1,e.x,e.y,width=brush_size,fill=color,capstyle=ROUND,stipple='gray25')
            self.x1 = e.x
            self.y1 = e.y

        def poly2(self,e):
            self.x1 = e.x
            self.y1 = e.y
            self.x0 = self.x1
            self.y0 = self.y1
            
        def xy2(self,e):
            self.x2 = e.x
            self.y2 = e.y
        
    p = Point2()
    c.bind("<B1-Motion>", p.xy1)
    c.bind("<Button-1>",p.poly2) 
    c.bind("<ButtonRelease-1>", p.xy2)


def oval():
    global oval
    oval = True
    global n1
    n1=0
    global oval2
    oval2=[]
    global spline
    spline = False
    global line
    line = False
    global flower
    flower = False
    global rect_fill
    rect_fill = False
    global oval_fill
    oval_fill = False
    global text
    text = False
    class Oval:
        def poly(self, e):
            self.x1 = e.x
            self.y1 = e.y

        def poly2(self, e):
            self.x2 = e.x
            self.y2 = e.y
            if oval:
                c.create_oval(self.x1, self.y1, self.x2, self.y2,
                              fill='',  outline=color,width = brush_size)

        def poly3(self, e):
            global n1
            self.x2 = e.x
            self.y2 = e.y
            if oval:
                oval1 = c.create_oval(self.x1, self.y1, self.x2, self.y2,
                              fill='',  outline=color,width = brush_size)
                oval2.append(oval1)
                n1 = n1+1
                if n1 > 1:
                    c.delete(oval2[n1-2])
    p1 = Oval()
    c.bind("<B1-Motion>", p1.poly3)
    c.bind("<Button-1>", p1.poly)
    c.bind("<ButtonRelease-1>", p1.poly2)



def rect():
    global n1
    n1=0
    global rect2
    rect2=[]
    global spline
    spline = False
    global line
    line = False
    global flower
    flower = False
    global rect
    rect = True
    global rect_fill
    rect_fill = False
    global oval
    oval = False
    global oval_fill
    oval_fill = False
    global text
    text = False
    class Rectangle:
        def poly(self, e):
            self.x1 = e.x
            self.y1 = e.y

        def poly2(self, e):
            self.x2 = e.x
            self.y2 = e.y
            if rect:
                c.create_polygon(self.x1, self.y1,self.x1 + (self.x2 - self.x1), self.y1, self.x2, self.y2,
                             self.x1 , self.y1 + (self.y2-self.y1), fill='',  outline=color,width = brush_size,joinstyle = MITER, smooth=0)

        def poly3(self, e):
            global n1
            self.x2 = e.x
            self.y2 = e.y
            if rect:
                rect1 = c.create_polygon(self.x1, self.y1,self.x1 + (self.x2 - self.x1), self.y1, self.x2, self.y2,
                                self.x1 , self.y1 + (self.y2-self.y1), fill='', outline=color, width = brush_size,joinstyle = MITER, smooth=0)
                rect2.append(rect1)
                n1 = n1+1
                if n1 > 1:
                    c.delete(rect2[n1-2])
    p1 = Rectangle()
    c.bind("<B1-Motion>", p1.poly3)
    c.bind("<Button-1>", p1.poly)
    c.bind("<ButtonRelease-1>", p1.poly2)





def polygon():
    global polygon
    polygon = True
    
    global rect
    rect = False
    global line
    line = False
    global oval
    oval = False
    
    global text
    text = False

    class Poly:
        def __init__(self):
            self.coord=[]
            self.line2 = []
            self.line1 = True
            self.n = 0
            self.n1 = 0

        def points(self, e):
            self.coord.append(e.x)
            self.coord.append(e.y)
            
            if self.n >= 2 :
                if polygon:
                    c.create_line(self.coord[self.n-2],self.coord[self.n-1],self.coord[self.n],self.coord[self.n+1],fill=color,width=brush_size,capstyle=ROUND)
            self.n += 2

        def poly(self, coord):
            if polygon:
                c.create_polygon(self.coord, fill='',  outline=color,width = brush_size,joinstyle = MITER, smooth=0)
            self.coord.clear()
            self.n = 0

        def line(self,e):
                self.x2 = e.x
                self.y2 = e.y
                if polygon:
                    line1 = c.create_line(self.coord[self.n-2],self.coord[self.n-1],self.x2,self.y2,fill=color, dash=(3,5),capstyle=ROUND)
                #print(self.coord, self.n)
                #x.append(self.x2)
                self.line2.append(line1)
                self.n1=self.n1+1
                if self.n > 1:
                    c.delete(self.line2[self.n1-2])
                
    p1 = Poly()
    c.bind("<Button-1>", p1.points)
    c.bind("<Double-Button-1>", p1.poly)
    c.bind("<Motion>", p1.line)

def text():
    global text
    text = True
    global line
    line = False
    global oval
    oval = False
    global rect
    rect = False
    global polygon
    polygon = False
    global spline
    spline = False
    class Text:
        def __init__(self):
            self.coord=[]
            self.h = 1
            self.t_len =0
            self.max_w = 1
            self.text_box = tk.Text(height = self.h, width = 1, state='normal',font=("Helvetica",14))
          
        def points(self, e):
            self.coord.append(e.x)
            self.coord.append(e.y)
            print(self.coord, e)
            if text:
                c.create_window(self.coord,anchor="nw",window=self.text_box)
                self.text_box.focus()
                self.coord.clear()   
            self.text_box.bind("<Return>", t.conf_h)
            self.text_box.bind("<Key>", t.width_t_box)

        def conf_h(self, e):
            self.h  = self.h + 1
            self.text_box.config(height = self.h)
            if self.h >= 2:
                if self.t_len > self.max_w:
                    self.max_w = self.t_len
            self.text_box.config(width = self.max_w)
            self.t_len =0
            print('E key pressed, max_w = ', self.max_w)
            

        def width_t_box(self,e):
            self.t_len = self.t_len + 1
            self.text_box.configure(width = self.t_len)
            if self.max_w < self.t_len:
                self.text_box.configure(width = self.t_len)
            else:
                self.text_box.configure(width = self.max_w)    
            
    t=Text()       
    c.bind("<Button-1>", t.points)
    t.width_t_box()

but_line = PhotoImage(file="line.png")
but_line = but_line.subsample(5,5)

but_hilight = PhotoImage(file="hilight.png")
but_hilight = but_hilight.subsample(5,5)

but_oval = PhotoImage(file="oval.png")
but_oval = but_oval.subsample(5,5)

but_rect = PhotoImage(file="rectangle.png")
but_rect = but_rect.subsample(5,5)

but_polygon = PhotoImage(file="polygon.png")
but_polygon = but_polygon.subsample(5,5)
but_text = PhotoImage(file="text.png")
but_text = but_text.subsample(5,5)

but_colors = PhotoImage(file="colors.png")
but_colors = but_colors.subsample(5,5)

sel_color = Button(master=frame1, image = but_colors,  command=change_color) # створюєм кнопку для вибору кльору
sel_color.pack (side='left')

draw_hilight = Button(master=frame1,image = but_hilight,  command=spline) # створюєм кнопку для виділення
draw_hilight.pack (side='left')

draw_line = Button(master=frame1,image = but_line,  command=line) # створюєм кнопку для ліній
draw_line.pack (side='left')
#draw_spline = Button(master=frame3, text="Сплайн", width=10,height=4,  command=spline) # створюєм кнопку для сплайнів

draw_oval = Button(master=frame1, image = but_oval,  command=oval) # створюєм кнопку для овалу
draw_oval.pack (side='left')

draw_rectangle = Button(master=frame1, image = but_rect,  command=rect) # створюєм кнопку для прямокутника прозорого
draw_rectangle.pack (side='left')

draw_polygon = Button(master=frame1, image = but_polygon,  command=polygon) # створюєм кнопку для багатокутника
draw_polygon.pack (side='left')

draw_text = Button(master=frame1, image = but_text,  command=text) # створюєм кнопку для багатокутника
draw_text.pack (side='left')
                        
def main():
            
    window.mainloop()

if __name__ == "__main__":

    main()