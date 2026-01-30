import flet as ft
from pages import BasePage


class WindPage(BasePage):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)

    # ЭТО ОБЯЗАТЕЛЬНО НУЖНО НАПИСАТЬ
    async def build(self) -> ft.View:
        return ft.View(
            route='/wind', # Это route твоей страницы из main.py
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=self.get_content()
        )

    # Эта функция для отображения всех элементов твоей страницы
    def get_content(self) -> list[ft.BaseControl]:
        return [
            ft.Column(
                controls=[
                    ft.Text("Ветреная электростанция")
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]
