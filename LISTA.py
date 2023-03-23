from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image
root = Tk()
root.title("Silvia")
root.configure(bg="#00FF00")
vent = Frame(root,bg="#00FFFF").grid()
Regris = Label(vent, text="REGISTRO DE PRODUCTOS", bg="#00FFFF", font=("Roboto",10)).grid(row=3,column=2)
""""
imge = Image.open("ima2.jpg")
imagens = imge.resize((50,50))
imagenA = ImageTk.PhotoImage(imagens)
Ponerimagen = Label(vent, image=imagenA).grid(row=5,column=2,columnspan=1,rowspan=2)
"""
Prod = Label(vent, text="Producto:", bg="#FF00FF", font=("Roboto",10)).grid(row=10,column=1)

Sku = Label(vent, text="SKU:", bg="#FF00FF", font=("Roboto",10)).grid(row=11,column=1)

registro = Entry(vent, bg="#CCCCCC", font=("Roboto",10)).grid(row=10,column=2, padx=1,pady=5)

productos = Entry(vent, bg="#CCCCCC", font=("Roboto",10)).grid(row=11,column=2, padx=1,pady=5)

depto = Label(vent, bg="#CCCCCC", text=("Depto:"),font=("Roboto",10)).grid(row=13,column=1)

Ba = tk.Checkbutton(vent, text="A", bg="#CCCCCC", font=("Roboto",10)).grid(row=15,column=1)
Bb = tk.Checkbutton(vent, text="B",bg="#CCCCCC", font=("Roboto",10)).grid(row=15,column=2)
Bc = tk.Checkbutton(vent, text="C", bg="#CCCCCC",font=("Roboto",10)).grid(row=15,column=3)

provedor = Label(vent, bg="#CCCCCC",text="Proveedor:", font=("Roboto",10)).grid(row=16,column=1)
lista_desplegable = ttk.Combobox(vent,width=17)
lista_desplegable.grid(row=16,column=2)
opciones = ["OP1", "OP2", "OP3"]
lista_desplegable['values']=opciones
  
idioma = Label(vent, bg="#CCCCCC",text="Idioma:", font=("Roboto",10)).grid(row=17,column=1)
Be = tk.Checkbutton(vent, bg="#CCCCCC", text="EN",font=("Roboto",10)).grid(row=18,column=1)
Bs = tk.Checkbutton(vent, bg="#CCCCCC", text="ESP",font=("Roboto",10)).grid(row=18,column=2)

registrar = Button(vent, text=("Registrar"), font=("Roboto",10),width=20,height=1).grid(row=25,column=2,padx=1,pady=5)

root.mainloop()