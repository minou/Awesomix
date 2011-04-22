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
        self.effect_radius_global = kwargs.get('effect_radius', 200)
        if (self.value != 0):
            self.effect_radius = self.effect_radius_global / self.value
        else:
            self.effect_radius = self.effect_radius_global
        self.effect_color = kwargs.get('effect_color', (0.4, 0.1, 0.9, 0.4))
        self._active = False
        self.label = kwargs.get('label', self.name)
        self.label_visible = kwargs.get('label_visible', True)
        self.list_sound = []

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
            sound = sound_widget.sound
            curpos = Vector(self.pos)
            sound_widget_pos = Vector(sound_widget.pos)
            distance = curpos.distance(sound_widget_pos)
            if (distance < self.effect_radius_global + self.radius):
                if (distance <= self.radius):
                    return
                self.list_sound.append(sound)
                self.list_sound = list(set(self.list_sound))
                if (self.value != 0):
                    value = int(abs((distance - self.radius) / self.effect_radius))
                    sound.do(self.name, value=value)
                else:
                    sound.do(self.name)
            else:
                if sound in self.list_sound:
                    if self.value != 0:
                        sound.do(self.name)
                    else:
                        sound.do(self.name, value=self.value)
                    self.list_sound.remove(sound)


    def draw(self):
        super(EffectWidget, self).draw()
        if self._active:
            if (self.value != 0):
                for i in xrange(self.value):
                    set_color(*(0.3*i,0.1*i,0.2*i,0.4))
                    drawSemiCircle(pos=self.pos, inner_radius=self.radius + i * self.effect_radius, outer_radius=self.radius + (i+1) * self.effect_radius)
            else:
                set_color(*self.effect_color)
                drawSemiCircle(pos=self.pos, inner_radius=self.radius, outer_radius=self.effect_radius)
