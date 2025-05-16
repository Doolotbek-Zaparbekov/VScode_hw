import flet as ft
from database import Database
def main(page: ft.Page):
    page.title = "Учет расходов"
    page.data = 0
    db = Database("expenses.sqlite3")
    db.create_tables()
    def add_todo(e):
        todo = f"Расход: {cause.value}/сумма: {quantity.value}"
        todo_list_area.controls.append(ft.Text(value=todo, size=20))
        page.data += int(quantity.value)
        quantity.value = ""
        cause.value = ""
        consumption.value = f"Общая сумма расходов: {page.data}"
        page.update()
    consumption = ft.Text(value=f"Общая сумма расходов {page.data}", size=25)
    page.update()
    title = ft.Text(value="Ваши расходы", size=33)
    cause = ft.TextField(label="Название расхода")
    quantity = ft.TextField(label="Сумма расхода")
    add_button = ft.ElevatedButton("Добавить", on_click=add_todo)
    form_area = ft.Row(controls=[cause, quantity, add_button])
    todo_list_area = ft.Column()
    page.add(title, form_area, consumption, todo_list_area)
ft.app(main)