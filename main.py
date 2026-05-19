import flet as ft
import src.page_states as pagestate



def main(page: ft.Page):
    # Configuramos la alineación de la página para centrar el contenido
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Creamos un control de texto con formato de título y lo agregamos a la página

    titulo = ft.Text("Bienvenid@ a este Onbording", size=32, weight=ft.FontWeight.BOLD)
    page.add(titulo)

    boton_entrada = ft.Button(
        "Acceder",
        on_click= lambda e: pagestate.acceder_a_login(page)
    )
    page.add(boton_entrada)
    

    

ft.app(target=main)
    
