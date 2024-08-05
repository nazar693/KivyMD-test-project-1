from kivymd.app import MDApp
from kivy.lang import Builder

class LoginApp(MDApp):
    def build(self):
        return Builder.load_file("Main.kv")

if __name__ == "__main__":
    LoginApp().run()