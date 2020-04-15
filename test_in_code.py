from kivymd.app import MDApp

from bidi.algorithm import get_display
import arabic_reshaper

from mdtextfield import MDTextFieldPersian


class MainApp(MDApp):
    def build(self):
        return MDTextFieldPersian(
        	font_name="font/iransans.ttf", 
        	halign="center",
        	pos_hint={"center_x":0.5, "center_y":0.5})


MainApp().run()