

# import tkinter
# import tkinter as tk
# from tkinter import *
# print (f'Версия TkInter :{TkVersion}')


# Чтобы написать GUI-программу, надо выполнить приблизительно следующее:
    # Создать главное окно.
    # Создать виджеты и выполнить конфигурацию их свойств (опций).
    # Определить события, то есть то, на что будет реагировать программа.
    # Описать обработчики событий, то есть то, как будет реагировать программа.
    # Расположить виджеты в главном окне.
    # Запустить цикл обработки событий.


# <---- Пример 1

# from tkinter import *
# print (f'Версия TkInter :{TkVersion}')
# root = Tk()

# def str_to_sort_list(event):
#     s = ent.get()
#     s = s.split()
#     s.sort()
#     lab['text'] = ' '.join(s)


# ent = Entry(root, width=20)
# but = Button(root, text="Преобразовать")
# lab = Label(root, width=20, 
#             bg='black', fg='white')


# ent = Entry(width=20)
# but = Button(text="Преобразовать")
# lab = Label(width=20, 
#             bg='black', fg='white')


# but.bind('<Button-1>', str_to_sort_list)

# ent.pack()
# but.pack()
# lab.pack()

# root.mainloop()

# ---->


# <---- Пример 2

# from tkinter import *
# root = Tk()

# class Block:
#     def __init__(self, master):
#         self.ent = Entry(master, width=20 )
#         self.but = Button(master, 
#                           text="Преобразовать")
#         self.lab = Label(master, width=20, 
#                          bg='black', fg='white')
#         self.but['command'] = self.str_to_sort

#         self.ent.pack()
#         self.but.pack()
#         self.lab.pack()
 
#     def str_to_sort(self):
#         s = self.ent.get()
#         s = s.split()
#         s.sort()
#         self.lab['text'] = ' '.join(s)

# first_block = Block(root)

# root.mainloop()

# ---->

# <---- Пример 3

# from tkinter import *
 
 
# class Block:
#     def __init__(self, master, func):
#         self.ent = Entry(master, width=20)
#         self.but = Button(master,
#                           text="Преобразовать")
#         self.lab = Label(master, width=20,
#                          bg='black', fg='white')
#         self.but['command'] = getattr(self, func)
#         self.ent.pack()
#         self.but.pack()
#         self.lab.pack()
 
#     def str_to_sort(self):
#         s = self.ent.get()
#         s = s.split()
#         s.sort()
#         self.lab['text'] = ' '.join(s)
 
#     def str_reverse(self):
#         s = self.ent.get()
#         s = s.split()
#         s.reverse()
#         self.lab['text'] = ' '.join(s)
 
 
# root = Tk()
 
# first_block = Block(root, 'str_to_sort')
# second_block = Block(root, 'str_reverse')
 
# root.mainloop()

# ---->


# Напишите простейший калькулятор, состоящий из двух текстовых полей,
# куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/".
# Результат вычисления должен отображаться в метке.
# Если арифметическоедействие выполнить невозможно (например, если были введены буквы, а не числа),
# то в метке должно появляться слово "ошибка".


# <---- 1 решение

from tkinter import *

root = Tk()

def Add(event):
    try:
        result = float(ent1.get()) + float(ent2.get())
        lab['text'] = result
    except ValueError:
        lab['text'] = 'Введите корректные числа'
def Decrement(event):
    try:
        result = float(ent1.get()) - float(ent2.get())
        lab['text'] = result
    except ValueError:
        lab['text'] = 'Введите корректные числа'

def Multiply(event):
    try:
        result = float(ent1.get()) * float(ent2.get())
        lab['text'] = result
    except ValueError:
        lab['text'] = 'Введите корректные числа'
def Divide(event):
    try:
        result = float(ent1.get()) / float(ent2.get())
        lab['text'] = result
    except ValueError:
        lab['text'] = 'Введите корректные числа'



ent1 = Entry(root, width=20)
ent2 = Entry(root, width=20)
but1 = Button(text="+", width=30)
but2 = Button(text="-", width=30)
but3 = Button(text="*", width=30)
but4 = Button(text="/", width=30)
lab = Label(width=50, 
            bg='black', fg='white')


but1.bind('<Button-1>', Add)
but2.bind('<Button-1>', Decrement)
but3.bind('<Button-1>', Multiply)
but4.bind('<Button-1>', Divide)

ent1.pack()
ent2.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
lab.pack()

root.mainloop()

# ---->