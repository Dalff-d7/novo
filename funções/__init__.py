
# self.botão= tik.Button(self.fra3, text= text_btn, pady= 15,width=5, padx= 2,
#                                         font=('Times New Roman', '13'), command= self.limpar)
#                 self.botão.grid(row= pos, column=pos2, sticky= tik.NSEW,padx= 1, pady= 1)
#                 self.lista2.append(self.botão)

from tkinter import scrolledtext, Y, END,  WORD, Menubutton, Menu, Radiobutton, TOP,BOTTOM, RIGHT, LEFT, Button, NSEW
import sqlite3 as sq3

def botões(widget_pai, função):
    import tkinter as tik
    botões= [['1','2','3','DEL','CL',],
              ['4','5','6','+','-'],
              ['7','8','9','/','*'],
              ['(',')','0','.','=']]
    lista=[]
    for pos, linha in enumerate(botões):
        lista2=[]
        for pos2, coluna in enumerate(botões[pos]):
            text_btn= botões[pos][pos2]
            botão= tik.Button(widget_pai, text= text_btn, pady= 15,width=5, padx= 2,
                                         font=('Times New Roman', '13'), command=lambda t= coluna: função(t))
            botão.grid(row= pos, column=pos2, sticky= tik.NSEW,padx= 1, pady= 1)
            botão.config(relief= 'flat', bg= '#E8E0D7', highlightcolor= '#EAE4DE' )
            if text_btn== botões[3][4]:
                botão['bg']= '#1DAC0A'
            if text_btn== botões[0][3]:
                botão['bg']= '#EC0E0E'
            if text_btn== botões[0][4]:
                botão['fg']= '#e63900'
            lista2.append(botão)
        lista.append(lista2)
    return lista


def money_btn(widget_pai, func=0):
    botões= [['1','2','3','DEL','CL',],
              ['4','5','6','+','-'],
              ['7','8','9','/','↓↑'],
              ['(',')','0','.','=']]
    for pos, linha in enumerate(botões):
        for pos2, coluna in enumerate(botões[pos]):
            text_btn= botões[pos][pos2]
            btn= Button(widget_pai, text= text_btn, command= lambda t= coluna: func(t))
            btn.config(width= 6, pady=7, padx=3, height= 2,
                       font=('Times New Roman Bold', '10'),highlightthickness= 1, relief='flat',
                       bg= '#EBEBEB', highlightcolor= '#EAE4DE')
            btn.grid(row= pos, column=pos2, sticky= NSEW, pady=1, padx=1 )
            if text_btn == botões[3][4]:
                btn['fg']='#00cc00'
            elif text_btn == botões[2][4]:
                btn['fg']= '#00cc00'
            elif text_btn == botões[1][4]:
                btn['fg']= '#00cc00'
            elif text_btn == botões[0][4]:
                btn['fg']= '#e63900'
            elif text_btn == botões[0][3]:
                btn['fg']= '#00cc00'

def especial_btn(widget_pai, função=0):
    import tkinter as tik
    Sbtn= ['√', 'tan', '1', '2', '3', 'DEL', 'CL',
           'log', 'sin', '4', '5', '6', '/', '*',
           'cos','!', '7', '8', '9', '-', '+',
           '(', ')', '.', '0', ',', '^', '=']

    col_value=0
    row_value=1
    for text_btn in Sbtn:
        botão= tik.Button(widget_pai, text= text_btn, pady= 12, padx= 2, width= 4,
                          command= lambda t= text_btn: função(t), font=('Times New Roman', '15'), highlightthickness= 1)
        botão.grid(row= row_value, column= col_value, sticky= tik.NSEW, pady= 1, padx= 1)
        botão.config(relief= 'flat', bg= '#E8E0D7', highlightcolor= '#EAE4DE')
        col_value+=1
        if col_value >=7:
            col_value=0
            row_value+=1
        if text_btn == Sbtn[5]:
            botão['bg']= '#EC0E0E'
        if text_btn == Sbtn[6]:
            botão['fg']= '#EC7B0A'
        if text_btn == Sbtn[-1]:
            botão['bg']= '#1DAC0A'


def memory(widget_pai):
    scro= scrolledtext.ScrolledText(widget_pai, wrap= WORD, relief= 'flat')
    scro.pack(expand= True, fill= Y)

    data_base= sq3.connect(r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\armazenamento')
    cursor= data_base.cursor()

    cursor.execute("SELECT informação FROM store")
    result= cursor.fetchall()
    for rel in result:
        for rel2 in rel:
            scro.insert(END, rel2 +'\n')
            scro.see(END)


    # for txt in text:
    #     for tx in txt:
    #         scro.insert(END, tx +'\n')
            # scro.see(END)= este método permite que o usuário
            # visualize sempre a última informação que foi adi-
            # cionada.

def memory2(text):
    data_base= sq3.connect(r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\armazenamento')
    cursor= data_base.cursor()
    valor= f'{text}'
    inserção= "INSERT INTO store VALUES('"+valor+"')"
    cursor.execute(inserção)
    data_base.commit()


def delete_info():
    data_base= sq3.connect(r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\armazenamento')
    cursor= data_base.cursor()

    delete= 'DELETE FROM store'
    cursor.execute(delete)
    data_base.commit()


















