import flet as ft
def main(page: ft.Page):
    page.title = "Учет расходов"
    title = ft.Text(value="Выши расходы", size=33)
    cause = ft.TextField(label="Название расхода")
    quantity = ft.TextField(label="Сумма рвсхода")
    add_button = ft.ElevatedButton("Добавить")
    page.add(title, cause, quantity, add_button)
ft.app(main)