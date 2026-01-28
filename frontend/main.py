import flet as ft
from pages import HomePage, SolarPage, WindPage

class AppRouter:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.routes = {
            '/': HomePage,
            '/solar': SolarPage,
            '/wind': WindPage
        }

    async def handle_route(self, route: str):
        self.page.views.clear()

        page_class = self.routes.get(route)
        if page_class is None:
            return

        page_instance = page_class(self.page)
        view = await page_instance.build()

        self.page.views.append(view)
        self.page.update()


async def main(page: ft.Page):
    page.title = 'Калькулятор окупаемости домашней энерго-станции'
    page.theme_mode = ft.ThemeMode.LIGHT

    page.window.max_width = 460
    page.window.max_height = 650
    await page.window.center()


    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    router = AppRouter(page)

    async def route_change(e: ft.RouteChangeEvent):
        await router.handle_route(e.route)

    page.on_route_change = route_change

    await router.handle_route(page.route)


if __name__ == '__main__':
    ft.run(main)

