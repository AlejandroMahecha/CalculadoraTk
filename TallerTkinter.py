import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import messagebox
from tkinter import ttk
import random
import math


def cambiar_color():  #Funcion para cambiar el color de la interfaz, elije un color al azar (pantalla 0)
    colores = ["#F2AD1F", "#FC6E21", "#E62930", "#DD21FC", "#380DF5","#1FEFF2","#5821FC","#FCAE21","#92F500","#992502","#022EE6"]
    global colores_random
    colores_random = random.choice(colores)
    pestaña0.config(bg=colores_random)
    label.config(bg=colores_random)
    label_entrada1.config(bg=colores_random)
    label_entrada2.config(bg=colores_random)
    label_operador.config(bg=colores_random)
    label_resultado.config(bg=colores_random)
def cambio_color2(): #Funcion para cambiar el color de la interfaz, elije un color al azar (pantalla 1)
    colores = ["#F2AD1F", "#FC6E21", "#E62930", "#DD21FC", "#380DF5", "#1FEFF2", "#5821FC", "#FCAE21", "#92F500","#992502", "#022EE6"]
    global colores_random2
    colores_random2 = random.choice(colores)
    pestaña1.config(bg=colores_random2)
    label_1.config(bg=colores_random2)
    label_entrada1_1.config(bg=colores_random2)
    label_operador_1.config(bg=colores_random2)
    label_resultado_1.config(bg=colores_random2)

def init_window():
    contador667=0
    global window
    window=tk.Tk() #creamos la ventana
    window.iconbitmap("calculator.ico")
    window.config(cursor="dotbox")
    global notebook
    notebook=ttk.Notebook(window)
    notebook.pack(fill="both",expand="yes")
    global pestaña0
    global pestaña1
    pestaña0=tk.Frame(notebook)
    pestaña1=tk.Frame(notebook)
    notebook.add(pestaña0,text="Calculadora Básica")
    notebook.add(pestaña1, text="Calculadora Compleja")
    window.title("Calculadora 1.0") #agregamos el titulo
    window.geometry('450x250') #establecimos el ancho (400px) y el largo (250 px))

##############################################CALCULADORA BASICA#################################################
#Todas las funciones de este apartado son de la primera pestaña de la calculadora.
    global label
    label =tk.Label(pestaña0,text="Calculadora Básica",font=("Helvetica", 20, "bold italic"))
    label.grid(column=0,row=0)

    global label_entrada1
    label_entrada1=tk.Label(pestaña0,text="Ingrese su primer numero",font=("Arial bold",10))
    label_entrada1.grid(column=0,row=1)


    global label_entrada2
    label_entrada2=tk.Label(pestaña0,text="Ingrese su segundo numero",font=("Arial bold",10))
    label_entrada2.grid(column=0,row=2)



    entrada1 = tk.Entry(pestaña0, width=10)
    entrada2 = tk.Entry(pestaña0, width=10)

    entrada1.focus()
    entrada2.focus()

    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    global label_operador
    label_operador=tk.Label(pestaña0,text="Escoja un operador",font=("Arial bold",10))
    label_operador.grid(column=0,row=3)

    combo_operadores=ttk.Combobox(pestaña0)
    combo_operadores["values"]=["+","-","*","/","pow"]
    combo_operadores.current(0)
    combo_operadores.grid(column=1,row=3)

    #agregamos una etiqueta que muestre el resultado en pantalla
    global label_resultado
    label_resultado=tk.Label(pestaña0,text="Resultado: ",font=("Helvetica", 20, "bold italic"),)
    label_resultado.grid(column=0,row=5)

    #Boton_calcular uwu
    boton=tk.Button(pestaña0,
                    command=lambda:click_calcular(
                        label_resultado,
                        entrada1.get(),
                        entrada2.get(),
                        combo_operadores.get()),
                    text="Calcular",
                    bg="blue",
                    fg="white",bd=6)

    boton.grid(column=1,row=4)
    style = ttk.Style()

    #boton cambio de colores
    boton_cambio=tk.Button(pestaña0,text="Cambia el color del fondo",command=cambiar_color,bg="blue",fg="white",bd=5)
    boton_cambio.place(x=167,y=185)
    style = ttk.Style()

    style = ttk.Style()

    style.theme_use('default')

    style.configure("green.Horizontal.TProgressbar", background='green')

    bar = Progressbar(pestaña0, length=50, style='green.Horizontal.TProgressbar')

    bar['value'] = 50

    bar.place(x=380,y=175)
    ##############################################CALCULADORA COMPLEJA#################################################
    global label_1
    label_1 =tk.Label(pestaña1,text="Calculadora Compleja",font=("Helvetica", 20, "bold italic"))
    label_1.grid(column=0,row=0)

    global label_entrada1_1
    label_entrada1_1=tk.Label(pestaña1,text="Ingrese su primer numero",font=("Arial bold",10))
    label_entrada1_1.grid(column=0,row=1)

    entrada1_1 = tk.Entry(pestaña1, width=10)
    entrada1_1.focus()
    entrada1_1.grid(column=1, row=1)

    global label_operador_1
    label_operador_1=tk.Label(pestaña1,text="Escoja un operador",font=("Arial bold",10))
    label_operador_1.grid(column=0,row=3)

    combo_operadores_1=ttk.Combobox(pestaña1)
    combo_operadores_1["values"]=["exp","ln","sqrt"]
    combo_operadores_1.current(0)
    combo_operadores_1.grid(column=1,row=3)

    #agregamos una etiqueta que muestre el resultado en pantalla
    global label_resultado_1
    label_resultado_1=tk.Label(pestaña1,text="Resultado: ",font=("Helvetica", 20, "bold italic"),)
    label_resultado_1.grid(column=0,row=5)

    #Boton_calcular uwu
    boton_1=tk.Button(pestaña1,
                    command=lambda:click_calcular_1(
                        label_resultado_1,
                        entrada1_1.get(),
                        combo_operadores_1.get()),
                    text="Calcular",
                    bg="blue",
                    fg="white",
                      bd=5)

    boton_1.grid(column=1,row=4)
    style = ttk.Style()

    #boton cambio de colores
    boton_cambio1=tk.Button(pestaña1,text="Cambia el color del fondo",command=cambio_color2,bg="blue",fg="white",bd=5)
    boton_cambio1.place(x=167,y=185)
    style = ttk.Style()
    style = ttk.Style()

    style.theme_use('default')

    style.configure("green.Horizontal.TProgressbar", background='green')

    bar = Progressbar(pestaña1, length=50, style='green.Horizontal.TProgressbar')

    bar['value'] = 100

    bar.place(x=380,y=175)
    window.mainloop()

def calculadora(num1,num2,operador):
    global contador7
    contador7=0
    if operador=="+":
        resultado=num1+num2
    elif operador=="-":
        resultado=num1-num2
    elif operador=="*":
        resultado=num1*num2
    elif operador=="/":
        try:
            resultado = round(num1 / num2, 2)
        except ZeroDivisionError:
            contador7+=1
            messagebox.showerror('ERROR', 'No es posible la división entre cero :(')
    else:
        resultado=num1**num2
    if contador7!=1:
        return resultado

def calculadora_1(num1,operador):
    global contador8
    contador8=0
    if operador=="exp":
        resultado=round(math.e**num1,2)

    elif operador=="ln":
        try:
            resultado=round(math.log(num1),2)
        except ValueError:
            contador8+=1
            messagebox.showerror('ERROR', 'No es posible realizar el logaritmo natural de un valor negativo')
    else:
        try:
            resultado = round(((num1) ** (1 / 2)), 2)
        except ValueError or TypeError:
            contador8+=1
            messagebox.showerror('ERROR', 'No es posible realizar la raiz cuadrada de un valor negativo')
    if contador8!=1:
        return resultado
def click_calcular(label,num1,num2,operador):
    try:
        if num1==" " or num2==" ":
            messagebox.showerror('ERROR', 'Por favor, llena los campos')
        else:
            #convertimos los valores
            valor1=float(num1)
            valor2=float(num2)
            res=calculadora(valor1,valor2,operador)
            #actualizacion del texto de la etiqueta
            if contador7!=1:
                label.configure(text="Resultado: " + str(res), font=("Helvetica", 20, "bold italic"))
                messagebox.showinfo('Felicidades', 'Muy bien!, tu resultado fue: ' + str(res))
    except ValueError:
        messagebox.showwarning('PRECAUCIÓN', 'Ingresa unos datos validos')
def click_calcular_1(label,num1,operador):
    try:
        if num1==" ":
            messagebox.showerror('ERROR', 'Por favor, llena los campos')
        else:
            #convertimos los valores
            valor1=float(num1)
            res=calculadora_1(valor1,operador)
            #actualizacion del texto de la etiqueta
            if contador8!=1:
                label.configure(text="Resultado: " + str(res), font=("Helvetica", 20, "bold italic"))
                messagebox.showinfo('Felicidades', 'Muy bien!, tu resultado fue: ' + str(res))
    except ValueError:
        messagebox.showwarning('PRECAUCIÓN', 'Ingresa unos datos validos')
def main():
    init_window()
main()