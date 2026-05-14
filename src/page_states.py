import flet as ft

def acceder_a_login(page: ft.Page):
    page.controls.clear()
    page.vertical_alignment = ft.MainAxisAlignment.START

    Texto_login = ft.Text("Inicia tu sesion", size=24, weight=ft.FontWeight.BOLD, )
    page.add(Texto_login)
    page.add(escribir_usuario(page))


    page.update()

def escribir_usuario(page:ft.Page):
    page.horizontal_alignment= ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    ft.TextField(label="Usuario")

    pass