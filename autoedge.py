import ctypes
import win32api
import win32con
import win32gui
import json
import os

class AutoEdge:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                self.config = json.load(file)
        else:
            self.config = {}

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

    def get_current_resolution(self):
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        return screensize

    def apply_display_settings(self, app_name):
        if app_name in self.config:
            settings = self.config[app_name]
            width, height = settings.get('resolution', self.get_current_resolution())
            color_depth = settings.get('color_depth', 32)

            # Set resolution
            self.set_resolution(width, height)

            # Set color depth
            self.set_color_depth(color_depth)

    def set_resolution(self, width, height):
        dm = win32api.EnumDisplaySettings(None, 0)
        dm.PelsWidth = width
        dm.PelsHeight = height
        dm.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
        win32api.ChangeDisplaySettings(dm, 0)

    def set_color_depth(self, color_depth):
        # This is a placeholder; changing color depth programmatically is not straightforward in Windows
        print(f"Setting color depth to {color_depth} bits (Note: This requires manual configuration in most cases)")

    def add_application_settings(self, app_name, resolution, color_depth):
        self.config[app_name] = {
            'resolution': resolution,
            'color_depth': color_depth
        }
        self.save_config()

if __name__ == "__main__":
    auto_edge = AutoEdge()

    # Example usage
    auto_edge.add_application_settings("ExampleApp", (1920, 1080), 32)
    auto_edge.apply_display_settings("ExampleApp")