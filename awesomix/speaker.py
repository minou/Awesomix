import jack, sys

class Speaker(object):
    def __init__(self, manager, **kwargs):
        super(Speaker, self).__init__(**kwargs)
        self._manager = manager
        jack.attach("sooperlooper")
        jack.activate()

    def connect_left_speaker(self):
        try :
            jack.connect("sooperlooper:common_out_1", "alsa_pcm:playback_1")
        except :
            print("Run jack and sooperlooper")
            sys.exit(1) 
    
    def connect_right_speaker(self):
        try :
            jack.connect("sooperlooper:common_out_2", "alsa_pcm:playback_2")
        except :
            print("Run jack and sooperlooper")
            sys.exit(1) 
