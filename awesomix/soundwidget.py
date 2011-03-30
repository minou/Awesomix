from pymt import *
from widgets.optionwidget import MTOptionWidget
from widgets.quarterbutton import MTQuarterButton
from widgets.quarterslider import MTQuarterSlider

from lib.sound import Sound
from lib.soundmanager import SoundManager
from lib.sooperloopersoundmanager import SooperlooperSoundManager

class SoundWidget(MTOptionWidget):
    def __init__(self, sound, **kwargs):
        super(SoundWidget, self).__init__(**kwargs)
        self.sound = sound
        self.ajout()

    def rate_change(self, value, *largs):
        self.sound.do_rate(value)

    def volume_change(self, value):
        self.sound.set_volume(value)

    def scratch_change(self, value):
        self.sound.do_scratch_pos(value)
    
    def reverse_change(self):
        self.sound.do_reverse()

    def ajout(self):
        y = 1
        rate = MTQuarterSlider(label = 'rate', label_visible = True, color=(y / 50., y / 20., y / 10.), slider_color=(y / 10., 0., y / 10))
        rate.connect('on_value', self.rate_change)
        self.add_widget(rate)
        y+=1
        volume = MTQuarterSlider(label = 'volume', label_visible = True, color=(y / 50., y / 20., y / 10.), slider_color=(y / 10., 0., y / 10))
        volume.connect('on_value', self.volume_change)
        self.add_widget(volume)
        y+=1
        scratch = MTQuarterSlider(label = 'scratch', label_visible = True, color=(y / 50., y / 20., y / 10.), slider_color=(y / 10., 0., y / 10))
        scratch.connect('on_value', self.scratch_change)
        self.add_widget(scratch)
        y+=1
        reverse = MTQuarterButton(label = 'reverse', label_visible = True, color=(y / 50., y / 20., y / 10.), slider_color=(y / 10., 0., y / 10))
        reverse.connect('on_press', self.reverse_change)
        self.add_widget(reverse)

    def on_press(self, *largs):
        self.sound.play()
