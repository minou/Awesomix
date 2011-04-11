from pymt import *

from widgets.optionwidget import MTOptionWidget

from lib.sound import Sound
from soundwidget import SoundWidget

class EffectWidget(MTOptionWidget):
    def __init__(self, list_sound_widget, name, value, **kwargs):
        super(EffectWidget, self).__init__(**kwargs)
        self.list_sound_widget = list_sound_widget
        self.name = name
        self.value = value
        self.effect_radius = kwargs.get('effect_radius', 200)
        self.effect_color = kwargs.get('effect_color', (0.4, 0.1, 0.9, 0.4))
        self._active = False
        self.label = kwargs.get('label', self.name)
        self.label_visible = kwargs.get('label_visible', True)

    def on_touch_down(self, touch):
        if not super(EffectWidget, self).on_touch_down(touch):
            return
        self._active = True
        return True

    def on_touch_up(self, touch):
        if not super(EffectWidget, self).on_touch_up(touch):
            return
        self._active = False
        return True

    def on_update(self):
        for sound_widget in self.list_sound_widget:
            curpos = Vector(self.pos)
            sound_widget_pos = Vector(sound_widget.pos)
            distance = curpos.distance(sound_widget_pos)
            if (distance < self.effect_radius):
                if (self.value != 0):
                    print(distance)
                    #sound_widget.sound.do(self.name, distance / self.value)
                    return
                sound_widget.sound.do(self.name, self.value)

    def draw(self):
        super(EffectWidget, self).draw()
        if self._active:
            if (self.value != 0):
                i = 0
                while (i < self.value):
                    set_color(*(0.3*i,0.1*i,0.2*i,0.4))
                    drawSemiCircle(pos=self.pos, inner_radius=self.radius + i * 50, outer_radius=self.radius + (i+1) * 50)
                    i += 1
                return
            set_color(*self.effect_color)
            drawSemiCircle(pos=self.pos, inner_radius=self.radius, outer_radius=self.effect_radius)
