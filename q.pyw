from tkinter import *
from tkinter import messagebox
import mysql.connector

# CONEXIÓN DE BASE DE DATOS
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='restaurante'
)
cursor = conexion.cursor()

#FUNCIÓN PARA GUARDAR LOS PEDIDOS
def guardar_pedido(Cantidad, Id_Bebidas, Id_Comidas, Total):
    try:
        if Cantidad <= 0:
            messagebox.showerror("Error", "Tiene que elegir una opción para poder realizar la compra")
            return
        
        consulta = "INSERT INTO Pedidos (Cantidad, Id_Bebidas, Id_Comidas, Total) VALUES (%s, %s,%s,%s)"
        valores = (Cantidad, Id_Bebidas, Id_Comidas, Total)
        cursor.execute(consulta, valores)
        conexion.commit()
        messagebox.showinfo("Pedido exitoso", "Guardado correctamente")

    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo guardar el pedido: {str(e)}")
        conexion.rollback()

#Función para un frame de facturación 
def facturación():
    fact_fr=Toplevel()
    fact_fr.title("Factura")
    fact_fr.geometry("300x200")
    fact_fr.config(bg="lightgreen")
    cursor.execute("SELECT Cantidad, Total FROM Pedidos")
    pedidos = cursor.fetchall()
    Label(fact_fr,text="¡GRACIAS POR COMPRAR! :D").pack()
    Button(fact_fr, text="Cerrar", command=fact_fr.destroy).pack()


# cantidad total de bebidas y comidas
    Cantidad = sum(pedidos[0] for pedidos in pedidos if pedidos[1] is not None)

    # TOTAL FACTURA
    total_factura = sum(pedidos[2] for pedidos in pedidos)
    
    # MOSTRAR CANTIDAD DE PRODUCTOS
    Label(fact_fr, text=f"Cantidad: {Cantidad}").pack()
    Label(fact_fr, text=f"Total factura: ${total_factura:.2f}").pack()

#Función salir 
def salir():
    print

# Función para mostrar un nuevo frame
def mostrar_frame(nombre, imagenes=None):
    n_frin = Toplevel()
    n_frin.title(nombre)
    n_frin.geometry("300x200")
    Label(n_frin, text=f"Este es el apartado {nombre}").pack()

#Barra de menú
    barra = Menu(n_frin)
    n_frin.config(menu=barra, width=400, height=300)
    Comidas = Menu(barra, tearoff=0)
    Bebidas = Menu(barra, tearoff=0)
    General = Menu(barra, tearoff=0)
    salir = Menu(barra, tearoff=0)

# SUBMENU
    barra.add_cascade(label="Comidas", menu=Comidas)
    barra.add_cascade(label="Bebidas", menu=Bebidas)
    barra.add_cascade(label="General", menu=General)
    barra.add_cascade(label="Salir", menu=salir)

#COMANDOS PARA BARRA DE MENU EN CADA FRAME 
    Comidas.add_command(label="Mostrar Comidas", command=lambda:mostrar_frame("Comidas", imagenes_comidas))
    Bebidas.add_command(label="Mostrar Bebidas", command=lambda:mostrar_frame("Bebidas", imagenes_Bebidas))
    General.add_command(label="Mostrar General", command=lambda:mostrar_frame("General", imagenes_General))
    salir.add_command(label="me quiero ir", command=quit)

#COLOR FRAMES SECUNDARIOS
    if nombre=="Comidas":
        n_frin.configure(bg="lightblue")
    elif nombre=="Bebidas":
        n_frin.configure(bg="lightgreen")
    elif nombre=="General":
        n_frin.configure(bg="lightyellow")

#FUNCIÓN PARA PONER VARIAS IMAGENES
    if imagenes:
        for i, imagen in enumerate(imagenes):
            imagen_b=Checkbutton(n_frin, image=imagen)
            imagen_b.pack()
            Label(n_frin).pack()

#CONFIGURACIÓN PARA QUE ATRAVÉS DE LA IMAGÉN SE GUARDE LOS CAMPOS
    imagen_b.config(command=lambda imagen=imagen: guardar_pedido(imagen.Cantidad, imagen.Id_Comidas, imagen.Id_Bebidas, imagen.Total))

#BOTÓN PARA SELECCIONAR PEDIDO
    b_seleccionar=Button(n_frin, text="Seleccionar Pedido", command=facturación)
    b_seleccionar.pack(pady=10)
    
#BOTONES DE PRECIOS: 
    """hamburguesa=Label(n_frin, text="Hamburguesa: $10.000")
    n_frin.mainloop()"""

# CREACIÓN DEL FRAME PRINCIPAL
frein = Tk()
frein.resizable(False, False) #PROPIEDAD PARA QUE NO SEA REDIMENSIONABLE
frein.title("Restaurante")
frein.config(width=100, height=200)

"""titulo = Label(frein, text="Se le tiene")
titulo.grid(row=0, column=2, columnspan=3)"""

#imagen principal cargue
imagen_restaurante = PhotoImage(file="restaurante.png")

#visualizar la imagén
restaurante= Label (frein, image=imagen_restaurante)
restaurante.grid(row=2, column=0)

# Barra de menú
barra = Menu(frein)
frein.config(menu=barra, width=400, height=300)
Comidas = Menu(barra, tearoff=0)
Bebidas = Menu(barra, tearoff=0)
General = Menu(barra, tearoff=0)
salir=Menu(barra, tearoff=0)

# SUBMENU
barra.add_cascade(label="Comidas", menu=Comidas)
barra.add_cascade(label="Bebidas", menu=Bebidas)
barra.add_cascade(label="General", menu=General)
barra.add_cascade(label="Salir", menu=salir)
#CONFIGURACIÓN PARA CADA FRAME- IMAGENES
imagenes_comidas= [
    PhotoImage(file="Hamburguesa.png").subsample(2),
    PhotoImage(file="salchipapas.png").subsample(3),
    PhotoImage(file="pizza.png").subsample(3)
]
imagenes_Bebidas=[
    PhotoImage(file="Cocacola.png").subsample(2),
    PhotoImage(file="agua.png").subsample(3),
    PhotoImage(file="vino.png").subsample(3)
]
imagenes_General=[
    PhotoImage(file="Hamburguesa.png").subsample(3),
    PhotoImage(file="Cocacola.png").subsample(3),
    PhotoImage(file="salchipapas.png").subsample(4),
    PhotoImage(file="agua.png").subsample(4),
    PhotoImage(file="pizza.png").subsample(4),
    PhotoImage(file="vino.png").subsample(3)
]

# COMANDOS PARA MOSTRAR LOS FRAMES SECUNDARIOS
Comidas.add_command(label="Mostrar Comidas", command=lambda:mostrar_frame("Comidas", imagenes_comidas))
Bebidas.add_command(label="Mostrar Bebidas", command=lambda:mostrar_frame("Bebidas", imagenes_Bebidas))
General.add_command(label="Mostrar General", command=lambda:mostrar_frame("General", imagenes_General))
salir.add_command(label="ya, chao", command=quit)

frein.mainloop()
conexion.close()