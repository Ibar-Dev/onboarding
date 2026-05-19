from flet import TextField
import flet as ft

def acceder_a_login(page: ft.Page):
    page.controls.clear()

    page.add(
        ft.Column(
            [
                ft.Text("Inicia tu sesion", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(
                    ft.Column(
                    
                        [
                        ft.TextField(label="Usuario"),
                        ft.TextField(label="Contraseña", password=True)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment= ft.CrossAxisAlignment.CENTER
                        ),
                        expand=True
                ),
            ],
            expand= True,
            alignment= ft.MainAxisAlignment.START,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()

    