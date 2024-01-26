import tkinter as tk
from tkinter import Toplevel, Entry, Label, Frame, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END


class HojaCliente(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.wm_title("Ventana Cliente")
        self.config(bg='gray22')
        self.geometry('900x600')
        self.resizable(True, True)

        #frame 1
        self.frame1 = Frame(self, bg='brown', width=100)
        self.frame1.grid(column=0, row=0, sticky="nsew")
        #frame 2
        self.frame2 = Frame(self, bg='brown')
        self.frame2.grid(column=1, row=0, sticky="nsew")
        # frame 3
        self.frame3 = Frame(self, bg='white', height=120)
        self.frame3.grid( row=1, columnspan=2, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


         #Crear los botones mediante funciones
        #frame1
        self.botones_cajas()
        #fram2
        #self.boton_pedidos()
        #fram3 abajo
        self.frame_ojos()

        #fram1
    def botones_cajas(self):

        self.cajas_cliente = {}  # Diccionario para almacenar las cajas de texto del cliente
        self.cajas_medidas = {}  # Diccionario para almacenar las cajas de texto de medidas

        campos = ["Nombre", "Numerouno", "Numerodos", "Correo", "DNI", "Direccion", "Ruc10", "fecha ingreso",
                  "Observacion"]

        for i, campo in enumerate(campos):
            etiqueta = Label(self.frame1, text=f"{campo}:")
            etiqueta.grid(row=i, column=0, padx=10, pady=1, sticky="w")

            if campo == "Observacion":
                caja = tk.Text(self.frame1, height=10, width=30)  # Ajustar el ancho y alto
            else:
                caja = tk.Entry(self.frame1, width=15)

            self.cajas_cliente[campo] = caja  # Agregar la caja al diccionario del cliente
            caja.grid(row=i, column=1, padx=10, pady=1, sticky="w")


#frame2




    # def boton_pedidos(self):
    #
    #     self.etiqueta_ver_pedido = Label(self.frame2, text="Ver pedido:")
    #     self.etiqueta_ver_pedido.grid(row=1, column=2, padx=1, pady=1, sticky="n")
    #
    #
    #     self.etiqueta_registrar_pedido = Label(self.frame2, text="Registgrar pedido:")
    #     self.etiqueta_registrar_pedido.grid(row=1, column=4, padx=1, pady=1, sticky="n")

#frame 3
    def frame_ojos(self):
        #etiquetas ojos
        self.etiqueta_ojo_derecho = Label(self.frame3, text="Ojo derecho:")
        self.etiqueta_ojo_derecho.grid(row=3, column=0, padx=1, pady=1, sticky="w")

        self.etiqueta_ojo_izquierdo = Label(self.frame3, text="Ojo izquierdo:")
        self.etiqueta_ojo_izquierdo.grid(row=4, column=0, padx=1, pady=1, sticky="w")

        # Etiquetas superiores
        etiquetas = ["Esfera", "Cilindro", "Eje", "Adicion", "Esfera cerca", "N/P"]
        self.cajas_medidas = {}  # Diccionario para almacenar las cajas de medidas
        for i, etiqueta_texto in enumerate(etiquetas):
            etiqueta = Label(self.frame3, text=etiqueta_texto)
            etiqueta.grid(row=2, column=i+1, padx=1, pady=1)

        #cajas
        self.caja_ojo_derecho_esfera = Entry(self.frame3)
        self.caja_ojo_derecho_esfera.grid(row=3, column=1, padx=1, pady=1, sticky="w")
        self.caja_ojo_izquierdo_esfera = Entry(self.frame3)
        self.caja_ojo_izquierdo_esfera.grid(row=4, column=1, padx=1, pady=1, sticky="w")

        self.caja_ojo_derecho_cilindro = Entry(self.frame3)
        self.caja_ojo_derecho_cilindro.grid(row=3, column=2, padx=1, pady=1, sticky="w")
        self.caja_ojo_izquierdo_cilindro = Entry(self.frame3)
        self.caja_ojo_izquierdo_cilindro.grid(row=4, column=2, padx=1, pady=1, sticky="w")

        self.caja_ojo_derecho_eje = Entry(self.frame3)
        self.caja_ojo_derecho_eje.grid(row=3, column=3, padx=1, pady=1, sticky="w")
        self.caja_ojo_izquierdo_eje = Entry(self.frame3)
        self.caja_ojo_izquierdo_eje.grid(row=4, column=3, padx=1, pady=1, sticky="w")

        self.caja_ojo_derecho_Adicion = Entry(self.frame3)
        self.caja_ojo_derecho_Adicion.grid(row=3, column=4, padx=1, pady=1, sticky="w")
        self.caja_ojo_izquierdo_Adicion = Entry(self.frame3)
        self.caja_ojo_izquierdo_Adicion.grid(row=4, column=4, padx=1, pady=1, sticky="w")

        self.caja_ojo_derecho_Esfera_cerca = Entry(self.frame3)
        self.caja_ojo_derecho_Esfera_cerca.grid(row=3, column=5, padx=1, pady=1, sticky="w")
        self.caja_ojo_izquierdo_Esfera_cerca = Entry(self.frame3)
        self.caja_ojo_izquierdo_Esfera_cerca.grid(row=4, column=5, padx=1, pady=1, sticky="w")

        self.caja_ojo_derecho_NP = Entry(self.frame3)
        self.caja_ojo_derecho_NP.grid(row=3, column=6, padx=1, pady=1, sticky="w")
        self.caja_ojo_izquierdo_NP = Entry(self.frame3)
        self.caja_ojo_izquierdo_NP.grid(row=4, column=6, padx=1, pady=1, sticky="w")

    def insertar_datos(self, cliente):
        campos = ["Nombre", "Numerouno", "Numerodos", "Correo", "DNI", "Direccion", "Ruc10", "fecha ingreso",
                  "Observacion"]
        for campo, valor in zip(campos, cliente[1:]):
            if campo == "Observacion":
                self.cajas_cliente[campo].insert("1.0", valor)

            else:
                self.cajas_cliente[campo].insert(0, valor)
                # Hacer la caja de texto solo de lectura
                self.cajas_cliente[campo].configure(state="readonly")

    def insertar_medidas(self, medidas_cliente):
        print("Claves disponibles en self.cajas:", self.cajas_medidas.keys())
        # Insertar los datos de medidas en las cajas correspondientes
        # Asegúrate de tener las mismas etiquetas en la misma posición en las cajas de medidas
        campos_medidas = ["od_esfera", "od_cilindo", "od_eje", "od_adicion", "od_esfera_c", "od_np",
                          "oi_esfera", "oi_cilindo", "oi_eje", "oi_adicion", "oi_esfera_c", "oi_np"]

        # Ojo derecho
        self.caja_ojo_derecho_esfera.insert(0, medidas_cliente[1])
        self.caja_ojo_derecho_cilindro.insert(0, medidas_cliente[2])
        self.caja_ojo_derecho_eje.insert(0, medidas_cliente[3])
        self.caja_ojo_derecho_Adicion.insert(0, medidas_cliente[4])
        self.caja_ojo_derecho_Esfera_cerca.insert(0, medidas_cliente[5])
        self.caja_ojo_derecho_NP.insert(0, medidas_cliente[6])

        # Hacer la caja de texto solo de lectura
        self.caja_ojo_derecho_esfera.configure(state="readonly")
        self.caja_ojo_derecho_cilindro.configure(state="readonly")
        self.caja_ojo_derecho_eje.configure(state="readonly")
        self.caja_ojo_derecho_Adicion.configure(state="readonly")
        self.caja_ojo_derecho_Esfera_cerca.configure(state="readonly")
        self.caja_ojo_derecho_NP.configure(state="readonly")

        # Ojo izquierdo
        self.caja_ojo_izquierdo_esfera.insert(0, medidas_cliente[7])
        self.caja_ojo_izquierdo_cilindro.insert(0, medidas_cliente[8])
        self.caja_ojo_izquierdo_eje.insert(0, medidas_cliente[9])
        self.caja_ojo_izquierdo_Adicion.insert(0, medidas_cliente[10])
        self.caja_ojo_izquierdo_Esfera_cerca.insert(0, medidas_cliente[11])
        self.caja_ojo_izquierdo_NP.insert(0, medidas_cliente[12])

        # Hacer la caja de texto solo de lectura
        self.caja_ojo_izquierdo_esfera.configure(state="readonly")
        self.caja_ojo_izquierdo_cilindro.configure(state="readonly")
        self.caja_ojo_izquierdo_eje.configure(state="readonly")
        self.caja_ojo_izquierdo_Adicion.configure(state="readonly")
        self.caja_ojo_izquierdo_Esfera_cerca.configure(state="readonly")
        self.caja_ojo_izquierdo_NP.configure(state="readonly")
