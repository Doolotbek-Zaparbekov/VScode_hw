import flet as ft
from database import Database
def main(page: ft.Page):
    page.title = "Учет расходов"
    page.data = 0
    db = Database("expense.sqlite3")
    db.create_tables()
    def delete_todo(e, expense_id):
        db.delete_expense(expense_id)
        refresh_todo_list()
    def refresh_todo_list():
        todo_list_area.controls.clear()
        for expense in db.get_all_expenses():
            expense_id, cause_text, quantity_val = expense
            todo_row = ft.Row([
                ft.Text(value=f"Расход: {cause_text} / сумма: {quantity_val}", size=20, expand=True),
                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color="red",
                    tooltip="Удалить",
                    on_click=lambda e, id=expense_id: delete_todo(e, id)
                )
            ])
            todo_list_area.controls.append(todo_row)
            page.data += int(quantity_val)
        consumption.value = f"Общая сумма расходов: {page.data}"
        page.update()
    def add_todo(e):
        refresh_todo_list()
        db.add_expense(cause.value, quantity.value)
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
    refresh_todo_list()
    page.add(title, form_area, consumption, todo_list_area)
ft.app(main)