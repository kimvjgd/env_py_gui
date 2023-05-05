import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class KeyboardSreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.columnconfigure(0, weight=1)

        self.pw_entry = Entry(self)
        self.pw_entry.grid(row=0, column=0,sticky='NEWS')

        keyboard_part = Frame(self, bg='red')
        keyboard_part.grid(row=1, column=0, sticky="NEWS")

        keyboard_part.rowconfigure(0, weight=3)
        keyboard_part.rowconfigure(1, weight=3)
        keyboard_part.rowconfigure(2, weight=3)
        keyboard_part.rowconfigure(3, weight=3)
        keyboard_part.rowconfigure(4, weight=2)
        keyboard_part.columnconfigure(0, weight=1)

        # ~ 1 2 3 4 5 6 7 8 9 0 - = backspace
        # ` ! @ # $ % ^ & * ( ) _ + backspace
        first_line_frame = Frame(keyboard_part, bg='black')
        first_line_frame.grid(row=0,column=0, sticky='NEWS')
        # q w e r t y u i o p [ ] \
        # Q W E R T Y U I O P { } |
        second_line_frame = Frame(keyboard_part, bg='green')
        second_line_frame.grid(row=1,column=0, sticky='NEWS')
        # capslock a s d f g h j k l ; ' enter
        # capslock A S D F G H J K L : " enter
        third_line_frame = Frame(keyboard_part, bg = 'yellow')
        third_line_frame.grid(row=2,column=0, sticky='NEWS')
        # shift z x c v b n m , . / shift
        # shift Z X C V B N M < > ? shift
        fourth_line_frame = Frame(keyboard_part, bg='blue')
        fourth_line_frame.grid(row=3,column=0, sticky='NEWS')
        # Back spacebar 입력
        fifth_line_frame = Frame(keyboard_part, bg='cyan')
        fifth_line_frame.grid(row=4,column=0, sticky='NEWS')

        # ~ 1 2 3 4 5 6 7 8 9 0 - = backspace
        # ` ! @ # $ % ^ & * ( ) _ + backspace
        first_line_frame.columnconfigure(0, weight=1)              # `             ~      
        first_line_frame.columnconfigure(1, weight=1)              # 1             !           
        first_line_frame.columnconfigure(2, weight=1)              # 2             @          
        first_line_frame.columnconfigure(3, weight=1)              # 3             #         
        first_line_frame.columnconfigure(4, weight=1)              # 4             $        
        first_line_frame.columnconfigure(5, weight=1)              # 5             %       
        first_line_frame.columnconfigure(6, weight=1)              # 6             ^      
        first_line_frame.columnconfigure(7, weight=1)              # 7             &     
        first_line_frame.columnconfigure(8, weight=1)              # 8             *    
        first_line_frame.columnconfigure(9, weight=1)              # 9             (   
        first_line_frame.columnconfigure(10, weight=1)             # 0             )  
        first_line_frame.columnconfigure(11, weight=1)             # -             _  
        first_line_frame.columnconfigure(12, weight=1)             # =             + 
        first_line_frame.columnconfigure(13, weight=2)             # backspace     backspace
        first_line_frame.rowconfigure(0, weight=1)

        # q w e r t y u i o p [ ] \
        # Q W E R T Y U I O P { } |
        second_line_frame.columnconfigure(0, weight=1)             # 공백
        second_line_frame.columnconfigure(1, weight=1)             # q            Q
        second_line_frame.columnconfigure(2, weight=1)             # w            W
        second_line_frame.columnconfigure(3, weight=1)             # e            E
        second_line_frame.columnconfigure(4, weight=1)             # r            R
        second_line_frame.columnconfigure(5, weight=1)             # t            T
        second_line_frame.columnconfigure(6, weight=1)             # y            Y
        second_line_frame.columnconfigure(7, weight=1)             # u            U
        second_line_frame.columnconfigure(8, weight=1)             # i            I
        second_line_frame.columnconfigure(9, weight=1)             # o            O
        second_line_frame.columnconfigure(10, weight=1)            # p            P
        second_line_frame.columnconfigure(11, weight=1)            # [            {
        second_line_frame.columnconfigure(12, weight=1)            # ]            }
        second_line_frame.columnconfigure(13, weight=2)            # \            |
        second_line_frame.rowconfigure(0, weight=1)
        

        # capslock a s d f g h j k l ; ' enter
        # capslock A S D F G H J K L : " enter
        third_line_frame.columnconfigure(0, weight=3)              # capslock      capsloc
        third_line_frame.columnconfigure(1, weight=2)              # a             A
        third_line_frame.columnconfigure(2, weight=2)              # s             S
        third_line_frame.columnconfigure(3, weight=2)              # d             D
        third_line_frame.columnconfigure(4, weight=2)              # f             F
        third_line_frame.columnconfigure(5, weight=2)              # g             G
        third_line_frame.columnconfigure(6, weight=2)              # h             H
        third_line_frame.columnconfigure(7, weight=2)              # j             J
        third_line_frame.columnconfigure(8, weight=2)              # k             K
        third_line_frame.columnconfigure(9, weight=2)              # l             L
        third_line_frame.columnconfigure(10, weight=2)             # ;             :
        third_line_frame.columnconfigure(11, weight=2)             # '             "
        third_line_frame.columnconfigure(12, weight=5)             # enter         enter
        third_line_frame.rowconfigure(0, weight=1)

        # shift z x c v b n m , . / shift
        # shift Z X C V B N M < > ? shift
        fourth_line_frame.columnconfigure(0, weight=2)
        fourth_line_frame.columnconfigure(1, weight=1)
        fourth_line_frame.columnconfigure(2, weight=1)
        fourth_line_frame.columnconfigure(3, weight=1)
        fourth_line_frame.columnconfigure(4, weight=1)
        fourth_line_frame.columnconfigure(5, weight=1)
        fourth_line_frame.columnconfigure(6, weight=1)
        fourth_line_frame.columnconfigure(7, weight=1)
        fourth_line_frame.columnconfigure(8, weight=1)
        fourth_line_frame.columnconfigure(9, weight=1)
        fourth_line_frame.columnconfigure(10, weight=1)
        fourth_line_frame.columnconfigure(11, weight=3)
        fourth_line_frame.rowconfigure(0, weight=1)


        # Back spacebar 입력
        fifth_line_frame.columnconfigure(0, weight=1)
        fifth_line_frame.columnconfigure(1, weight=5)
        fifth_line_frame.columnconfigure(2, weight=2)
        fifth_line_frame.rowconfigure(0, weight=1)

        

        # first_line_frame
        self.Btn(first_line_frame, 0, 0, '~')
        self.Btn(first_line_frame, 0, 1, '1')
        self.Btn(first_line_frame, 0, 2, '2')
        self.Btn(first_line_frame, 0, 3, '3')
        self.Btn(first_line_frame, 0, 4, '4')
        self.Btn(first_line_frame, 0, 5, '5')
        self.Btn(first_line_frame, 0, 6, '6')
        self.Btn(first_line_frame, 0, 7, '7')
        self.Btn(first_line_frame, 0, 8, '8')
        self.Btn(first_line_frame, 0, 9, '9')
        self.Btn(first_line_frame, 0, 10, '0')
        self.Btn(first_line_frame, 0, 11, '-')
        self.Btn(first_line_frame, 0, 12, '=')
        self.Btn(first_line_frame, 0, 13, '<-Del')

        # Btn_wave = Button(first_line_frame, text='~',font=('Arial', 10),bg='black', fg='white')
        # Btn_wave.grid(row=0, column=0, sticky='NEWS')
        # Btn_1 = Button(first_line_frame, text='1', font=('Arial', 10), bg='black', fg='white')
        # Btn_1.grid(row=0, column=1, sticky='NEWS')
        # Btn_2 = Button(first_line_frame, text='2', font=('Arial', 10), bg='black', fg='white')
        # Btn_2.grid(row=0, column=2, sticky='NEWS')
        # Btn_3 = Button(first_line_frame, text='3', font=('Arial', 10), bg='black', fg='white')
        # Btn_3.grid(row=0, column=3, sticky='NEWS')
        # Btn_4 = Button(first_line_frame, text='4', font=('Arial', 10), bg='black', fg='white')
        # Btn_4.grid(row=0, column=4, sticky='NEWS')
        # Btn_5 = Button(first_line_frame, text='5', font=('Arial', 10), bg='black', fg='white')
        # Btn_5.grid(row=0, column=5, sticky='NEWS')
        # Btn_6 = Button(first_line_frame, text='6', font=('Arial', 10), bg='black', fg='white')
        # Btn_6.grid(row=0, column=6, sticky='NEWS')
        # Btn_7 = Button(first_line_frame, text='7', font=('Arial', 10), bg='black', fg='white')
        # Btn_7.grid(row=0, column=7, sticky='NEWS')
        # Btn_8 = Button(first_line_frame, text='8', font=('Arial', 10), bg='black', fg='white')
        # Btn_8.grid(row=0, column=8, sticky='NEWS')
        # Btn_9 = Button(first_line_frame, text='9', font=('Arial', 10), bg='black', fg='white')
        # Btn_9.grid(row=0, column=9, sticky='NEWS')
        # Btn_0 = Button(first_line_frame, text='0', font=('Arial', 10), bg='black', fg='white')
        # Btn_0.grid(row=0, column=10, sticky='NEWS')
        # Btn_Minus = Button(first_line_frame, text='-', font=('Arial', 10), bg='black', fg='white')
        # Btn_Minus.grid(row=0, column=11, sticky='NEWS')
        # Btn_equal= Button(first_line_frame, text='=', font=('Arial', 10), bg='black', fg='white')
        # Btn_equal.grid(row=0, column=12, sticky='NEWS')
        # Btn_Backspace = Button(first_line_frame, text='<-del', font=('Arial', 10), bg='black', fg='white')
        # Btn_Backspace.grid(row=0, column=13, sticky='NEWS')

        # second_line_frame
        
        self.Btn(second_line_frame, 0, 0, '')
        self.Btn(second_line_frame, 0, 1, 'q')
        self.Btn(second_line_frame, 0, 2, 'w')
        self.Btn(second_line_frame, 0, 3, 'e')
        self.Btn(second_line_frame, 0, 4, 'r')
        self.Btn(second_line_frame, 0, 5, 't')
        self.Btn(second_line_frame, 0, 6, 'y')
        self.Btn(second_line_frame, 0, 7, 'u')
        self.Btn(second_line_frame, 0, 8, 'i')
        self.Btn(second_line_frame, 0, 9, 'o')
        self.Btn(second_line_frame, 0, 10, 'p')
        self.Btn(second_line_frame, 0, 11, '[')
        self.Btn(second_line_frame, 0, 12, ']')
        self.Btn(second_line_frame, 0, 13, '\\')
        # Btn_empty = Button(second_line_frame, text='', font=('Arial',10), bg='black', fg='white')
        # Btn_empty.grid(row=0, column=0, sticky='NEWS')
        # Btn_Q = Button(second_line_frame, text='q', font=('Arial',10), bg='black', fg='white')
        # Btn_Q.grid(row=0, column=1, sticky='NEWS')
        # Btn_W = Button(second_line_frame, text='w', font=('Arial',10), bg='black', fg='white')
        # Btn_W.grid(row=0, column=2, sticky='NEWS')
        # Btn_E = Button(second_line_frame, text='e', font=('Arial',10), bg='black', fg='white')
        # Btn_E.grid(row=0, column=3, sticky='NEWS')
        # Btn_R = Button(second_line_frame, text='r', font=('Arial',10), bg='black', fg='white')
        # Btn_R.grid(row=0, column=4, sticky='NEWS')
        # Btn_T = Button(second_line_frame, text='t', font=('Arial',10), bg='black', fg='white')
        # Btn_T.grid(row=0, column=5, sticky='NEWS')
        # Btn_Y = Button(second_line_frame, text='y', font=('Arial',10), bg='black', fg='white')
        # Btn_Y.grid(row=0, column=6, sticky='NEWS')
        # Btn_U = Button(second_line_frame, text='u', font=('Arial',10), bg='black', fg='white')
        # Btn_U.grid(row=0, column=7, sticky='NEWS')
        # Btn_I = Button(second_line_frame, text='i', font=('Arial',10), bg='black', fg='white')
        # Btn_I.grid(row=0, column=8, sticky='NEWS')
        # Btn_O = Button(second_line_frame, text='o', font=('Arial',10), bg='black', fg='white')
        # Btn_O.grid(row=0, column=9, sticky='NEWS')
        # Btn_P = Button(second_line_frame, text='p', font=('Arial',10), bg='black', fg='white')
        # Btn_P.grid(row=0, column=10, sticky='NEWS')
        # Btn_l_bra = Button(second_line_frame, text='[', font=('Arial', 10), bg='black', fg='white')
        # Btn_l_bra.grid(row=0, column=11, sticky='NEWS')
        # Btn_r_bra = Button(second_line_frame, text=']', font=('Arial', 10), bg='black', fg='white')
        # Btn_r_bra.grid(row=0, column=12, sticky='NEWS')
        # Btn_won = Button(second_line_frame, text='\\', font=('Arial',10), bg='black', fg='white')
        # Btn_won.grid(row=0, column=13, sticky='NEWS')

        # third_line_frame
        self.Btn(third_line_frame, 0, 0, 'capslock')
        self.Btn(third_line_frame, 0, 1, 'a')
        self.Btn(third_line_frame, 0, 2, 's')
        self.Btn(third_line_frame, 0, 3, 'd')
        self.Btn(third_line_frame, 0, 4, 'f')
        self.Btn(third_line_frame, 0, 5, 'g')
        self.Btn(third_line_frame, 0, 6, 'h')
        self.Btn(third_line_frame, 0, 7, 'j')
        self.Btn(third_line_frame, 0, 8, 'k')
        self.Btn(third_line_frame, 0, 9, 'l')
        self.Btn(third_line_frame, 0, 10, ';')
        self.Btn(third_line_frame, 0, 11, "'")
        self.Btn(third_line_frame, 0, 12, 'Enter')
        # Btn_capslock = Button(third_line_frame, text='capslock', font=('Arial',10), bg='black', fg='white')
        # Btn_capslock.grid(row=0, column=0, sticky='NEWS')
        # Btn_A = Button(third_line_frame, text='a', font=('Arial', 10), bg='black', fg='white')
        # Btn_A.grid(row=0, column=1, sticky='NEWS')
        # Btn_S = Button(third_line_frame, text='s', font=('Arial', 10), bg='black', fg='white')
        # Btn_S.grid(row=0, column=2, sticky='NEWS')
        # Btn_D = Button(third_line_frame, text='d', font=('Arial', 10), bg='black', fg='white')
        # Btn_D.grid(row=0, column=3, sticky='NEWS')
        # Btn_F = Button(third_line_frame, text='f', font=('Arial', 10), bg='black', fg='white')
        # Btn_F.grid(row=0, column=4, sticky='NEWS')
        # Btn_G = Button(third_line_frame, text='g', font=('Arial', 10), bg='black', fg='white')
        # Btn_G.grid(row=0, column=5, sticky='NEWS')
        # Btn_H = Button(third_line_frame, text='h', font=('Arial', 10), bg='black', fg='white')
        # Btn_H.grid(row=0, column=6, sticky='NEWS')
        # Btn_J = Button(third_line_frame, text='j', font=('Arial', 10), bg='black', fg='white')
        # Btn_J.grid(row=0, column=7, sticky='NEWS')
        # Btn_K = Button(third_line_frame, text='k', font=('Arial', 10), bg='black', fg='white')
        # Btn_K.grid(row=0, column=8, sticky='NEWS')
        # Btn_L = Button(third_line_frame, text='l', font=('Arial', 10), bg='black', fg='white')
        # Btn_L.grid(row=0, column=9, sticky='NEWS')
        # Btn_semi_col = Button(third_line_frame,text=';', font=('Arial',10), bg='black', fg='white')
        # Btn_semi_col.grid(row=0, column=10, sticky='NEWS')
        # Btn_apo = Button(third_line_frame,text='\'', font=('Arial',10), bg='black', fg='white')
        # Btn_apo.grid(row=0, column=11, sticky='NEWS')
        # Btn_enter = Button(third_line_frame, text='Enter', font=('Arial', 10), bg='black', fg='white')
        # Btn_enter.grid(row=0, column=12, sticky='NEWS')

        # fourth_line_frame
        self.Btn(fourth_line_frame, 0, 0, 'shift')
        self.Btn(fourth_line_frame, 0, 1, 'z')
        self.Btn(fourth_line_frame, 0, 2, 'x')
        self.Btn(fourth_line_frame, 0, 3, 'c')
        self.Btn(fourth_line_frame, 0, 4, 'v')
        self.Btn(fourth_line_frame, 0, 5, 'b')
        self.Btn(fourth_line_frame, 0, 6, 'n')
        self.Btn(fourth_line_frame, 0, 7, 'm')
        self.Btn(fourth_line_frame, 0, 8, ',')
        self.Btn(fourth_line_frame, 0, 9, '.')
        self.Btn(fourth_line_frame, 0, 10, '/')
        self.Btn(fourth_line_frame, 0, 11, 'shift')
        

        # Btn_l_shift = Button(fourth_line_frame, text='shitt', font=('Arial',10), bg='black', fg='white')
        # Btn_l_shift.grid(row=0, column=0, sticky='NEWS')
        # Btn_Z = Button(fourth_line_frame, text='z', font=('Arial',10), bg='black', fg='white')
        # Btn_Z.grid(row=0, column=1, sticky='NEWS')
        # Btn_X = Button(fourth_line_frame, text='x', font=('Arial',10), bg='black', fg='white')
        # Btn_X.grid(row=0, column=2, sticky='NEWS')
        # Btn_C = Button(fourth_line_frame, text='c', font=('Arial',10), bg='black', fg='white')
        # Btn_C.grid(row=0, column=3, sticky='NEWS')
        # Btn_V = Button(fourth_line_frame, text='v', font=('Arial',10), bg='black', fg='white')
        # Btn_V.grid(row=0, column=4, sticky='NEWS')
        # Btn_B = Button(fourth_line_frame, text='b', font=('Arial',10), bg='black', fg='white')
        # Btn_B.grid(row=0, column=5, sticky='NEWS')
        # Btn_N = Button(fourth_line_frame, text='n', font=('Arial',10), bg='black', fg='white')
        # Btn_N.grid(row=0, column=6, sticky='NEWS')
        # Btn_M = Button(fourth_line_frame, text='m', font=('Arial',10), bg='black', fg='white')
        # Btn_M.grid(row=0, column=7, sticky='NEWS')
        # Btn_comma = Button(fourth_line_frame,text=',', font=('Arial',10), bg='black', fg='white')
        # Btn_comma.grid(row=0, column=8, sticky='NEWS')
        # Btn_period = Button(fourth_line_frame,text='.', font=('Arial',10), bg='black', fg='white')
        # Btn_period.grid(row=0, column=9, sticky='NEWS')
        # Btn_slash = Button(fourth_line_frame,text='/', font=('Arial',10), bg='black', fg='white')
        # Btn_slash.grid(row=0, column=10, sticky='NEWS')
        # Btn_r_shift = Button(fourth_line_frame, text='shitt', font=('Arial',10), bg='black', fg='white')
        # Btn_r_shift.grid(row=0, column=11, sticky='NEWS')


        # fifth_line_frame
        self.Btn(fifth_line_frame, 0, 0, '')
        self.Btn(fifth_line_frame, 0, 1, 'space bar')
        self.Btn(fifth_line_frame, 0, 2, 'Connect')
        
        # Btn_fif_empty = Label(fifth_line_frame, bg='black')
        # Btn_fif_empty.grid(row=0, column=0, sticky='NEWS')
        # Btn_spacebar = Button(fifth_line_frame, text='space bar', font=('Arial',10), bg='black', fg='white')
        # Btn_spacebar.grid(row=0, column=1, sticky='NEWS')
        # Btn_connect = Button(fifth_line_frame, text='Connect', font=('Arial', 15), bg='black', fg='white')
        # Btn_connect.grid(row=0, column=2, sticky='NEWS')
    
    def Btn(self, frame, row, column, content, cmd):
        Button(frame, text=content, font=('Arial', 10), fg='white', bg='black', command=lambda: self.Btn_click(content)).grid(row=row, column=column, sticky='NEWS')


    def Btn_click(self, alphabet):
        current = self.pw_entry.get()
        self.pw_entry.delete(0, END)
        self.pw_entry.insert(0, str(current)+str(alphabet))
