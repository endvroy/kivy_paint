from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.config import Config
from kivy.utils import get_color_from_hex
from kivy.uix.togglebutton import ToggleButton, ToggleButtonBehavior


class RadioButton(ToggleButton):
    def _do_press(self):
        if self.state == 'normal':
            # ToggleButtonBehavior._do_press(self)
            super()._do_press()


class CanvasWidget(Widget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = get_color_from_hex('#2980B9')
        self.line_width = 2

    def on_touch_down(self, touch):
        if super().on_touch_down(touch):
            return
        with self.canvas:
            Color(*self.color)
            touch.ud['current_line'] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        try:
            touch.ud['current_line'].points += (touch.x, touch.y)
        except KeyError:
            pass

    def set_line_width(self, line_width=2):
        self.line_width = line_width

    def set_color(self, color):
        self.color = color

    def clear_canvas(self):
        saved_widgets = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        for widget in saved_widgets:
            self.add_widget(widget)


class PaintApp(App):
    def build(self):
        canvas_widget = CanvasWidget()
        # canvas_widget.set_color(get_color_from_hex('#2980B9'))
        # canvas_widget.set_line_width()
        return canvas_widget


if __name__ == '__main__':
    Config.set('graphics', 'width', '960')
    Config.set('graphics', 'height', '540')
    # Config.set('input', 'mouse', 'mouse,disable_multitouch')
    from kivy.core.window import Window

    Window.clearcolor = get_color_from_hex('#FFFFFF')
    PaintApp().run()
