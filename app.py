from tkinter import *
from utilities import Utilies
import time

class App():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Alarm')
        self.root.geometry('300x200')

        self.label1 = Label(self.root, text='Alarm Time (HH:MM AM/PM):')
        self.label1.pack()
        self.alarm_time_entry = Entry(self.root)
        self.alarm_time_entry.pack()

        self.label2 = Label(self.root, text='Description:')
        self.label2.pack()
        self.description_entry = Entry(self.root)
        self.description_entry.pack()

        self.set_button = Button(self.root, text='Set Alarm', command=self.set_alarm)
        self.set_button.pack()
        
    def set_alarm(self):
        alarm_time = self.alarm_time_entry.get()
        description = self.description_entry.get()
        app.main(alarm_time, description)

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

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
