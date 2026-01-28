import flet as ft

class BasePage:
    def __init__(self, page: ft.Page) -> None:
        self.page = page

    async def build(self) -> ft.View:
        raise NotImplementedError("Метод build должен быть реализован")
