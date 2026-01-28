import flet as ft
from pages import BasePage

class HomePage(BasePage):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)

        self.station_type = None
        self.station_dropdown = ft.Dropdown(
            label='Выбери тип электростанции',
            value='solar',
            options=[
                ft.DropdownOption(key='solar', text='Солнечная'),
                ft.DropdownOption(key='wind', text='Ветреная'),
                ft.DropdownOption(key='all', text='Обе'),
            ],
            width=320,
            on_text_change=self.on_station_change
        )

        self.continue_button = ft.ElevatedButton(
            "Продолжить",
            width=320,
            height=45,
            on_click=self.on_continue,
        )

    async def build(self) -> ft.View:
        return ft.View(
            route='/',
            controls=self.get_content()
        ) 
    
    def get_content(self) -> list[ft.BaseControl]:
        return [
            ft.Column(
                controls=[
                    ft.Text("Выбери тип станции"),
                    self.station_dropdown,
                    self.continue_button
                ]
            )
        ]
    
    def on_station_change(self, e: ft.Event[ft.Dropdown]):
        self.station_type = e.control.value


    async def on_continue(self):
        if not self.station_type:
           self.page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("Ошибка"),
                    content=ft.Text("Пожалуйста, выберите тип электростанции")
                )
            )
           
           return

        if self.station_type == 'solar':
            self.page.go('/solar')

        if self.station_type == 'wind':
            self.page.go('/wind')