
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
import tkinter as tk
from kivy.uix.popup import Popup
from tkinter import filedialog
import pandas as pd
from Node import Node
from graphviz import Source


class Result(BoxLayout):
    def __init__(self, data, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.orientation = "vertical"
        self.screen_manager = screen_manager

        self.return_b = Button(text="Go back", size_hint_x=None, width=150)
        self.return_b.bind(on_press=self.return_screen)
        self.btn_generate_tree = Button(
            text="Generate tree", size_hint_x=None, width=150)
        self.btn_generate_tree.bind(on_press=self.generate_tree)
        self.btn_download = Button(
            text="Save CSV", size_hint_x=None, width=150)
        self.btn_download.bind(on_press=self.save_file)
        self.layout_header = GridLayout(cols=4, size_hint_y=None, height=60)
        self.layout_header.add_widget(self.return_b)
        self.layout_header.add_widget(Label(text='Result'))
        self.layout_header.add_widget(self.btn_generate_tree)
        self.layout_header.add_widget(self.btn_download)

        self.contend_scroll_view = GridLayout(
            size_hint_y=None, row_default_height=60, cols=4)
        self.contend_scroll_view.bind(
            minimum_height=self.contend_scroll_view.setter('height'))

        self.update_info(self.data, Node('None'))

        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.contend_scroll_view)

        self.add_widget(self.layout_header)
        self.add_widget(self.scroll_view)

    def update_info(self, data, root_node):
        self.data = data
        self.num_aux = 0
        self.root_node = root_node
        self.contend_scroll_view.clear_widgets()
        self.contend_scroll_view.add_widget(Label(text='Lexeme'))
        self.contend_scroll_view.add_widget(Label(text='Token category'))
        self.contend_scroll_view.add_widget(Label(text='Token'))
        self.contend_scroll_view.add_widget(
            Label(text='Position first character'))
        for r in self.data:
            for c in r:
                self.contend_scroll_view.add_widget(Label(text=str(c)))

    def return_screen(self, instance):
        self.screen_manager.current = "main_screen"

    def save_file(self, instance):
        try:
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))

            path = file_path.strip()
            df = pd.DataFrame(self.data, columns=[
                              'lexeme', 'token_category', 'token', 'pos_first_char'])
            df.to_csv(path, index=False)

            popup = Popup(title='Save CSV', content=Label(text='File saved!'),
                          auto_dismiss=True, size_hint=(None, None), size=(200, 100))
            popup.open()
        except:
            pass

    def generate_tree(self, instance):
        txt = 'n'+str(self.root_node.code) + \
            ' [label='+str(self.root_node.name)+'];'
        for child in self.root_node.children:
            txt += self.printNode(child, self.root_node)
        txt = 'digraph G{'+txt+'}'

        try:
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png", filetypes=(("PNG", "*.png"), ("All Files", "*.*")))

            path = file_path.strip().split('.')[0]

            s = Source(txt, filename=path, format="png")
            s.view()

            popup = Popup(title='Save Tree', content=Label(text='File saved!'),
                          auto_dismiss=True, size_hint=(None, None), size=(200, 100))
            popup.open()
        except Exception as e:
            print(e)
            pass

    def printNode(self, node, parent):
        txt = 'n'+str(parent.code)+'->'+('n'+str(node.code))+";"
        if len(node.children) == 0:
            txt += ('n'+str(node.code)) + '[label="'+str(node.name) + \
                '" style=filled color="dodgerblue" fillcolor="lightyellow"];'
        else:
            txt += ('n'+str(node.code)) + '[label="'+str(node.name)+'"];'
            for child in node.children:
                txt += self.printNode(child, node)
        return txt
