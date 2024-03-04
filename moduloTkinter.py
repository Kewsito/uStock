import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos
import database
class FormularioArticulos:
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Mantenimiento de artículos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_articulos()
        self.listado_completo()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Artículo")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        # Descripción label
        self.label0=ttk.Label(self.labelframe1, text="Descripción:")
        self.label0.grid(column=0, row=0, padx=4, pady=4)
        # Descripción entry
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        # Marca label
        self.label1=ttk.Label(self.labelframe1, text="Marca:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        # Marca entry
        self.marcacarga=tk.StringVar()
        self.entrymarca=ttk.Entry(self.labelframe1, textvariable=self.marcacarga)
        self.entrymarca.grid(column=1, row=1, padx=4, pady=4)
        # Talle
        self.label2=ttk.Label(self.labelframe1, text="Talle:")        
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        # Talle entry
        self.tallecarga=tk.StringVar()
        self.entrytalle=ttk.Entry(self.labelframe1, textvariable=self.tallecarga)
        self.entrytalle.grid(column=1, row=2, padx=4, pady=4)
        # Precio label
        self.label3=ttk.Label(self.labelframe1, text="Precio:")        
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        # Precio entry
        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=3, padx=4, pady=4)
        # Bolsa
        self.label4=ttk.Label(self.labelframe1, text="Bolsa:")        
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        # Bolsa entry
        self.bolsacarga=tk.StringVar()
        self.entrybolsa=ttk.Entry(self.labelframe1, textvariable=self.bolsacarga)
        self.entrybolsa.grid(column=1, row=4, padx=4, pady=4)
        # Boton
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=5, padx=4, pady=4)

    def agregar(self):
        datos=(self.descripcioncarga.get(),self.entrymarca.get(), self.tallecarga.get(),self.preciocarga.get(),self.bolsacarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcioncarga.set("")
        self.marcacarga.set("")
        self.tallecarga.set("")
        self.preciocarga.set("")
        self.bolsacarga.set("")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=50, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "Código:"+str(fila[0])+"\nDescripción:"+fila[1]+"\nMarca:"+fila[2]+"\nTalle:"+str(fila[3])+"\nBolsa:"+str(fila[4])+"\nPrecio:"+str(fila[5])+"\n")
            self.scrolledtext1.insert(tk.END, "-"*50+"\n")
            
    def modificar(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Modificar precio segun codigo")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        # Código label
        self.label5=ttk.Label(self.labelframe2, text="Código:")
        self.label5.grid(column=0, row=0, padx=4, pady=4)
        # Código entry
        self.codigomod=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        # Nuevo precio label
        self.label6=ttk.Label(self.labelframe2, text="Nuevo precio:")
        self.label6.grid(column=0, row=1, padx=4, pady=4)
        # Nuevo precio entry
        self.nuevoprecio=tk.StringVar()
        self.entrynuevoprecio=ttk.Entry(self.labelframe2, textvariable=self.nuevoprecio)
        self.entrynuevoprecio.grid(column=1, row=1, padx=4, pady=4)
        # Boton
        self.boton2=ttk.Button(self.labelframe2, text="Modificar", command=self.modificar_precio)
        self.boton2.grid(column=1, row=2, padx=4, pady=4)

    def modificar_precio(self):
        datos = (self.nuevoprecio.get(), self.codigomod.get())
        self.articulo1.modificar_precio(datos)
        mb.showinfo("Información", "El precio ha sido modificado")
        self.codigomod.set("")
        self.nuevoprecio.set("")
if __name__ == '__main__':
    database.crear_tabla("mi_database.db")
    aplicacion1=FormularioArticulos()
    
    