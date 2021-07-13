import speech_recognition as sr
from os import path
                
def printWAV(FILE_NAME, pos, clip):
    # use the audio file as the audio source
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), 'static/'+FILE_NAME)
    r = sr.Recognizer()
    text = ""
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source, duration=clip, offset=pos)
        # recognize speech using Google Speech Recognition
        try:
            text += r.recognize_google(audio) + "\n"
        except sr.UnknownValueError:
            text += "Could not understand audio\n"
        except sr.RequestError as e:
            text += "Could not request results; {0}".format(e)+ "\n"
    return text