from kivy.app import App
from kivy.uix.button import Button
class MyApp(App):
    def build(self):
        return Button(text="Olá mundo! Esse é o meu primeiro programa em Kivy \n Eu sou estudante Sesiano ")
if __name__ == '__main__':
    MyApp().run()