# CalculadoraTk
Proyecto de clase de PC Grupo 12. Realizado por Alejandro Mahecha Arango.

Información basica del proyecto:
Este proyecto consiste en el diseño de una calculadora con la libreria Tkinter. 

El programa necesita las siguientes librerias (pero no requieren instalación): 

import tkinter as tk
-from tkinter.ttk import Progressbar
-from tkinter import messagebox
-from tkinter import ttk
-import random
-import math

Widgets añadidos: 
1. MessageBox: Genera una ventana de error, en caso de que se realicen operaciones con numeros complejos o indeterminaciones. Ademas produce advertencias si los campos de texto estan vacios. De igual manera, si el usuario hace la operacion correctamente, genera una ventana en la que muestra el resultado.
2. Notebook widget: Permite generar pestañas (Tabs).
3. ProgressBar: Representa en que pestaña se encuentre el usuario. 

La calculadora puede variar entre operaciones basicas y otra pestaña de operaciones mas complejas como Ln, exp, y se tiene la posibilidad e cambiar el color de fondo de la calculadora a un aleatorio (cada pestaña es independiente del color de la otra).

![Presentacion](https://user-images.githubusercontent.com/73804094/99122177-d958db00-25cb-11eb-8f29-3265428fa484.png)
