from flet.controls.material import vertical_divider
from flet import VerticalAlignment
from tkinter.constants import CENTER
import flet as ft


def main(page: ft.Page) :
    texto_presentacion: type[str] = ft.Text("Esta será la pagina de Sign in")
    page.add(texto_presentacion)
    boton = ft.ElevatedButton("Boton prueba")
    page.add(
        ft.Column(
            boton,
            alignment= ft.MainAxisAlignment.END,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

ft.run(main)