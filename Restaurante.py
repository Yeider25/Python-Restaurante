import tkinter as tk
import platform
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()
ventana.config(bg="white")
ventana.title("Tienda")
ventana.iconbitmap('./img/Logo_cafe.ico')  

# Maximizar ventana
if platform.system() == "Windows":
    ventana.state("zoomed")
else:
    ventana.attributes("-fullscreen", True)
    
tk.Label(ventana, text="BIENVENIDO",font=("Rockwell", 30, "bold"),background="white",pady=30,padx=100).pack(anchor="n")
tk.Label(ventana, text="¡Realiza tu pedido ahora!",font=("Rockwell", 10, "bold"),background="white").pack()
    
# Crear el frame de comidas
frame_comidas = tk.Frame(ventana,bg="white")
frame_comidas.pack(side=tk.LEFT,padx=100)
tk.Label(frame_comidas, text="Comidas", font=("Rockwell", 20, "bold"),bg="orange").pack(anchor="n")

# Crear el frame de bebidas
frame_bebidas = tk.Frame(ventana,bg="white")
frame_bebidas.pack(side=tk.RIGHT,padx=100)
tk.Label(frame_bebidas, text="Bebidas", font=("Rockwell", 20, "bold"),bg="orange").pack(anchor="n")

# Crear las comidas
comidas = [
    {"nombre": "Empanada", "precio": 2500, "imagen": "img/Empanada.png"},
    {"nombre": "Hamburguesa", "precio": 7000, "imagen": "img/Hamburguesa.jpeg"},
    {"nombre": "Pizza", "precio": 6000, "imagen": "img/Pizza.jpg"}
]

# Crear las bebidas
bebidas = [
    {"nombre": "Cocacola", "precio": 3000, "imagen": "img/Cocacola.jpg"},
    {"nombre": "Postobon", "precio": 3000, "imagen": "img/Postobon.jpg"},
    {"nombre": "Colombiana", "precio": 3000, "imagen": "img/Colombiana.png"}
]

# Crear el total del pedido
total_pedido = tk.IntVar()
total_pedido.set(0)

for comida in comidas:
    
    imagen = ImageTk.PhotoImage(Image.open(comida["imagen"]))
    imagen_label = tk.Label(frame_comidas, image=imagen,width=150,height=150)
    imagen_label.image = imagen
    imagen_label.pack()

    cantidad = tk.IntVar()
    cantidad_selector = tk.Spinbox(frame_comidas, from_=0, to=10, textvariable=cantidad, font=("Rockwell", 10, "bold"),borderwidth=3)
    cantidad_selector.pack()
    
    nombre = tk.Label(frame_comidas, text=comida["nombre"], font=("Rockwell", 10, "bold"),background="white")
    nombre.pack()

    precio = tk.Label(frame_comidas, font=("Rockwell", 10, "bold"),background="white",text=f"${comida['precio']}")
    precio.pack()

    def actualizar_total():
        total_pedido.set(total_pedido.get() + cantidad.get() * comida['precio'])

    boton_agregar = tk.Button(frame_comidas, text="Agregar al pedido", command=actualizar_total,background="orange", font=("Rockwell", 10, "bold"),padx=10)
    boton_agregar.pack()

for bebida in bebidas:
    
    imagen = ImageTk.PhotoImage(Image.open(bebida["imagen"]))
    imagen_label = tk.Label(frame_bebidas, image=imagen,width=150,height=150)
    imagen_label.image = imagen
    imagen_label.pack()

    cantidad = tk.IntVar()
    cantidad_selector = tk.Spinbox(frame_bebidas, from_=0, to=10, textvariable=cantidad, font=("Rockwell", 10, "bold"),borderwidth=3)
    cantidad_selector.pack()
    
    nombre = tk.Label(frame_bebidas, text=bebida["nombre"], font=("Rockwell", 10, "bold"),background="white")
    nombre.pack()

    precio = tk.Label(frame_bebidas, font=("Rockwell", 10, "bold"),background="white",text=f"${bebida['precio']}")
    precio.pack()

    def actualizar_total():
        total_pedido.set(total_pedido.get() + cantidad.get() * bebida['precio'])

    boton_agregar = tk.Button(frame_bebidas, text="Agregar al pedido", command=actualizar_total,background="orange", font=("Rockwell", 10, "bold"))
    boton_agregar.pack()


total_label = tk.Label(ventana, textvariable=total_pedido)
total_label.pack()

# Iniciar la aplicación
ventana.mainloop()