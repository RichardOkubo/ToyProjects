from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MyBoxLayout(BoxLayout):
    ...


class Exemplo_3App(App):  # Começa com 'Exemplo_3' como o arquivo .kv
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    Exemplo_3App().run()
