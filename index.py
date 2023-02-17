from tkinter import * #biblioteca de interface grafica
import math           #biblioteca de operação matematica
import tkinter.messagebox#biblioteca de interface grafica caixa de menssagem
janela_principal= Tk()  # a variavel janela_principal recebe a função tkinter 
janela_principal.title("Calculadora Cientifica")# objeto da variavel janela_principal recebe a função titulo
janela_principal.resizable(width=False, height=False)
janela_principal.geometry("480x568+450+90")# objeto da variavel janela_principal recebe a dimensoes da janela

calc = Frame(janela_principal)
calc.grid()
  
class Calc():
    def __init__(self):
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False
  
    def numberEnter(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)
  
    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())
  
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
  
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
  
    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False
  
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value=True
  
    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0
  
    def pi(self):
        self.result =  False
        self.current = math.pi
        self.display(self.current)
  
    def tau(self):
        self.result =  False
        self.current = math.tau
        self.display(self.current)
  
    def e(self):
        self.result =  False
        self.current = math.e
        self.display(self.current)
  
    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
  
    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
  
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
  
    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
  
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
  
    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
  
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
  
    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
  
    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)
  
    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)
  
    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)
  
    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)
  
    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)
  
    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)
  
    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)
  
    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)
  
    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)
  
    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)
  
added_value = Calc()
  
txtDisplay = Entry(calc, font=('Helvetica',20,'bold'),
                   bg='black',fg='white',
                   bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")
  
numero_tela = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2,
                          bg='black',fg='white',
                          font=('Helvetica',20,'bold'),
                          bd=4,text=numero_tela[i]))
        btn[i].grid(row=j, column= k, pady = 1)
        btn[i]["command"]=lambda x=numero_tela[i]:added_value.numberEnter(x)
        i+=1
        
botao_limpar = Button(calc, text=chr(67),width=6,
                  height=2,bg='blue',
                  font=('Helvetica',20,'bold')
                  ,bd=4, command=added_value.Clear_Entry
                 ).grid(row=1, column= 0, pady = 1)
  
botao_limpar_tudo = Button(calc, text=chr(67)+chr(69),
                     width=6, height=2,
                     bg='blue', 
                     font=('Helvetica',20,'bold'),
                     bd=4,
                     command=added_value.All_Clear_Entry
                    ).grid(row=1, column= 1, pady = 1)
  
botao_raiz = Button(calc, text="\u221A",width=6, height=2,
               bg='blue', font=('Helvetica',
                                       20,'bold'),
               bd=4,command=added_value.squared
              ).grid(row=1, column= 2, pady = 1)
  
botao_Adicao = Button(calc, text="+",width=6, height=2,
                bg='blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("add")
                ).grid(row=1, column= 3, pady = 1)
  
botao_Subtracao = Button(calc, text="-",width=6,
                height=2,bg='blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("sub")
                ).grid(row=2, column= 3, pady = 1)
  
botao_Multiplicacao = Button(calc, text="x",width=6, 
                height=2,bg='blue', 
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("multi")
                ).grid(row=3, column= 3, pady = 1)
  
botao_Divisao = Button(calc, text="/",width=6, 
                height=2,bg='blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("divide")
                ).grid(row=4, column= 3, pady = 1)
  
botao_Zero = Button(calc, text="0",width=6,
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=lambda:added_value.numberEnter(0)
                 ).grid(row=5, column= 0, pady = 1)
  
botao_Dot = Button(calc, text=".",width=6,
                height=2,bg='blue', 
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.numberEnter(".")
                ).grid(row=5, column= 1, pady = 1)
botao_PM = Button(calc, text=chr(177),width=6, 
               height=2,bg='blue', font=('Helvetica',20,'bold'),
               bd=4,command=added_value.mathPM
              ).grid(row=5, column= 2, pady = 1)
  
botao_resultado = Button(calc, text="=",width=6,
                   height=2,bg='blue',
                   font=('Helvetica',20,'bold'),
                   bd=4,command=added_value.sum_of_total
                  ).grid(row=5, column= 3, pady = 1)
# ROW 1 :
botao_Pi = Button(calc, text="pi",width=6,
               height=2,bg='red',fg='white', 
               font=('Helvetica',20,'bold'),
               bd=4,command=added_value.pi
              ).grid(row=1, column= 4, pady = 1)
  
botao_Cos = Button(calc, text="Cos",width=6, 
                height=2,bg='red',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.cos
               ).grid(row=1, column= 5, pady = 1)
  
botao_tang = Button(calc, text="tan",width=6, 
                height=2,bg='red',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.tan
               ).grid(row=1, column= 6, pady = 1)
  
botao_sen = Button(calc, text="sin",width=6,
                height=2,bg='red',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.sin
               ).grid(row=1, column= 7, pady = 1)
  
# ROW 2 :
botao_2xPi = Button(calc, text="2xpi",width=6, 
                height=2,bg='red',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.tau
               ).grid(row=2, column= 4, pady = 1)
  
botao_2xcos = Button(calc, text="2xCos",width=6,
                 height=2,bg='red',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.cosh
                ).grid(row=2, column= 5, pady = 1)
  
botao_2xtang = Button(calc, text="2xtan",width=6, 
                 height=2,bg='red',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.tanh
                ).grid(row=2, column= 6, pady = 1)
  
botao_2xsen = Button(calc, text="2xsin",width=6, 
                 height=2,bg='red',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.sinh
                ).grid(row=2, column= 7, pady = 1)
  
# ROW 3 :
botao_log = Button(calc, text="log",width=6,
                height=2,bg='red',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.log
               ).grid(row=3, column= 4, pady = 1)
  
botao_Exponencial = Button(calc, text="exp",width=6, height=2,
                bg='red',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.exp
               ).grid(row=3, column= 5, pady = 1)
  
botao_Mod = Button(calc, text="Mod",width=6,
                height=2,bg='red',fg='white', 
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("mod")
                ).grid(row=3, column= 6, pady = 1)
  
botao_E   = Button(calc, text="e",width=6, 
                height=2,bg='red',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.e
               ).grid(row=3, column= 7, pady = 1)
  
# ROW 4 :
botao_log10 = Button(calc, text="log10",width=6, 
                  height=2,bg='red',fg='white', 
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.log10
                 ).grid(row=4, column= 4, pady = 1)
  
botao_cos   = Button(calc, text="log1p",width=6,
                  height=2,bg='red',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.log1p
                 ).grid(row=4, column= 5, pady = 1)
  
botao_expm1 = Button(calc, text="expm1",width=6,
                  height=2,bg='red',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd = 4,command=added_value.expm1
                 ).grid(row=4, column= 6, pady = 1)
  
botao_gamma = Button(calc, text="gamma",width=6,
                  height=2,bg='red',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.lgamma
                 ).grid(row=4, column= 7, pady = 1)
# ROW 5 :
botao_log2 = Button(calc, text="log2",width=6, 
                 height=2,bg='red',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.log2
                ).grid(row=5, column= 4, pady = 1)
  
botao_deg = Button(calc, text="deg",width=6, 
                height=2,bg='red',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.degrees
               ).grid(row=5, column= 5, pady = 1)
  
botao_cosh = Button(calc, text="acosh",width=6,
                  height=2,bg='red',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.acosh
                 ).grid(row=5, column= 6, pady = 1)
  
botao_sinh = Button(calc, text="asinh",width=6, 
                  height=2,bg='red',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.asinh
                 ).grid(row=5, column= 7, pady = 1)
  
Display_cientifico= Label(calc, text = "Calculadora Cientifica",font=('Helvetica',30,'bold'),fg='black',justify=CENTER)
Display_cientifico.grid(row=0, column= 4,columnspan=4)
  
def sair():
    sair = tkinter.messagebox.askyesno("Calculadora Cientifica",
                                        "Deseja sair ?")
    if sair>0:
        janela_principal.destroy()
        return
  
def cientifico():
    janela_principal.resizable(width=False, height=False)
    janela_principal.geometry("944x568+0+0")
  
  
def padrao():
    janela_principal.resizable(width=False, height=False)
    janela_principal.geometry("480x568+0+0")
  
aba_menu= Menu(calc)
  
# Manu parte 1 :
menu_arquivo = Menu(calc, tearoff = 0)
aba_menu.add_cascade(label = 'Arquivo', menu = menu_arquivo)
menu_arquivo.add_command(label = "Cientifico", command = cientifico)
menu_arquivo.add_command(label = "Padrao", command = padrao)
menu_arquivo.add_separator()
menu_arquivo.add_command(label = "Sair", command = sair)
  
# Manu parte  2 :
menu_editar= Menu(calc, tearoff = 0)
aba_menu.add_cascade(label = 'Editar', menu = menu_editar)
menu_editar.add_command(label = "Recortar")
menu_editar.add_command(label = "Copia")
menu_editar.add_command(label = "Pasta")
menu_editar.add_command(label = "Sair", command = sair) 
menu_editar.add_separator()
  
janela_principal.config(menu=aba_menu)
janela_principal.mainloop()
