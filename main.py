from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton

PATH = "api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
API = "api id"
import requests
import math



Screenhelper='''
ScreenManager:
    id:screen
    LoginScreen:
    MainScreen:
<LoginScreen>:
    name:'login'

    MDCard:
        id : box
        orientation: "vertical"
        padding: 25
        spacing: 20
        size_hint : None, None
        size: "200", "300"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        elevation: 25
        MDLabel:
            id: second_screen_label
            text:'Login'
            font_size: 30

            halign: 'center'
            size_hint_y: None
            padding_y: 30
            theme_text_color: "Secondary"
            adaptive_height: True

        MDTextField:
            id:nitin
            hint_text: "User Name"
            icon_right: "account"
            size_hint_x:None
            width:170
            font_size:15
            pos_hint:{"center_x":0.5}
        MDTextField:
            id: Password
            hint_text: "City"
            
            icon_right: "location"
            size_hint_x:None
            width:170
            font_size:15
            pos_hint:{"center_x":0.5, "center_y":0.7}
        MDRectangleFlatButton:
            text:'Sign up'
            font_size:12
            pos_hint:{"center_x":0.5}
            on_press:
                root.manager.current = 'main'
                app.check()
<MainScreen>:
    name:'main'
    MDLabel:
        id: greet
        text:"Greetings Nitin"
        font_style:"Body1"
        halign:"center"
        size_hint_y:None
        theme_text_color:"Secondary"
        pos_hint:{"center_x": 0.5, "center_y": 0.95}
    MDLabel:
        id:city
        text:"Nashik"
        font_style:"Subtitle2"
        halign:"center"
        size_hint_y:None
        theme_text_color:"Secondary"
        pos_hint:{"center_x": 0.5, "center_y": 0.85}
    MDLabel:
        id: temp
        text:"{tempindegree}°c"
        font_style:"H4"
        halign:"center"
        size_hint_y:None
        theme_text_color:"Secondary"
        pos_hint:{"center_x": 0.5, "center_y": 0.75}
    MDLabel:
        id:des
        text:"Discription : {discription}"
        font_style:"Subtitle2"
        halign:"center"
        size_hint_y:None
        theme_text_color:"Secondary"
        pos_hint:{"center_x": 0.5, "center_y": 0.6}
    MDLabel:
        id:wspeed
        text:"Wind Speed : {windspeed}"
        font_style:"Subtitle2"
        halign:"center"
        size_hint_y:None
        theme_text_color:"Secondary"
        pos_hint:{"center_x": 0.5, "center_y": 0.55}
    MDLabel:
        id:state
        text:"Weather : {mainstate}"
        font_style: "Subtitle2"
        halign: "center"
        size_hint_y: None
        theme_text_color: "Secondary"
        pos_hint : {"center_x":0.5, "center_y":0.65}
    Image:
        source: 'autumn-removebg-preview.png'
        size_hint: None, None
        size: 650, 2050
        pos_hint: {"center_x":0.5, "center_y":0.26}
    
'''
class LoginScreen(Screen):

    pass
class MainScreen(Screen):
    pass


sm =ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MainScreen(name='main'))



class DemoApp(MDApp):
    name = None
    city =None
    def build(self):

        self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.primary_hue = "A700"


        self.KIII = Builder.load_string(Screenhelper)

        return self.KIII


    def check(self):
        param = {
            "q": self.KIII.get_screen("login").ids.Password.text,
            "appid": API
        }

        weath = requests.get("http://api.openweathermap.org/data/2.5/weather?", params=param)
        response = weath.json()
        self.root.get_screen("main").ids.greet.text =f"Greetings {self.KIII.get_screen('login').ids.nitin.text}"
        tempindegree = math.floor(response['main']['temp'] - 273.15)
        discription = response['weather'][0]['description']
        windspeed = response['wind']['speed']
        mainstate = response['weather'][0]['main']
        self.root.get_screen("main").ids.temp.text = f"{tempindegree}°c"
        self.root.get_screen("main").ids.des.text = f"Discription : {discription}"
        self.root.get_screen("main").ids.state.text = f"Weather : {mainstate}"
        self.root.get_screen("main").ids.wspeed.text = f"Wind speed : {windspeed}"

        self.KIII.get_screen("login").ids.Password.text
        self.root.get_screen("main").ids.city.text = self.KIII.get_screen("login").ids.Password.text





DemoApp().run()
