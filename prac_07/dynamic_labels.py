from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names_list = ["Jeff", "Ling", "Max", "Squall", "Sarah"]


DynamicLabels().run()