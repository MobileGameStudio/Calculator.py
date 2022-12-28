from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Set the app size
Window.size = (400, 600)


class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.solution = TextInput(text="0", multiline=False, readonly=False, halign="right", font_size=40, input_filter="float")
        main_layout.add_widget(self.solution)
        buttons = [
            ["CE", "<-"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "=", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=30, color='white', pos_hint={"center_x": 0.5, "center_y": 0.5})
                button.bind(on_press=self.button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        # return a Button() as a root widget
        return main_layout

    def button_press(self, instance):
        if instance.text == "<-":
            self.solution.text = self.solution.text[:-1]
        elif instance.text == "CE":
            self.solution.text = "0"
        elif self.solution.text == '0':
            self.solution.text = ''
            self.solution.text = f'{instance.text}'
        elif instance.text == "=":
            try:
                self.solution.text = str(eval(self.solution.text))
            except:
                self.solution.text = "Error"
        else:
            self.solution.text += instance.text



if __name__ == '__main__':
    MainApp().run()
