import reflex as rx


class State(rx.State):
    """The app state."""

    count: int = 0

    @rx.event
    def increment(self):
        """Increment the count."""
        self.count += 1

    @rx.event
    def decrement(self):
        """Decrement the count."""
        self.count -= 1


def index() -> rx.Component:
    """The main page of the app."""
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Interactive Button", class_name="text-3xl font-bold text-gray-900"
                ),
                rx.el.p(
                    "A simple demonstration of a stateful button in Reflex.",
                    class_name="text-gray-500 mt-1 font-medium",
                ),
                class_name="mb-8 text-center",
            ),
            rx.el.div(
                rx.el.p(
                    "Current Count:", class_name="text-lg font-medium text-gray-700"
                ),
                rx.el.p(
                    State.count,
                    class_name="text-7xl font-extrabold text-blue-600 tracking-tighter",
                ),
                class_name="flex flex-col items-center gap-2 my-8",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("minus", class_name="w-5 h-5"),
                    "Decrement",
                    on_click=State.decrement,
                    class_name="flex items-center justify-center gap-2 px-6 py-3 bg-red-500 text-white font-semibold rounded-xl shadow-sm hover:bg-red-600 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-red-400 focus:ring-offset-2",
                ),
                rx.el.button(
                    rx.icon("plus", class_name="w-5 h-5"),
                    "Increment",
                    on_click=State.increment,
                    class_name="flex items-center justify-center gap-2 px-6 py-3 bg-blue-500 text-white font-semibold rounded-xl shadow-sm hover:bg-blue-600 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-offset-2",
                ),
                class_name="flex items-center justify-center gap-4",
            ),
            class_name="bg-white p-8 md:p-12 rounded-2xl border border-gray-200 shadow-sm w-full max-w-lg",
        ),
        class_name="min-h-screen bg-gray-50 flex items-center justify-center p-4 font-['Inter'] **:border-gray-200",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400..700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)