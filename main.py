from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import os

# Dummy function for ML model prediction
def predict_hemoglobin(image_path, method):
    # Replace with your ML model inference
    if method == "flashlight":
        return 13.5
    elif method == "nail":
        return 12.8
    return None

# Home screen
class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text="Hemoglobin Level Detection", font_size="20sp", bold=True, size_hint=(1, 0.2)))

        self.flashlight_btn = Button(
            text="Detect with Flashlight", size_hint=(1, 0.3), background_color=(0, 0.7, 0.9, 1)
        )
        self.flashlight_btn.bind(on_press=self.detect_with_flashlight)
        self.add_widget(self.flashlight_btn)

        self.nail_btn = Button(
            text="Detect with Nail Image", size_hint=(1, 0.3), background_color=(0.8, 0.2, 0.6, 1)
        )
        self.nail_btn.bind(on_press=self.detect_with_nail)
        self.add_widget(self.nail_btn)

        self.result_label = Label(text="", size_hint=(1, 0.2))
        self.add_widget(self.result_label)

    def detect_with_flashlight(self, instance):
        self.open_file_chooser("flashlight")

    def detect_with_nail(self, instance):
        self.open_file_chooser("nail")

    def open_file_chooser(self, method):
        file_chooser = FileChooserIconView()

        popup = Popup(
            title="Select Image",
            content=file_chooser,
            size_hint=(0.9, 0.9)
        )

        def on_selection(instance, selection):
            if selection:
                image_path = selection[0]
                result = predict_hemoglobin(image_path, method)
                self.result_label.text = f"Hemoglobin Level: {result} g/dL"
            popup.dismiss()

        file_chooser.bind(on_selection=on_selection)
        popup.open()

# Main App class
class HemoglobinApp(App):
    def build(self):
        return HomeScreen()

if __name__ == "__main__":
    HemoglobinApp().run()
