import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyPyApp(App):
    def build(self):
        return Label(text="My First App")
    
if __name__ == "__main__":
    MyPyApp().run()
