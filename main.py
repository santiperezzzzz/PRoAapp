import kivy
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
kivy.require('1.11.1')

class GridDays(ScrollView):
    def __init__(self, **kwargs):
        super(GridDays, self).__init__(**kwargs)
        self.cols = 1
class GridMonday(ScrollView):
    def __init__(self, **kwargs):
        super(GridMonday, self).__init__(**kwargs)
        self.cols = 1
class GridTuesday(ScrollView):
    def __init__(self, **kwargs):
        super(GridTuesday, self).__init__(**kwargs)
        self.cols = 1
class GridWednesday(ScrollView):
    def __init__(self, **kwargs):
        super(GridWednesday, self).__init__(**kwargs)
        self.cols = 1
class GridThursday(ScrollView):
    def __init__(self, **kwargs):
        super(GridThursday, self).__init__(**kwargs)
        self.cols = 1
class GridFriday(ScrollView):
    def __init__(self, **kwargs):
        super(GridFriday, self).__init__(**kwargs)
        self.cols = 1

class MainApp(App):
    def build(self):
        # Establece el tamaño deseado para la ventana
        Window.size = (390, 644)  # Tamaño del iPhone 13 (390x844)

        # Crea el ScreenManager
        sm = ScreenManager()

        # Mapeo de nombres de pantallas y clases
        screens = {
            'grid_days': GridDays,
            'grid_monday': GridMonday,
            'grid_tuesday': GridTuesday,
            'grid_wednesday': GridWednesday,
            'grid_thursday': GridThursday,
            'grid_friday': GridFriday
        }

        # Agrega las pantallas al ScreenManager
        for name, screen_class in screens.items():
            screen = screen_class()
            sm.add_widget(Screen(name=name))
            sm.get_screen(name).add_widget(screen)

        # Establece GridDays como la pantalla principal
        sm.current = 'grid_days'

        return sm

if __name__ == '__main__':
    MainApp().run()
