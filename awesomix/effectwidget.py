from pymt import *

from widgets.optionwidget import MTOptionWidget

from lib.sound import Sound
from soundwidget import SoundWidget

class EffectWidget(MTOptionWidget):
    def __init__(self, list_sound_widget, **kwargs):
        super(EffectWidget, self).__init__(**kwargs)
        self.list_sound_widget = list_sound_widget
        self.effect_radius = kwargs.get('effect_radius', 200)
        self.effect_color = kwargs.get('effect_color', (0.4, 0.1, 0.9, 0.4))
        self._active = False
        self.label = kwargs.get('label', 'Effect')
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
        #if not super(SpeakerWidget, self).on_touch_move(touch):
            #return
        for sound_widget in self.list_sound_widget:
            curpos = Vector(self.pos)
            sound_widget_pos = Vector(sound_widget.pos)
            distance = curpos.distance(sound_widget_pos)
            if (distance < self.effect_radius):
                print(sound_widget.sound.soundid)
                #sound_widget.sound.set_volume(self.max_volume - (distance / 100.))

    def draw(self):
        super(EffectWidget, self).draw()
        if self._active:
            set_color(*self.effect_color)
            drawSemiCircle(pos=self.pos, inner_radius=self.radius, outer_radius=self.effect_radius)
