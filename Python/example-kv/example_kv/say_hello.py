from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class MyBoxLayout(BoxLayout):
    username = ''
    greets = StringProperty('')

    def greeting(self, *args):
        if self.username == '':
            self.greets = 'Hi!'
        else:
            self.greets = f'Hello, {self.username}!'


class Say_HelloApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    Say_HelloApp().run()
