import jack, sys

class Pyjack(object):
    def __init__(self):
        super(Pyjack, self).__init__()

    def connect(self):
        try :
            jack.attach("sooperlooper")
            jack.activate()
            jack.connect("sooperlooper:common_out_1", "alsa_pcm:playback_1")
            jack.connect("sooperlooper:common_out_2", "alsa_pcm:playback_2")
        except :
            print("Run jack and sooperlooper")
            sys.exit(1) 
