import flet as ft
from pages import BasePage


class BothPage(BasePage):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)

    async def build(self) -> ft.View:
        return ft.View(
            route='/both'
        )
    
    def get_content(self) -> list[ft.BaseControl]:
        return [
            ft.Column(
                controls=[
                    
                ]
            )
        ]