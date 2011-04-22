from sound import Sound
from soundmanager import SoundManager
from soundosc import SoundOsc
from simpleOSC import *

class SooperlooperSoundManager(SoundManager):
    def __init__(self, **kwargs):
        super(SooperlooperSoundManager, self).__init__(**kwargs)
        self.addr = 'osc.udp://127.0.0.1:9951/'
        initOSCServer(port=9952)
        initOSCClient(port=9951)
        self._nextid = 0
        self._sounds = {}
        self.values = {}
        self.list_hit = ['trigger', 'pause', 'solo', 'reverse']
        self.list_set = ['wet', 'rate', 'scratch_pos']

    def nextid(self):
        soundid = self._nextid
        self._nextid += 1
        return soundid

    def create(self, filename):
        soundid = self.nextid()
        sendOSCMsg('/loop_add', [2, 60])
        sound = Sound(self, filename, soundid)
        self._sounds[soundid] = sound
        sendOSCMsg('/sl/%d/load_loop' % soundid, [filename, self.addr, '/loop/%d' % soundid])
        #_len = sendOSCMsg('/sl/%d/get' % soundid, [filename, self.addr, '/loop/%d' % soundid])
        return sound

    def play(self, soundid):
        self.do(soundid, 'trigger')

    def pause(self, soundid):
        self.do(soundid, 'pause')

    def stop(self, soundid):
        sendOSCMsg('/loop_del', ['%d'] %soundid)

    def set_volume(self, soundid, volume):
        sendOSCMsg('/sl/%d/set' %soundid, ['wet', volume])

    def do_reverse(self, soundid):
        _value = self.values.get('reverse', 0)
        if _value == 0:
            sendOSCMsg('/sl/%d/hit' %soundid, ['reverse'])
            _value = 1
        if _value == 1:
            sendOSCMsg('/sl/%d/hit' %soundid, ['trigger'])
            _value = 0
        self.values['reverse'] = _value


    def do(self, soundid, name, **kwargs):
        if name in self.list_hit:
            if name == 'reverse':
                self.do_reverse(soundid)
            else:
                sendOSCMsg('/sl/%d/hit' %soundid, [name])
            return
        value = kwargs.get('value', 1)
        _value = self.values.get(name, None)
        if _value == value:
            return
        if name in self.list_set:
            sendOSCMsg('/sl/%d/set' %soundid, [name, value])
        self.values[name] = value
