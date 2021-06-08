from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.toast import toast

from core.core import engine, market_basket_table, select

class RV(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = self.load_db()

    def load_db(self):
        return [
            {'text': str(register)}
            for register in [
                register[1:]
                for register in select([market_basket_table]).execute()]]


class InWindow(Screen):
    product = StringProperty("")
    price = StringProperty("")
    quantity = StringProperty("")
    market = StringProperty("")


class OutWindow(Screen):
    ...


class WindowManager(ScreenManager):
    __price = None

    def commit(self):
        _in = self.get_screen('in')
        _out = self.get_screen('out')
        _rv = _out.children[0].children[1]

        try:
            self.__price = float(_in.price)
        except Exception as e:
            #toast("Erro")
            ...
        else:
            with engine.begin() as connection:
                connection.execute(
                    market_basket_table.insert(),
                    [{
                        "market": _in.market,
                        "product": _in.product,
                        "price": self.__price,
                        "quantity": _in.quantity
                    }])

            _rv.data.append(
                {"text": str(select([market_basket_table])
                    .order_by(market_basket_table.c.id.desc())
                    .execute()
                    .first()[1:])
            })
            _rv.refresh_from_data()

            _textinputs = [
                child for child in _in.children[0].children if isinstance(child, TextInput)]

            for i, _ in enumerate(_textinputs):
                if i != 0:
                    _textinputs[i].text = ""
            #toast("Success")
            
    def quit(self):
    	exit()


class MainApp(App):
    def build(self):
        return Builder.load_file('../lang/app.kv')


MainApp().run()
