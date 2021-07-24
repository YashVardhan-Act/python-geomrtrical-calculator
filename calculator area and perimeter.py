import tkinter

root = tkinter.Tk()

root.title("Claculate Area And Perimeter Of Rectangle Easily")

root.geometry("600x250+50+50")
root.configure(background="white")

# Making The Text Boxes

label = tkinter.Label(root, text="Enter The Length")
label.pack()

length = tkinter.Entry(root, width=50, borderwidth=10)
length.pack()

label_1 = tkinter.Label(root, text="Enter The Breadth")
label_1.pack()

breadth = tkinter.Entry(root, width=50, borderwidth=10)
breadth.pack()

# Defining Area And Perimeter

area = length*breadth
perimeter = 2*(length+breadth)

l = float(length.get())
b = float(breadth.get())

# Making The Buttons

label2 = tkinter.Label(root, text="Tell What Do You Want To Calculate")
label2.pack()

btn_area = tkinter.Button(root, text="Area", command=area)
btn_area.pack()

btn_perimeter = tkinter.Button(root, text="Perimeter", command=perimeter)
btn_perimeter.pack()

root.mainloop()