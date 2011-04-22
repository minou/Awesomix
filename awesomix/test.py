from pymt import *

from widgets.optionwidget import MTOptionWidget
from widgets.quarterbutton import MTQuarterButton

from lib.sound import Sound
from lib.soundmanager import SoundManager
from lib.sooperloopersoundmanager import SooperlooperSoundManager

from speaker import Speaker
from speakerwidget import SpeakerWidget
from soundwidget import SoundWidget
from effectwidget import EffectWidget

from simpleOSC import *
import sys, os
from os.path import realpath, join
from glob import glob

if __name__ == '__main__':
    win = getWindow()
    win.style['bg-color'] = (0,0,0,0) 

    width = 0.
    height = 0.
    def random_position(width, height):
        dx = dy = 100.
        if (width > win.width):
            width = 100.
        else :
            width += dx
        height += dy
        return (width, height)
    
    manager = SooperlooperSoundManager()

    list_sound_widget = []
    list_effect = [('rate', 5), ('reverse', 0), ('scratch_pos', 0)]

    selectSound = MTOptionWidget(label = 'Select', label_visible = True, pos = win.center)
    win.add_widget(selectSound)

    def on_effect_press(name, value, *largs):
        effect = EffectWidget(list_sound_widget, name, value, pos = random_position(width, height))
        win.add_widget(effect)

    selectEffect = MTOptionWidget(label = 'Effect', label_visible = True, pos = (500, 200))
    x = 0
    for name, value in list_effect:
        effect = MTQuarterButton(label=name, label_visible=True, color=(0.6+x*0.1, 0.1, 0.3))
        effect.connect('on_press', curry(on_effect_press, name, value))
        selectEffect.add_widget(effect)
        x+=1
    win.add_widget(selectEffect)

    speaker = Speaker(manager)
    speaker.connect_right_speaker()
    speaker.connect_left_speaker()

    speaker_widget = SpeakerWidget(list_sound_widget, pos = (win.width / 2, win.height / 2 + 200))
    win.add_widget(speaker_widget)

    def on_sound_press(filename, *largs):
        sound = manager.create(filename)
        sound_widget = SoundWidget(sound, label=sound.soundid, label_visible=True, pos = random_position(width, height))
        list_sound_widget.append(sound_widget)
        win.add_widget(sound_widget)

    x = 0
    for filename in glob(join(sys.argv[len(sys.argv) - 1], '*.wav')):
        option = MTQuarterButton(label=filename, color=(x / 20.,0,x / 10.))
        option.connect('on_press', curry(on_sound_press, filename))
        selectSound.add_widget(option)
        x+=1

    runTouchApp()
    sendOSCMsg('/quit')
    closeOSC()
