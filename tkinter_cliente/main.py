from Formulario import Formulario

# ****** Código Principal ******
if __name__ == "__main__":
    objFormulario = Formulario()
    auxFormulario = objFormulario.iniciar_ventana()
    objFormulario.iniciar_preguntas()
    auxFormulario.mainloop()
