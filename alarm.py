from  utilities import Utilies
import time

class App():
    def __init__(self) -> None:
        print('initializing alarm...')
        
    def main(self, _time, narration):        
        utilities = Utilies()
        hh, xx = _time.split(':')
        mm , pp = xx[:2], xx[2:]
        while(True):
            text,hour, mins, prompt = utilities.datetime(mode='time')
            if int(hour)==int(hh) and int(mins)==int(mm) and prompt==pp:
                audiofile = utilities.text2audio(text=text+' '+narration)
                utilities.play_audio(audio_file_path=audiofile)
                break

if __name__ == "__main__":
    app = App()
    alarm_time = input('Enter alarm time')
    description = input('Enter description')
    app.main(alarm_time, description)