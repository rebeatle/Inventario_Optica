import tkinter as tk
from tkinter import Frame, ttk, PhotoImage, Label

from ventana_registrar import RegistroVentana
from ventana_cliente import HojaCliente
from requests_sql import BaseData

class OpticaApp:
    def __init__(self, master):
        self.master = master
        self.master.wm_title("Sistema Optica")
        self.master.config(bg='gray22')
        self.master.geometry('950x700')
        self.master.resizable(True, True)

        # Frame 1 (con botones)
        self.frame1 = Frame(self.master, bg='white')
        self.frame1.grid(column=0, row=0, sticky="nsew")
        self.master.columnconfigure(0, weight=1)  # Expansión horizontal
        # Agregar imagen de fondo a la izquierda
        self.image_left = PhotoImage(file="test3.png")
        self.background_label_left = Label(self.frame1, image=self.image_left, bd=0)
        self.background_label_left.grid(row=0, column=0, rowspan=6, padx=5, pady=5, sticky="w")


        # Frame 2 (lista de clientes)
        self.frame2 = Frame(self.master, bg='black')
        self.frame2.grid(column=0, row=1, sticky="nsew")
        self.master.rowconfigure(1, weight=1)  # Expansión vertical

        # Frame 3 (contenedor de la lista de clientes)
        self.frame3 = ttk.Frame(self.frame2, style="frame3.TFrame")
        self.frame3.grid(row=1, sticky="nsew")

        # Configurar expansión horizontal y vertical para Frame3
        self.frame2.rowconfigure(1, weight=1)  # Expansión vertical
        self.frame2.columnconfigure(0, weight=1)  # Expansión horizontal

        # Configurar barra de desplazamiento
        self.scrollbar = ttk.Scrollbar(self.frame3, orient=tk.VERTICAL)
        self.canvas = tk.Canvas(self.frame3, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Frame interior para contener la lista de clientes
        self.inner_frame = ttk.Frame(self.canvas, style="My.TFrame")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Configurar el Canvas para habilitar el desplazamiento vertical y horizontal
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configurar expansión horizontal para el inner_frame
        self.inner_frame.columnconfigure(0, weight=1)

        # # Crear estilo para resaltar
        # ttk.Style().configure("Resaltado.TLabel", background="orange")
        
        # Después de configurar los estilos existentes, agrega lo siguiente:
        ttk.Style().configure("Resultado.TLabel", background="white", foreground="black")

        # Crear estilo para los encabezados
        ttk.Style().configure("Encabezado.TLabel", font=("Helvetica", 10, "bold"))

        # Estilo para el frame interno
        ttk.Style().configure("My.TFrame", background="white")  # Ajusta el color según tus preferencias
        self.botones_widgets()


        # Agregar imagen de fondo a la derecha
        self.image_right = PhotoImage(file="test3.png")
        self.background_label_right = Label(self.frame1, image=self.image_right, bd=0)
        self.background_label_right.grid(row=0, column=2, rowspan=6, padx=5, pady=5, sticky="e")


        self.inicializar_encabezados()
        self.base_datos = BaseData()  # Crear una instancia de la clase BaseData
        self.filas_clientes = []  # Almacenar las etiquetas de las filas

        # Almacena el ID del cliente seleccionado
        self.id_cliente_seleccionado = None

    def botones_widgets(self):
        botones_frame = tk.Frame(self.frame1, bg='white')  # Frame para los botones dentro de frame2
        botones_frame.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        self.boton_registrar = tk.Button(botones_frame, text="Registrar cliente", command=self.registrar)
        self.boton_registrar.pack(pady=10)

        self.boton_buscar = tk.Button(botones_frame, text="Buscar Cliente Por nombre o DNI", command=self.buscar_cliente)
        self.boton_buscar.pack(pady=10)

        # Empacar la caja de búsqueda dentro de botones_frame
        self.caja_buscar = tk.Entry(botones_frame)
        self.caja_buscar.pack(pady=5)


    def inicializar_encabezados(self):
        # Encabezados por columna
        encabezados = ["Nombre", "Telefono1", "Telefono2", "Correo", "Dni"]
        for i, encabezado in enumerate(encabezados):
            boton = ttk.Button(self.inner_frame, text=encabezado, style="Encabezado.TButton", command=lambda i=i: self.ordenar_por_columna(i))
            boton.grid(row=0, column=i, padx=45, pady=15, sticky="nsew")
        # Configurar estilo para centrar el texto y expandir la caja
        style = ttk.Style()
        style.configure("Encabezado.TButton", padding=(10, 0), anchor="center")
    def registrar(self):
        self.Registro_ventana = RegistroVentana(self.master)

    def limpiar_resultados_busqueda(self):
        # Limpia los resultados anteriores en el tercer frame
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

    def buscar_cliente(self):
        nombre_o_dni = self.caja_buscar.get()
        resultados = self.base_datos.buscar_cliente_db(nombre_o_dni)

        # Limpiar resultados anteriores
        self.limpiar_resultados_busqueda()

        # Mostrar encabezados si es la primera búsqueda
        if not self.inner_frame.winfo_children():
            self.inicializar_encabezados()

        # Mostrar resultados en el tercer frame
        for idx, resultado in enumerate(resultados):
            self.mostrar_resultado_busqueda(resultado, idx + 1)

    def mostrar_resultado_busqueda(self, resultado, row):
        # Muestra un resultado de búsqueda en el tercer frame
        encabezados = ["Nombre", "Telefono1", "Telefono2", "Correo", "Dni"]
        etiquetas_fila = []

        for i, encabezado in enumerate(encabezados):
            etiqueta = ttk.Label(self.inner_frame, text=resultado[i + 1], font=("Helvetica", 10), style="Resultado.TLabel")
            etiqueta.grid(row=row, column=i, padx=5, pady=5, sticky="n")
            etiquetas_fila.append(etiqueta)

        # Almacenar las etiquetas de la fila
        self.filas_clientes.append(etiquetas_fila)

        # # Asociar eventos a las etiquetas para resaltar y mostrar la información completa
        for etiqueta in etiquetas_fila:
        #     etiqueta.bind("<Enter>", lambda e, row=row: self.resaltar_fila(row))
        #     etiqueta.bind("<Leave>", lambda e, row=row: self.desresaltar_fila(row))
             etiqueta.bind("<Button-1>", lambda e, cliente=resultado: self.mostrar_cliente_completo(cliente))

        # Actualizar la configuración de la barra de desplazamiento
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    # def resaltar_fila(self, row):
    #     # Cambiar el fondo de la fila cuando el mouse está sobre ella
    #     for etiqueta in self.filas_clientes[row - 1]:
    #         etiqueta.configure(style="Resaltado.TLabel")
    #
    # def desresaltar_fila(self, row):
    #     # Restaurar el fondo de la fila cuando el mouse sale
    #     for etiqueta in self.filas_clientes[row - 1]:
    #         etiqueta.configure(style="TLabel")

    def mostrar_cliente_completo(self, cliente):
        # Obtener el ID del cliente seleccionado
        self.id_cliente_seleccionado = cliente[0]

        # Abrir la ventana_cliente.py e insertar los datos en las cajas de entry correspondientes
        ventana_cliente = HojaCliente(self.master)
        ventana_cliente.insertar_datos(cliente)

        # Buscar y mostrar las medidas del cliente
        cliente_completo = self.base_datos.buscar_cliente_por_id(self.id_cliente_seleccionado)
        if cliente_completo:
            _, medidas_cliente = cliente_completo
            ventana_cliente.insertar_medidas(medidas_cliente)

def main():
    ventana_principal = tk.Tk()
    app = OpticaApp(ventana_principal)
    ventana_principal.mainloop()

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    main()
