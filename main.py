from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.uix.screenmanager import (Screen, ScreenManager, ScreenManagerException,
           TransitionBase, ShaderTransition, SlideTransition,
           SwapTransition, FadeTransition, WipeTransition,
           FallOutTransition, RiseInTransition, NoTransition,
           CardTransition)

from backend.start_pages.create_user import check_user_create_values
from backend.start_pages.login_user import check_user_login_values
from backend.main_pages.kahoot import kahoot


Window.size = (400,450)

class MainPage(Screen):
    pass

class LoginUser(Screen):
    pass

class CreateUser(Screen):
    pass

class KahootPage(Screen):
    pass


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def build(self):
        # self.fps_monitor_start()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = "200"

        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.accent_hue = "200"
        
        Builder.load_file("frontend/build.kv")
        screen_manager = ScreenManager(transition = RiseInTransition())
    
        screen_manager.add_widget(LoginUser(name="Login_User"))
        screen_manager.add_widget(CreateUser(name="Create_User"))
        
        screen_manager.add_widget(MainPage(name="Main_Page"))
        screen_manager.add_widget(KahootPage(name="Kahoot_Page"))
        
        
            
        return screen_manager
            
            
    def start_user_screen(self):
        # email = self.root.ids.email.text
        current_screen = self.root.current
        if current_screen in ["Create_User", "Login_User"]: 
                
            email = self.root.get_screen(current_screen).ids['email'].text # same for both login+create screens
            password = self.root.get_screen(current_screen).ids['password'].text
            
            if current_screen == "Create_User":
                # phone_number = self.root.get_screen(current_screen).ids['phone_number'].text # only used in create user screen  
                phone_number = 0      
                check_user_create_values(email, password, phone_number, self.root)
                
            else:
                if check_user_login_values(email, password):
                    self.root.get_screen(current_screen).ids['email'].text = "" # same for both login+create screens
                    self.root.get_screen(current_screen).ids['password'].text = "" 
                    self.root.current = "Main_Page"
                    toast("Successful Login.")
                    
        else:
            if current_screen == "Kahoot_Page":
                toast("Sending Bots...")
                game_pin = self.root.get_screen(current_screen).ids['gamepin'].text
                bot_names = self.root.get_screen(current_screen).ids['botnames'].text
                
                if game_pin is not None and (bot_names is not None):               
                    kahoot(game_pin, bot_names)
    
    
MainApp().run()