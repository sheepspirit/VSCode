# Пример 1

# from tkinter import *
 
 
# def change():
#     b1['text'] = "Изменено"
#     b1['bg'] = '#000000'
#     b1['activebackground'] = '#555555'
#     b1['fg'] = '#ffffff'
#     b1['activeforeground'] = '#ffffff'
 
 
# root = Tk()
# b1 = Button(text="Изменить", 
#             width=15, height=3)
# b1.config(command=change)
# b1.pack()
# root.mainloop()


# ПРимер 2

# from tkinter import *
 
# root = Tk()
 
# l1 = Label(text="Машинное обучение",
#            font="Arial 32")
 
# l2 = Label(text="Распознавание образов",
#            font=("Roboto",
#                  24, "bold"))
 
# l1.config(bd=20, bg='#ffaaaa')
# l2.config(bd=20, bg='#aaffff')
 
# l1.pack()
# l2.pack()
# root.mainloop()

# ПРимер 3


# from tkinter import *
# from datetime import datetime as dt
 
 
# def insert_time():
#     t = dt.now().time()
#     e1.insert(END, t.strftime('%H:%M:%S  '))
 
 
# root = Tk()
# e1 = Entry(width=50)
# but = Button(text="Время",
#              command=insert_time)
# e1.pack()
# but.pack()
# root.mainloop()


# Напишите программу, состоящую из семи кнопок,
# цвета которых соответствуют цветам радуги.
# При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета,
# а в метку – название цвета.
# Коды цветов в шестнадцатеричной кодировке:
# #ff0000 – красный,
# #ff7d00 – оранжевый,
# #ffff00 – желтый,
# #00ff00 – зеленый,
# #007dff – голубой,
# #0000ff – синий,
# #7d00ff – фиолетовый.

from tkinter import *
root = Tk()
def InsertColor(event):
    txt = ent.get

ent = Entry(root, width=20)






root.mainloop()
