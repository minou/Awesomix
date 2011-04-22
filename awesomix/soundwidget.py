from pymt import *
from widgets.optionwidget import MTOptionWidget
from lib.sound import Sound

class SoundWidget(MTOptionWidget):
    def __init__(self, sound, **kwargs):
        super(SoundWidget, self).__init__(**kwargs)
        self._sound = sound
        self._distance_detection = kwargs.get('distance_detection', 25)
        self._position = self.pos
    
    @property
    def sound(self):
        return self._sound

    def collide_point_play(self, x, y):
        curpos = Vector(self._position)
        touchpos = Vector(x, y)
        distance = curpos.distance(touchpos)
        return distance <= self._distance_detection

    def on_touch_up(self, touch):
        if not super(SoundWidget, self).on_touch_up(touch):
            return
        if self.collide_point_play(touch.x, touch.y):
            self._sound.play()
        self._position = touch.pos
        return True
