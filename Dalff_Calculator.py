# criando uma calculadora.

from funções import memory, memory2, delete_info, money_btn
import tkinter as tik
import re
from math import sqrt, pow, log, sin,tan, cos, factorial, radians, sinh
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
import json


window= tik.Tk()

class tela2:
    global resposta
    resposta=''
    def __init__(self, master, root):
        import funções as fun
        i_image= Image.open(r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/1605815.png')
        i_photo= ImageTk.PhotoImage(i_image)
        self.ourwindow= root
        self.new_window= master
        self.new_window.title('Dalff Scientific Calculator')
        self.new_window.geometry('410x339')
        self.new_window.iconphoto(False, i_photo)
        self.new_window.resizable(width= False, height= False)


        # criando os frames da jenela 2.
        self.fra1= tik.Frame(self.new_window, bg= 'white', width= 430, height= 70)
        self.fra2= tik.Frame(self.new_window, width= 430, height= 250, bg= 'white')
        self.fra3= tik.Frame(self.new_window, width= 412, height= 20, bg= 'white')
        self.fra4= tik.Frame(self.new_window, width= 408, height= 25, bg= '#E8E0D7')
        self.fra1.pack()
        self.fra3.pack()
        self.fra2.pack()
        self.fra4.pack(side= tik.BOTTOM)

        # criando os botões do Frame 4
        # inserção de imagens nos botões.
        self.imagem2= tik.PhotoImage(file=r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/3884295.png')
        self.imagem2= self.imagem2.subsample(17,29)

        self.btn= tik.Button(self.fra4, text= '= ∕ + x - %', command=self.back, relief= 'flat', bg= 'white', bd=1,
                             highlightthickness= 1, font= ('Copperplate Gothic Bold', '9'))
        self.btn.place(x= 3, y= 2)
        self.btn2= tik.Button(self.fra4, image= self.imagem2, command= self.memória, relief= 'flat', bg= 'white', bd=1,
                              highlightthickness= 1)
        self.btn2.place(x= 120, y= 2)
        self.btm= tik.Button(self.fra4, text= '$', command= self.open2, font=('Times New Roman Bold', '11'), width= 6,
                             relief= 'flat',bg= 'white')
        self.btm.place(x= 200, y= 1)


        # criando os componentes do frame 1
        self.entrada= tik.Entry(self.fra1, font=('Times New Roman', '25'), relief= 'flat', width= 24,
                                 justify= tik.RIGHT)
        self.entrada.bind('<Return>', self.enter)
        self.entrada.bind('<Key>', self.limpa_cal2)
        self.entrada.bind('<Key>', self.block_letters)
        self.entrada.pack()
        self.entrada.focus_set()
        # criando os componetes do frame 2
        self.btn= fun.especial_btn(self.fra2, self.command_principal)

        # criando componentes do frame 3
        self.lbl= tik.Label(self.fra3, text='', width= 26, bg= 'white')
        self.lbl.place(x= 223, y= 1)




        # criando as funções para a janela 2.
    def block_letters(self, event):
        if event.char.isalpha():
            return 'break'
        self.limpa_cal2(event)

    def open2(self):
        self.new_window.withdraw()
        self.janela4= tik.Toplevel(self.new_window)
        tela4(self.janela4, self.ourwindow)

    def back(self):
        self.ourwindow.deiconify()
        self.new_window.destroy()

    def command_principal(self, valor):
        global resposta
        get_text= self.entrada.get()
        if valor== 'CL':
            self.clean()
            self.lbl['text']= ' '
        if valor== 'DEL':
            self.deletar()
        if valor in '123,456/*789-+().0^':
            self.limpa_cal()
            self.text_delete()
            self.entrada.insert(tik.END, valor)
        if valor== '√':
            self.limpa_cal()
            self.inserir('sqrt(')
        if valor == 'sin':
            self.limpa_cal()
            self.inserir('sin(')
        if valor== 'log':
            self.limpa_cal()
            self.inserir('log(')
            self.message()
        if valor== 'cos':
            self.limpa_cal()
            self.inserir('cos(')
        if valor == 'tan':
            self.limpa_cal()
            self.inserir('tan(')
        if valor== '!':
            try:
                self.inserir('!')
                fixed_text= self.entrada_corrida(get_text)
                result=self.fact(fixed_text)
                self.lbl['text']= f'{result:,}'.replace(',','.')
                resultado= f'{fixed_text} = {result}'
                memory2(resultado)
                resposta= result
            except ValueError:
                self.clean()
                self.inserir('Error, falta de valor')

        if valor== '=':
            fixed_text= self.entrada_corrida(self.zero_crol(get_text))
            seprate_equatin=self.div_equatins(self.zero_crol(fixed_text))
            try:
                if len(seprate_equatin)== 1:
                    result= eval(self.entrada_corrida(self.zero_crol(seprate_equatin[0])))
                    self.lbl['text']= f'{result:,}'.replace(',','.')
                    resultado= f'{fixed_text} = {result}'
                    memory2(resultado)
                    resposta= result



                    if 'sin' in seprate_equatin[0]:
                        self.convertor(fixed_text)
                    if 'tan' in seprate_equatin[0]:
                        self.convertor(fixed_text)
                    if 'cos' in seprate_equatin[0]:
                        self.convertor(fixed_text)


                else:
                    result= eval(self.entrada_corrida(self.zero_crol(seprate_equatin[0])))
                    for equation in seprate_equatin[1:]:
                        result= pow(int(result), int(eval(self.entrada_corrida(self.zero_crol(equation)))))

                        self.lbl['text']= f'{result:,}'.replace(',','.')
                        resultado= f'{fixed_text} = {result}'
                        memory2(resultado)
                        resposta=result




            except OverflowError:
                self.clean()
                self.inserir('Error grande combinação')
            except ZeroDivisionError:
                self.clean()
                self.inserir('Error divisão por zero')
            except NameError:
                self.clean()
                self.inserir('Error de Sitax')
            except Exception:
                self.clean()
                self.inserir('Conta iválida')

    def text_delete(self):
        if self.entrada.get() == 'Conta iválida':
            self.clean()
        elif self.entrada.get()== 'Error de Sitax':
            self.clean()
        elif self.entrada.get()== 'Error divisão por zero':
            self.clean()
        elif self.entrada.get()== 'Error grande combinação':
            self.clean()
        elif self.entrada.get()== 'Error, falta de valor':
            self.clean()

    def enter(self,event):
        self.command_principal('=')

    def limpa_cal(self):
        global resposta
        if resposta !='':
            self.clean()
            resposta=''

    def limpa_cal2(self, event):
        global resposta
        if resposta !='':
            self.clean()
            resposta=''
        if self.entrada.get() == 'Conta iválida':
            self.clean()
        elif self.entrada.get()== 'Error de Sitax':
            self.clean()
        elif self.entrada.get()== 'Error divisão por zero':
            self.clean()
        elif self.entrada.get()== 'Error grande combinação':
            self.clean()
        elif self.entrada.get()== 'Error, falta de valor':
            self.clean()



    def entrada_corrida(self, text):
        text= re.sub(r'([\*\+\/\-\^\.]?\(\))', r' ', text)
        text= re.sub(r'[^Error grande combinaçãoError divisão por zeroError\, falta de valorError de SitaxConta iválidatansincossqrtlog123\,456\/\*789\-\+\(\)\.0\^]', r'', text)
        text= re.sub(r'([\*\+\/\,\-\.\^])\1', r'\1', text)
        return text

    def zero_crol(self, text):
        text= re.sub(r'\b0+(\d0+)', r'\1', text)
        return text

    def clean(self):
        self.entrada.delete(0, tik.END)


    def inserir(self, text):
        self.entrada.insert(tik.END, text)

    def deletar(self):
        get_text= self.entrada.get()
        new_text= get_text[:-1]
        self.entrada.delete(0, tik.END)
        self.entrada.insert(tik.END, new_text)

    def div_equatins(self, text):
        return  re.split(r'\^', text)

    def fact(self, text):
        if text.isnumeric:
            text= int(text)
            cal= factorial(text)
            return  cal

    def message(self):
        messagebox.showinfo('ORIENTAÇÃO', '''Você acinou a opção para calcular o lagaritimo de um número então terá que primeiro fornecer o logaritimando depois a virgula e o por fim a base assim: "log(x,base)"''')

    def convertor(self, text):
        fixed_text, fixed_text2 = text.split('(')
        coversão= str(fixed_text2[:-1])
        calculo= eval(coversão)
        rad= radians(calculo)
        new_string= f'{fixed_text}({rad})'
        rel_covertido= eval(new_string)
        if rel_covertido < 0:
            rel_covertido= round(rel_covertido)
        self.lbl['text']= f'{rel_covertido:,}'.replace(',','.')
        return rel_covertido

    def memória(self):
       self.janela3= tik.Toplevel(self.new_window)
       tela3(self.janela3)


class tela:
    resposta=''
    def __init__(self, master):
        import funções as fun
        imagem_i= Image.open(r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/pngtree-cartoon-math-symbols-logo-psd-layered-image_2274516.jpg')
        photo_i= ImageTk.PhotoImage(imagem_i)
        self.ourwwindow= master
        self.ourwwindow.title(' ')
        self.ourwwindow.geometry('300x370')
        self.ourwwindow.iconphoto(False, photo_i)
        self.ourwwindow.resizable(width= False, height= False)


        # componetes da toplevel
        self.lebal= tik.Label(self.ourwwindow, text= 'Dalff  Calculator', font=('Bell MT', '12', 'bold'))
        self.lebal.pack()
        # crinado as frames
        self.fra1= tik.Frame(self.ourwwindow, width= 294, bg='white',height= 47)
        self.fra2= tik.Frame(self.ourwwindow, width= 294, bg='white', height= 20)
        self.fra3= tik.Frame(self.ourwwindow, width= 302, height= 270)
        self.fra4= tik.Frame(self.ourwwindow, width= 302, bg= '#E8E0D7', height= 23, pady= 0 )
        self.fra1.pack()
        self.fra2.pack()
        self.fra3.pack()
        self.fra4.pack(side= tik.BOTTOM)
        # criando os componentes da 1º frame.
        self.entr= tik.Entry(self.fra1, font=('Arial', '25'), relief= 'flat', width=16, justify= tik.RIGHT)
        self.entr.bind('<Return>', self.enter)
        self.entr.bind('<Key>', self.limpar_cal2)
        self.entr.bind('<Key>', self.block_letters)
        self.entr.place(x=0, y= 3)
        self.entr.focus_set()
        # crinado os componentes da 2º frame.
        self.lbl_anwser= tik.Label(self.fra2, text= ' ', font=('Times New Roman', '12'), width= 25, padx=1, bg='white')
        self.lbl_anwser.place(x= 105, y= 1)
        # crinado os componentes do 3º frame.
        self.btn= fun.botões(self.fra3, self.comand_principal)
        # criando os componentes do 4º frame
        # inserção de imagens nos botões
        self.b_image= tik.PhotoImage(file=r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/3884295.png')
        self.b_image= self.b_image.subsample(16,29)
        # criando o proprio botão
        self.btn2= tik.Button(self.fra4, text= 'f(x) √² !' ,command= self.open, relief='flat', font=('Copperplate Gothic Bold', '10'))
        self.btn2.place(x= 2, y=0)
        self.btn4= tik.Button( self.fra4, image=self.b_image, command= self.memória, relief='flat')
        self.btn4.place(x= 100, y=1)
        self.btm= tik.Button(self.fra4, text= '$', command= self.open2, font=('Times New Roman', '11', 'bold'), width= 5,
                             relief= 'flat')
        self.btm.place(x= 178, y=0)

    # criando as funções:

    def block_letters(self, event):
        if event.char in 'qwertyuiopasdfghjklçzxcvbnm':
            return 'break'
        self.limpar_cal2(event)


    def text_delete(self):
       if  self.entr.get() == 'ZeroDivision':
           self.delte()
       elif self.entr.get() == 'Sytaxerror':
           self.delte()

    def open2(self):
        self.ourwwindow.withdraw()
        self.janela4= tik.Toplevel(self.ourwwindow)
        tela4(self.janela4, self.ourwwindow)
    def open(self):
        self.ourwwindow.withdraw()
        self.janela2= tik.Toplevel(self.ourwwindow)
        tela2(self.janela2, self.ourwwindow)

    def comand_principal(self, valor):
        global resposta
        entrada=self.entr.get()
        if valor == 'CL':
            self.delte()
        if valor == 'DEL':
            new_text= entrada[:-1]
            self.entr.delete(0, tik.END)
            self.entr.insert(0, new_text)
        if valor in '1234567890*+-/^.()':
            self.limpar_cal()
            self.text_delete()
            self.entr.insert(tik.END, valor)

        if valor== '=':
            fixed_text= self.entrada_corrida(entrada)
            div_enquations= self.divis_equaç(fixed_text)
            try:
                if len(div_enquations)== 1:
                    result= eval(self.entrada_corrida(self.zero_crol(div_enquations[0])))
                    self.lbl_anwser['text']= f'{result:,}'.replace(',','.')
                    resultado= f'{fixed_text} = {result}'
                    memory2(resultado)
                    resposta= result






                else:
                    result= eval(self.entrada_corrida(div_enquations[0]))
                    for equation in div_enquations[1:]:
                        result= pow(result, eval(self.entrada_corrida(equation)))
                        self.lbl_anwser['text']= result
                        resultado= f'{fixed_text} = {result}'
                        memory2(resultado)


            except  ZeroDivisionError:
                self.entr.delete(0, tik.END)
                self.entr.config(font=('Arial', '25'), width= 16)
                self.entr.insert(tik.END, 'ZeroDivision')
            except Exception :
                self.entr.delete(0, tik.END)
                self.entr.config(font=('Arial', '25'), width= 16)
                self.entr.insert(tik.END, 'Sytaxerror')


    def enter(self, event):
        self.comand_principal('=')

    def limpar_cal(self):
        global resposta
        if resposta !='':
            self.entr.delete(0, tik.END)
            resposta=''

    def limpar_cal2(self, event):
        global resposta
        if resposta !='':
            self.entr.delete(0, tik.END)
            resposta=''
        self.text_delete()


    def entrada_corrida(self, text):
        text= re.sub(r'([\*\+\/\-\^\.]?\(\))', r' ', text)
        text= re.sub(r'[^\d\.\+\/\^\-\*\(\)eSytaxerrorZeroDivision0]', r' ', text)
        text= re.sub(r'([\.\+\*\^\/\-])\1', r'\1', text)
        return text

    def zero_crol(self, text):
        text= re.sub(r'\b0+(\d0+)', r'\1', text)
        #help me in this case 009+008> i wanto to just 
        # grab the numbers and ignore the zeros
        return text
        
        

    def divis_equaç(self, texto):
        return re.split(r'\^', texto)


    def delte(self):
        self.entr.delete(0 ,tik.END )
        self.lbl_anwser['text']= ' '

    def memória(self):
        self.janela3= tik.Toplevel(self.ourwwindow)
        tela3(self.janela3)
        # global result
        # self.janela3= tik.Toplevel(self.ourwwindow)
        # self.janela3.title('memoria')
        # memory(self.janela3, result )

class tela3(tela):
    def __init__(self, master):
        # inserindo as imagens
        i_image= Image.open(r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/3884295.png')
        i_photo= ImageTk.PhotoImage(i_image)
        self.new_window= master
        self.new_window.title('Memória')
        self.new_window.geometry('200x270')
        self.new_window['bg']= 'white'
        self.new_window.resizable(width= False, height= False)
        self.new_window.iconphoto(False, i_photo)
        self.btn= tik.Button(self.new_window, text= 'Delete History', command= self.close)
        self.btn.config(relief= 'raised', bg='green', fg= 'white', font=('Copperplate Gothic Bold', '10'))
        self.btn.pack(side= tik.BOTTOM)
        memory(self.new_window)


    def close(self):
        delete_info()
        self.new_window.destroy()

class tela4:
    global textx
    global textx2
    global imagem2
    global imagem1
    global amount
    textx= ''
    textx2= ''
    imagem1= ''
    imagem2= ''
    amount= ''
    def __init__(self, master,root):
        i_image= Image.open(r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/dollar-sign-business-cash-cashe-dollar-dollars-earn-earn-36.png')
        i_photo= ImageTk.PhotoImage(i_image)
        self.ourwindow= root
        self.money_window= master
        self.money_window.title('')
        self.money_window.geometry('294x398')
        self.money_window.iconphoto(False, i_photo)
        self.money_window.resizable(width= False, height= False)

        # criando os frames
        self.fra1= tik.Frame(self.money_window, bg= '#EBEBEB', width= 290 ,height= 65)
        self.fra2= tik.Frame(self.money_window, bg= '#EBEBEB', width= 290, height= 65)
        self.fra3= tik.Frame(self.money_window, bg= '#EBEBEB', width= 290, height= 235)
        self.fra4= tik.Frame(self.money_window, bg= '#4dff4d', width= 290, height= 3)
        self.fra5= tik.Frame(self.money_window,  width= 290, height= 5)
        self.fra7= tik.Frame(self.money_window, width= 290, height= 25, bg='#EBEBEB')
        self.fra5.pack(side= tik.TOP)
        self.fra1.pack()
        self.fra4.pack()
        self.fra2.pack()
        self.fra3.pack()
        self.fra7.pack()

        # criando o botão da frame 7
        self.btn= tik.Button(self.fra7, text= '= ∕ + x - %', command= self.main_page, font= ('Copperplate Gothic Bold', '9'),
                             relief= 'groove', bg= '#EBEBEB').place(x=1, y=2)
        # criando a label de informação
        self.lbl_info= tik.Label(self.fra5, text= 'Conversor de Moeda', relief= 'flat', width= 42, bg='#00cc00' )
        self.lbl_info.pack()
        # criando a entry

        self.entrada= tik.Entry(self.fra1, width= 13, justify= tik.RIGHT, relief= 'flat', bg='#EBEBEB', fg='grey', font=('Times New Roman Bold', '10'))
        self.entrada.insert(tik.END, '100,00')
        self.entrada.bind('<FocusIn>', self.cursor_dentro)
        self.entrada.bind('<FocusOut>', self.cursor_fora)
        self.entrada.bind('<Return>', self.enter)
        self.entrada.bind('<Key>', self.block_letters)
        self.entrada.place(x= 190, y=13)
        self.entrada.focus_set()

        # lista dos paises
        image_coins= {'USD' : r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748050_flag_usa.png',
                  'EUR': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748065_european_union_flag.png',
                      'MZN': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748127_flag_mozambique.png',
                      'CNY': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748006_flag_china.png',
                      'ZAR': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748060_africa_flag_south.png',
                      'AOA': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748089_flag_angola.png',
                      'NOK': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748131_norway_flag.png',
                      'PEN': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748122_peru_flag.png',
                      'AFN': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748077_afghanistan_flag.png',
                      'SAR': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748010_flag_saudi_arabia.png',
                      'BWP': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748080_botswana_flag.png',
                      'CAD': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748016_flag_canada.png',
                      'INR': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748132_india_flag.png',
                      'MXN': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748137_mexico_flag.png',
                      'GBP': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748029_england_flag.png',
                      'TZS': r'C:\Users\chadreque\PycharmProjects\Interfeces or GUI\photos/748053_flag_tanzania.png'}

        money_btn(self.fra3, self.func)

        # o primeiro menubutton
        self.main_menu= tik.Menubutton(self.fra1, text= 'Tap to Choose', font=('Latha','11', 'italic'), bg='#EBEBEB' )
        self.main_menu.place(x=1, y=7)
        self.inside_menu= tik.Menu(self.main_menu, tearoff=0)
        for key, value in image_coins.items():
            imagem= Image.open(value)
            flag= ImageTk.PhotoImage(imagem)
            self.inside_menu.add_radiobutton(label= key, compound= tik.LEFT,image= flag,
                                             command= lambda t= key, t2= flag: self.show(t, t2))
        self.main_menu['menu']= self.inside_menu

        # o segundo Menubutton
        self.main_menu2= tik.Menubutton(self.fra2, text='Tap to Choose', font=('Latha','11', 'italic'), bg='#EBEBEB')
        self.main_menu2.place(x=1, y=7)
        self.inside_menu2= tik.Menu(self.main_menu2, tearoff=0)
        for key, value in image_coins.items():
            imagem= Image.open(value)
            flag= ImageTk.PhotoImage(imagem)
            self.inside_menu2.add_radiobutton(label= key, compound= tik.LEFT,image= flag,
                                             command= lambda t= key, t2= flag: self.show2(t, t2))
        self.main_menu2['menu']= self.inside_menu2

        # crinado a label
        self.lbl= tik.Label(self.fra2, text= '0,00', width= 12, relief= 'flat', font=('Times New Roman Bold', '10'), justify= tik.RIGHT, bg='#EBEBEB', fg='grey',
                            anchor= tik.E)
        self.lbl.place(x=191, y=13)


    def show2(self, x,x2):
        global textx2
        global imagem2
        self.main_menu2.config(text= x, compound= tik.LEFT, image= x2)
        textx2= x
        imagem2= x2

    def show(self,x ,x2):
        global imagem1
        global textx
        self.main_menu.config(text= x, compound= tik.LEFT, image= x2)
        textx= x
        imagem1= x2

    def main_page(self):
        self.ourwindow.deiconify()
        self.money_window.destroy()

    def enter(self, event):
        self.func('=')

    def func(self, text):
        global textx
        global textx2
        global imagem1
        global imagem2
        global amount
         # pegando a informação da entry
        self.amount= self.entrada.get()
        fixed_text= self.correct(self.zero_crol(self.amount))
        amount= ''
        for fx_text in fixed_text:
            amount= fx_text
        if text in '1234567890':
            self.press_number(text)
            self.insert(text)

        if text =='DEL':
            new_text= self.amount[:-1]
            self.entrada.delete(0, tik.END)
            self.entrada.insert(tik.END, new_text)
        if text== 'CL':
            self.entrada.delete(0, tik.END)
            self.lbl.config(text= '0,00', font=('Times New Roman Bold', '10'), fg='grey')
        if text== '=':

            coin1= textx
            coin2= textx2
            api_key= 'ee3e91bf-7863c50e-d0487370-0fb72c9b'
            base_url= 'http://api.exconvert.com/convert'
            try:

                # calculando
                params = {
                            'access_key': f'{api_key}',
                                'from': f'{coin1}',
                                'to': f'{coin2}',
                                'amount': f'{amount}'
                            }


                api_result = requests.get(base_url, params)
                website_content = api_result.content
                rate= website_content.decode('utf-8')
                result= json.loads(rate)
                ref= result['result']
                price= ref['rate']
                duas_casas= f'{ref[coin2]:.2f}'
                vl_formatado= str(duas_casas).replace('.',',')
                self.lbl.config(text=f'{vl_formatado:s}', font=('Times New Roman Bold', '10'), fg='black')
                self.lbl_info.config(text= f'Preço do {coin1} é  {price:.2f}')
            except SyntaxError:
                self.lbl_info.config(text= 'Erro, Valor Incorrecto...')
            except Exception:
                self.lbl_info.config(text='Erro de conexão! Tente Novamente...', font=('Times New Roman Bold', '10'), fg= 'red')

        if text== '↓↑':
            moeda1,moeda2 = textx2, textx
            self.main_menu.config(text= moeda1, compound= tik.LEFT, image=imagem2 )
            self.main_menu2.config(text= moeda2, compound= tik.LEFT, image= imagem1)
            self.rate(moeda1, moeda2, amount)
    def block_letters(self, event):
        if event.char.isalpha():
            return 'break'
    def zero_crol(self, text):
        text= re.sub(r'\b0+(\d)',r'\1', text)
        return text


    def cursor_dentro(self, event):
        if self.entrada.get()== '100,00':
            self.entrada.delete(0, tik.END)
            self.entrada.config(fg='black')
    def cursor_fora(self, event):
        if not self.entrada.get():
            self.entrada.insert(tik.END, '100,00')
            self.entrada.config(fg='grey', font=('Times New Roman Bold', '10'))

    def press_number(self, event):
        self.cursor_dentro(event)

    def correct(self, text):
        text= re.findall(r'\d+', text)
        return text
    def insert(self, text):
        self.entrada.insert(tik.END, text)
    def rate(self, moeda, moeda1, amount):
        try:
            api_key= 'ee3e91bf-7863c50e-d0487370-0fb72c9b'
            base_url= 'http://api.exconvert.com/convert'
            # calculando
            params = {
                        'access_key': f'{api_key}',
                            'from': f'{moeda}',
                            'to': f'{moeda1}',
                            'amount': f'{amount}'
                        }

            api_result = requests.get(base_url, params)
            website_content = api_result.content
            rate= website_content.decode('utf-8')
            result= json.loads(rate)
            ref= result['result']
            price= ref['rate']
            duas_casas= f'{ref[moeda1]:.2f}'
            vl_formatado= str(duas_casas).replace('.',',')
            self.lbl.config(text=f'{vl_formatado:s}', font=('Times New Roman Bold', '10'), fg='black')
            self.lbl_info.config(text= f'Preço do {moeda} é {price:.2f}')
        except SyntaxError:
            self.lbl_info.config(text= 'Erro, Valor Incorrecto...')
        except Exception:
            self.lbl_info.config(text= 'Erro de conexão! Tente Novamente...', font=('Times New Roman Bold', '10'), fg= 'red')

janela= tela(window)
window.mainloop()

# fim do projecto.

