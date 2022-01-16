from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        vl = BoxLayout(orientation = 'vertical')
        self.lbl = Label()
        vl.add_widget(self.lbl)

        hl1 = BoxLayout()
        btn1 = Button(text='1')
        btn2 = Button(text='2')
        btn3 = Button(text='3')
        btnplus = Button(text='+')
        hl1.add_widget(btn1)
        hl1.add_widget(btn2)
        hl1.add_widget(btn3)
        hl1.add_widget(btnplus)
        vl.add_widget(hl1)

        hl2 = BoxLayout()
        btn4 = Button(text='4')
        btn5 = Button(text='5')
        btn6 = Button(text='6')
        btnminus = Button(text='-')
        hl2.add_widget(btn4)
        hl2.add_widget(btn5)
        hl2.add_widget(btn6)
        hl2.add_widget(btnminus)
        vl.add_widget(hl2)

        hl3 = BoxLayout()
        btn7 = Button(text='7')
        btn8 = Button(text='8')
        btn9 = Button(text='9')
        btnU = Button(text='*')
        hl3.add_widget(btn7)
        hl3.add_widget(btn8)
        hl3.add_widget(btn9)
        hl3.add_widget(btnU)
        vl.add_widget(hl3)

        hl4 = BoxLayout()
        btnC = Button(text='C')
        btn0 = Button(text='0')
        btnR = Button(text='=')
        btnD = Button(text='/')
        hl4.add_widget(btnC)
        hl4.add_widget(btn0)
        hl4.add_widget(btnR)
        hl4.add_widget(btnD)
        vl.add_widget(hl4)

        btn1.on_press = lambda : self.AddSymbol('1')
        btn2.on_press = lambda : self.AddSymbol('2')
        btn3.on_press = lambda : self.AddSymbol('3')
        btn4.on_press = lambda : self.AddSymbol('4')
        btn5.on_press = lambda : self.AddSymbol('5')
        btn6.on_press = lambda : self.AddSymbol('6')
        btn7.on_press = lambda : self.AddSymbol('7')
        btn8.on_press = lambda : self.AddSymbol('8')
        btn9.on_press = lambda : self.AddSymbol('9')
        btn0.on_press = lambda : self.AddSymbol('0')
        btnplus.on_press = lambda : self.AddSymbol('+')
        btnminus.on_press = lambda : self.AddSymbol('-')
        btnU.on_press = lambda : self.AddSymbol('*')
        btnD.on_press = lambda : self.AddSymbol('/')
        btnR.on_press = self.Equal
        btnC.on_press = self.Clear
        self.add_widget(vl) # экран - это виджет, на котором могут создаваться все другие (потомки)

    def AddSymbol(self,s):
        self.lbl.text += s

    def Equal(self):
        self.lbl.text = str( eval(self.lbl.text))

    def Clear(self):
        self.lbl.text = self.lbl.text[0:-1]
        

    def next(self):
        self.manager.transition.direction = 'left' # объект класса Screen имеет свойство manager 
                                                   # - это ссылка на родителя
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        pass
        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        return sm

app = MyApp()
app.run()