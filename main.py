import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from Tokenizer import Tokenizer
from result import Result
from kivy.uix.screenmanager import ScreenManager, Screen
import tkinter as tk
from tkinter import filedialog
from kivy.config import Config
import numpy as np
from Parser import Parser
import re


class MyApp(App):

    def build(self):
        self.tokenizer = Tokenizer()
        layout = GridLayout(cols=1)
        layout_header = GridLayout(cols=2, size_hint_y=None, height=60)
        layout_header.add_widget(Label(text='Insert code:'))
        btn_import = Button(text="Import file", size_hint_x=None, width=150)
        btn_import.bind(on_press=self.readFile)
        layout_header.add_widget(btn_import)
        self.textinput = TextInput()
        layout.add_widget(layout_header)
        layout.add_widget(self.textinput)
        self.btn = Button(text="Process", size_hint_y=None, height=100)
        layout.add_widget(self.btn)
        self.btn.bind(on_press=self.tokenize)

        self.screen_manager = ScreenManager()

        self.connect_page = layout
        screen = Screen(name='main_screen')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.result_page = Result([], self.screen_manager)
        screen = Screen(name='result')
        screen.add_widget(self.result_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def tokenize(self, instance):
        text = self.textinput.text.strip()
        if len(text) == 0:
            popup = Popup(title='No code', content=Label(text='Please insert the code!'),
                          auto_dismiss=True, size_hint=(None, None), size=(200, 100))
            popup.open()
        else:
            res = self.tokenizer.tokenize(text)
            result = res[0]
            txt = res[1]
            if len(result) != 0 and len(txt.strip()) == 0:
                tokens = []
                for x in result:
                    if x[1] == 'comment':
                        text = text.replace(x[0], '')
                    else:
                        tokens.append(x)
                text = text.replace('\n', '')
                text = re.sub(r'\s+', ' ', text)
                try:
                    parser = Parser(tokens, text)
                    res_parse = parser.parse()
                    root_node = res_parse[0]
                    num_tokens_left = res_parse[1]
                    if num_tokens_left != 0:
                        raise Exception('There is a syntax error!')
                    self.result_page.update_info(result, root_node)
                    self.screen_manager.current = "result"
                except Exception as e:
                    popup = Popup(title='Syntax error', content=Label(text=str(e)),
                                  auto_dismiss=True, size_hint=(None, None), size=(500, 100))
                    popup.open()

            else:
                popup = Popup(title='Lexical error', content=Label(text='There is a lexical error!'),
                              auto_dismiss=True, size_hint=(None, None), size=(500, 100))
                popup.open()

    def readFile(self, instance):
        try:
            root = tk.Tk()
            root.withdraw()

            file_path = filedialog.askopenfilename(
                title="Select file", filetypes=(("AMLL Files", "*.amll"),))
            f = open(file_path, "r")
            self.textinput.text = f.read()
        except:
            pass


if __name__ == '__main__':
    Config.set('graphics', 'height', '800')
    Config.set('graphics', 'width', '1500')
    Config.window_icon = 'icon.ico'
    MyApp().run()
