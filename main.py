from  utilities import Utilies


class App():
    def __init__(self) -> None:
        print('initializing app...')
        
    def main(self):        
        utilities = Utilies()
        date = utilities.datetime(mode='date')
        time = utilities.datetime(mode='time')
        text = date + ' and ' +time
        audiofile = utilities.text2audio(text=text)
        utilities.play_audio(audio_file_path=audiofile)

if __name__ == "__main__":
    app = App()
    app.main()