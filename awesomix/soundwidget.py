from pymt import *
from widgets.optionwidget import MTOptionWidget
from lib.sound import Sound

class SoundWidget(MTOptionWidget):
    def __init__(self, sound, **kwargs):
        super(SoundWidget, self).__init__(**kwargs)
        self.sound = sound
        self._position = self.pos

    def get_sound(self):
        return self.sound

    def collide_point_play(self, x, y):
        curpos = Vector(self._position)
        touchpos = Vector(x, y)
        distance = curpos.distance(touchpos)
        return distance <= self.radius

    def on_touch_up(self, touch):
        if not super(SoundWidget, self).on_touch_up(touch):
            return
        if self.collide_point_play(touch.x, touch.y):
            self.sound.play()
        self._position = touch.pos
        return True
