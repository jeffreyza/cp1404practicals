from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names_list = ["Jeff", "Ling", "Max", "Squall", "Sarah"]

    def build(self):
        """Build and display program"""
        self.title = "Dynamic Name Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Loop through names list and add as label"""
        for name in self.names_list:
            self.root.ids.main.add_widget(Label(text=name))
        return


DynamicLabels().run()
