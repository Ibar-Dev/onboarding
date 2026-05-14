import flet as ft

def main(page: ft.Page):
    # Configuramos la alineación de la página para centrar el contenido
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Creamos un control de texto con formato de título y lo agregamos a la página

    titulo = ft.Text("Bienvenid@ a este Onbording", size=32, weight=ft.FontWeight.BOLD)
    page.add(titulo)

    boton_entrada = ft.Button(
        "Acceder"
    )
    page.add(boton_entrada)

ft.app(target=main)
    
