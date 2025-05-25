import flet as ft
from database import Database


def main(page: ft.Page):
    page.title = "Учет расходов"
    db = Database("expense.sqlite3")
    db.create_tables()

    def refresh_todo_list():
        todo_list_area.controls.clear()
        for expense in db.get_all_expenses():
            expense_id, cause_text, quantity_val = expense
            todo_row = ft.Row(
                [
                    ft.Text(value=f"Расход: {cause_text} / сумма: {quantity_val}", size=20, expand=True),
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        icon_color="red",
                        tooltip="Удалить",
                        on_click=lambda e, id=expense_id: delete_todo(e, id),
                    ),
                ]
            )
            todo_list_area.controls.append(todo_row)
        update_total_expense()

    def add_todo(e):
        if cause.value and quantity.value.isdigit():
            db.add_expense(cause.value, int(quantity.value))
            cause.value = ""
            quantity.value = ""
            refresh_todo_list()
            page.update()

    def delete_todo(e, expense_id):
        db.delete_expense(expense_id)
        refresh_todo_list()
        page.update()

    def update_total_expense():
        total = db.get_total_expense()
        consumption.value = f"Общая сумма расходов: {total}"

    consumption = ft.Text(value="Общая сумма расходов: 0", size=25)
    title = ft.Text(value="Ваши расходы", size=33)
    cause = ft.TextField(label="Название расхода")
    quantity = ft.TextField(label="Сумма расхода")
    add_button = ft.ElevatedButton("Добавить", on_click=lambda e: add_todo(e))
    form_area = ft.Row(controls=[cause, quantity, add_button])
    todo_list_area = ft.Column(scroll=ft.ScrollMode.AUTO,height=400)
    page.add(title, form_area, consumption, todo_list_area)
    refresh_todo_list()


ft.app(main)