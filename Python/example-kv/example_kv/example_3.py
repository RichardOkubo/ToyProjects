from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class MyBoxLayout(BoxLayout):
    propriedade = StringProperty('0')

    def mudar(self, *args):
        self.propriedade = '10'

    def request(self, *args):
        def on_success(req, response):
            self.propriedade = str(response)

        def on_error(req, response):
            self.propriedade = f'Error! {response}'

        def on_failure(req, response):
            self.propriedade = f'Fail! {response}'

        self.request = UrlRequest(
            'https://pokeapi.co/api/v2/pokemon/ditto',
            on_success=on_success,
            on_error=on_error,
            on_failure=on_failure,
            verify=False
        )
        
        print(self.request)


class Example_3App(App):  # Começa com 'Example_3' como o arquivo .kv
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    Example_3App().run()
