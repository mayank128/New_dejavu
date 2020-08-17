from dejavu import Dejavu
#from dejavu.logic.recognizer.microphone_recognizer import MicrophoneRecognizer
from dejavu.recognize import MicrophoneRecognizer
config = {
        "database" : {
            "host":"127.0.0.1",
            "user":"root",
            "password":"12345678",
            "database":"dejavu",
            }
        }
djv = Dejavu(config)
djv.fingerprint_directory("/home/mayank/Music/dejavu-master/mp3", [".mp3"])
print djv.db.get_num_fingerprints()
print "listning audio from newpy"
song = djv.recognize(MicrophoneRecognizer, seconds = 10)
