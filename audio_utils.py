import pyttsx3

def text_to_audio(text, filename="audio.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename
