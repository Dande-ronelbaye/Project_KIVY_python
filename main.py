import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols=2

        self.add_widget(Label(text="Frist name: "))
        self.name =TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Last Name: "))
        self.LastName = TextInput(multiline=False)
        self.add_widget(self.LastName)

        self.add_widget(Label(text="email: "))
        self.Email = TextInput(multiline=False)
        self.add_widget(self.Email)


class MyApp(App):
    def build(self):
        return MyGrid()
if __name__=="__main__":
    MyApp().run()