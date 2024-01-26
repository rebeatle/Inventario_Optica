import tkinter as tk
from tkinter import Toplevel, Entry, Label, Frame, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END, messagebox
from requests_sql import BaseData
import datetime
class RegistroVentana(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.wm_title("Ventana de Registro1")
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
        self.boton_ojos()



        #fram1

    def botones_cajas(self):

        self.cajas = {}  # Diccionario para almacenar las cajas de texto

        campos = ["Nombre", "Numerouno", "Numerodos", "Correo", "DNI", "Direccion", "Ruc10", "fecha", "Observacion"]

        for i, campo in enumerate(campos):
            etiqueta = Label(self.frame1, text=f"{campo}:")
            etiqueta.grid(row=i, column=0, padx=10, pady=1, sticky="w")

            if campo == "Observacion":
                caja = tk.Text(self.frame1, height=10, width=30)  # Ajustar el ancho y alto
            else:
                caja = tk.Entry(self.frame1, width=30)

            self.cajas[campo] = caja  # Agregar la caja al diccionario
            caja.grid(row=i, column=1, padx=10, pady=1, sticky="w")

        #boton generar fecha
        boton_generar_fecha = tk.Button(self.frame1, text="Generar fecha", command=self.generar_fecha)
        boton_generar_fecha.grid(row=7, column=3, padx=15, pady=1)
        # Botón Guardar
        boton_guardar = Button(self.frame1, text="Guardar", command=self.guardar_datos, width=10 , height= 3)
        boton_guardar.grid(row=10, column=0, padx=10, pady=10)

        # Botón borrar
        boton_borrar = Button(self.frame1, text="Exterminar", command=self.borrar_datos, width=10 , height= 3)
        boton_borrar.grid(row=10, column=3, padx=10, pady=10)
    def obtener_valores(self):
        # Método para obtener los valores de las cajas
        valores = {}
        for campo, caja in self.cajas.items():
            if campo == "Observacion":
                valores[campo] = caja.get("1.0", "end-1c")
            else:
                valores[campo] = caja.get()
        return valores
    def generar_fecha(self):
        # Obtener la fecha actual y hora actual
        fecha_actual = datetime.datetime.now()

        # Formatear la fecha como una cadena en el formato deseado
        fecha_formateada = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")

        # Establecer la fecha formateada en la caja correspondiente
        self.cajas["fecha"].delete(0, 'end')
        self.cajas["fecha"].insert(0, fecha_formateada)

    def guardar_datos(self):
        db = BaseData()
        valores = self.obtener_valores()
        id_cliente = db.insertar_cliente(
            valores["Nombre"],
            valores["Numerouno"],
            valores["Numerodos"],
            valores["Correo"],
            valores["DNI"],
            valores["Direccion"],
            valores["Ruc10"],
            valores["fecha"],
            valores["Observacion"]
        )

        db.insertar_medidas(
            id_cliente,
            self.caja_ojo_derecho_esfera.get(),
            self.caja_ojo_izquierdo_esfera.get(),
            self.caja_ojo_derecho_cilindro.get(),
            self.caja_ojo_izquierdo_cilindro.get(),
            self.caja_ojo_derecho_eje.get(),
            self.caja_ojo_izquierdo_eje.get(),
            self.caja_ojo_derecho_Adicion.get(),
            self.caja_ojo_izquierdo_Adicion.get(),
            self.caja_ojo_derecho_Esfera_cerca.get(),
            self.caja_ojo_izquierdo_Esfera_cerca.get(),
            self.caja_ojo_derecho_NP.get(),
            self.caja_ojo_izquierdo_NP.get()
        )

        db.cerrar_conexion()
        self.borrar_datos()  # Limpia las cajas después de guardar los datos
        # Cerrar la ventana actual
        self.destroy()
        # Después de guardar los datos, mostrar una ventana de confirmación
        messagebox.showinfo("Guardado", "Los datos del cliente se han guardado correctamente.")

    def borrar_datos(self):
        for caja in self.cajas.values():
            if isinstance(caja, tk.Entry):  # Verificar si la caja es de tipo Entry
                caja.delete(0, 'end')  # Borrar desde el inicio hasta el final
            elif isinstance(caja, tk.Text):  # Verificar si la caja es de tipo Text
                caja.delete('1.0', 'end')  # Borrar desde la línea 1, columna 0 hasta el final




    #frame 3
    def boton_ojos(self):
        #etiquetas ojos
        self.etiqueta_ojo_derecho = Label(self.frame3, text="Ojo derecho:")
        self.etiqueta_ojo_derecho.grid(row=3, column=0, padx=1, pady=1, sticky="w")

        self.etiqueta_ojo_izquierdo = Label(self.frame3, text="Ojo izquierdo:")
        self.etiqueta_ojo_izquierdo.grid(row=4, column=0, padx=1, pady=1, sticky="w")

        # Etiquetas superiores
        etiquetas = ["Esfera", "Cilindro", "Eje", "Adicion", "Esfera cerca", "N/P"]
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



if __name__ == "__main__":
    ventana = tk.Tk()
    app = RegistroVentana(ventana)
    app.mainloop()