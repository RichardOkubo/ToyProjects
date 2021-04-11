from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MyBoxLayout(BoxLayout):
    ...


class Example_2App(App):  # Começa com 'Example_2' como o arquivo .kv
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    Example_2App().run()
