import tkinter as Ventana

class Formulario:
    def __init__(self):
        self.colorRojo = "red"
        self.colorAmarillo = "yellow"
        
        self.entryNombre = None
        self.entryApellido = None
        self.entryCedula = None
        self.entryCorreo = None
        self.entryTelefono = None
        
        self.labelResultado = None
        self.formulario = None
        
        self.base_datos_clientes = []

    def iniciar_ventana(self):
        self.formulario = Ventana.Tk()
        self.formulario.title("Registro de Cliente")
        self.formulario.geometry("600x700")
        self.formulario.resizable(False, False)
        self.formulario.configure(bg=self.colorRojo)
        return self.formulario

    def crear_campo(self, texto_label):
        label = Ventana.Label(self.formulario, text=texto_label)
        label.configure(bg=self.colorAmarillo, fg=self.colorRojo, font=("Arial", 12, "bold"))
        label.configure(borderwidth=2, relief="raised", width=30)
        label.pack(padx=5, pady=5)
        
        entry = Ventana.Entry(self.formulario)
        entry.configure(bg="white", fg="black", font=("Arial", 12), width=30)
        entry.pack(padx=5, pady=5)
        return entry

    def iniciar_preguntas(self):
        self.entryNombre = self.crear_campo("Digite el nombre:")
        self.entryApellido = self.crear_campo("Digite el apellido:")
        self.entryCedula = self.crear_campo("Digite la cédula:")
        self.entryCorreo = self.crear_campo("Digite el correo electrónico:")
        self.entryTelefono = self.crear_campo("Digite el teléfono:")

        botonEnviar = Ventana.Button(self.formulario, text="Enviar Registro", font=("Arial", 14, "bold"), 
                                     command=self.funcion_general_procesar)
        botonEnviar.configure(bg="blue", fg=self.colorAmarillo, width=20, cursor="hand2")
        botonEnviar.pack(padx=20, pady=20)
        
        self.labelResultado = Ventana.Label(self.formulario, text="")
        self.labelResultado.configure(font=("Arial", 12, "bold"), width=50, height=4)
        self.labelResultado.pack(padx=10, pady=10)

    def funcion_general_procesar(self):
        if self.validar_campos_llenos():
            datos = self.tomar_datos()
            self.almacenar_en_arreglo(datos)
            self.imprimir_datos("¡Registro Exitoso! Campos válidos y diligenciados.", exitoso=True)
            self.limpiar_campos()
        else:
            self.imprimir_datos("Error: Todos los campos deben estar diligenciados (no vacíos).", exitoso=False)

    def validar_campos_llenos(self):
        if (not self.entryNombre.get().strip() or 
            not self.entryApellido.get().strip() or 
            not self.entryCedula.get().strip() or 
            not self.entryCorreo.get().strip() or 
            not self.entryTelefono.get().strip()):
            return False
        return True

    def tomar_datos(self):
        return [
            self.entryNombre.get().strip(),
            self.entryApellido.get().strip(),
            self.entryCedula.get().strip(),
            self.entryCorreo.get().strip(),
            self.entryTelefono.get().strip()
        ]

    def almacenar_en_arreglo(self, datos_cliente):
        self.base_datos_clientes.append(datos_cliente)
        print(f"Base de datos actual (Arreglo): {self.base_datos_clientes}")

    def imprimir_datos(self, mensaje, exitoso):
        if exitoso:
            self.labelResultado.configure(text=mensaje, bg="green", fg="white")
        else:
            self.labelResultado.configure(text=mensaje, bg="yellow", fg="red")

    def limpiar_campos(self):
        self.entryNombre.delete(0, Ventana.END)
        self.entryApellido.delete(0, Ventana.END)
        self.entryCedula.delete(0, Ventana.END)
        self.entryCorreo.delete(0, Ventana.END)
        self.entryTelefono.delete(0, Ventana.END)
