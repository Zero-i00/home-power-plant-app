import flet as ft
from pages import BasePage


class SolarPage(BasePage):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)

    # ЭТО ОБЯЗАТЕЛЬНО НУЖНО НАПИСАТЬ
    async def build(self) -> ft.View:
        return ft.View(
            route='/solar', # Это route твоей страницы из main.py
            controls=self.get_content()
        )
    
    # Эта функция для отображения всех элементов твоей страницы
    def get_content(self) -> list[ft.BaseControl]:
        return [
            ft.Column(
                controls=[
                    ft.Text("Солнечная электростанция")
                ]
            )
        ]
