import flet as ft
from pages import BasePage
from api.client import APIClient
from services.city import city_service
from services.calculation import calculation_service
from schemas.calculation import CalculationSolarPanelIn


class SolarPage(BasePage):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)
        self.city_dropdown = ft.Dropdown(
            label="Город",
            width=320,
        )

        self.sist_kpd_field = ft.TextField(
            label="КПД Системы",
            width=320,
            input_filter=ft.InputFilter(regex_string=r"[0-9.]", allow=True),
        )

        self.price_sun = ft.TextField(
            label="Стоимость установки",
            width=320,
            input_filter=ft.InputFilter(regex_string=r"[0-9.]", allow=True),
        )


        self.panel_power = ft.TextField(
            label="Мощность панели (кВт*ч)",
            width=320,
            input_filter=ft.InputFilter(regex_string=r"[0-9.]", allow=True),
        )

        self.price_energy_sun = ft.TextField(
            label="Стоимость энергии",
            width=320,
            input_filter=ft.InputFilter(regex_string=r"[0-9.]", allow=True),
        )

        self.continue_button = ft.ElevatedButton(
            "Продолжить",
            width=320,
            height=45,
            on_click=self.on_continue,
        )


    async def load_cities(self):
        client = APIClient()
        try:
            cities = await city_service.list(client)
            self.city_dropdown.options = [
                ft.dropdown.Option(key=str(city.id), text=city.name)
                for city in cities
            ]
        finally:
            await client.close()

    async def build(self) -> ft.View:
        await self.load_cities()
        return ft.View(
            route='/solar',
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=self.get_content()
        )

    def get_content(self) -> list[ft.BaseControl]:
        return [
            ft.Column(
                controls=[
                    ft.Text("Солнечная электростанция"),
                    self.city_dropdown,
                    self.sist_kpd_field,
                    self.panel_power,
                    self.price_sun,
                    self.price_energy_sun,
                    self.continue_button

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]

    
    async def on_continue(self, e):
        fields = [
            (self.city_dropdown, "Выберите город"),
            (self.sist_kpd_field, "Введите КПД Системы"),
            (self.panel_power, "Введите мощность панели"),
            (self.price_sun, "Введите стоимость установки"),
            (self.price_energy_sun, "Введите стоимость энергии"),
        ]

        has_error = False
        for field, error_text in fields:
            if not field.value:
                field.error_text = error_text
                has_error = True
            else:
                field.error_text = None

        self.page.update()

        if has_error:
            return

        data = CalculationSolarPanelIn(
            city_id=int(self.city_dropdown.value),  # type: ignore[arg-type]
            sist_kpd=float(self.sist_kpd_field.value),  # type: ignore[arg-type]
            panel_power=float(self.panel_power.value),  # type: ignore[arg-type]
            price_sun=float(self.price_sun.value),  # type: ignore[arg-type]
            price_energy_sun=float(self.price_energy_sun.value),  # type: ignore[arg-type]
        )
        client = APIClient()
        try:
            result = await calculation_service.calculate_solar(client, data)
            print(result)
        finally:
            await client.close()