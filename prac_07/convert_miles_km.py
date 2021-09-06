from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_IN_KM = 1.60934


class ConvertMilesToKM(App):
    km_output = StringProperty()

    def build(self):
        """Build app in window 500x200"""
        self.title = "Convert Miles to KM"
        Window.size = (500, 200)
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def validate_number(self):
        """Validates and returns 0.0 if not a valid number"""
        if self.root.ids.miles_input.text == '':
            return 0.0
        else:
            try:
                value = float(self.root.ids.miles_input.text)
                return value
            except ValueError:
                return 0.0

    def handle_increment(self, number):
        """increment the user input number by 1 or -1 based on button selection"""
        number_to_increment = self.validate_number()
        self.root.ids.miles_input.text = str(number_to_increment + number)

    def km_conversion(self):
        """Convert input miles to KM based on 1 mile = 1.60934"""
        miles = self.validate_number()
        kilometers = miles * MILES_IN_KM
        self.root.ids.km_output.text = str(kilometers)


ConvertMilesToKM().run()
