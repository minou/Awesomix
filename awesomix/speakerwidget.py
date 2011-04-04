from pymt import *
from widgets.optionwidget import MTOptionWidget
from widgets.quarterbutton import MTQuarterButton
from widgets.quarterslider import MTQuarterSlider

from lib.sound import Sound
from soundwidget import SoundWidget

class SpeakerWidget(MTOptionWidget):
    def __init__(self, list_sound_widget, **kwargs):
        super(SpeakerWidget, self).__init__(**kwargs)
        self.list_sound_widget = list_sound_widget
        self.max_volume = kwargs.get('max_volume', 5)
        self.label = kwargs.get('label', 'Speaker')
        self.label_visible = kwargs.get('label_visible', True)
    
    def on_update(self):
        for sound_widget in self.list_sound_widget:
            curpos = Vector(self.pos)
            sound_widget_pos = Vector(sound_widget.pos)
            distance = curpos.distance(sound_widget_pos)
            sound_widget.sound.set_volume(self.max_volume - (distance / 100.))
