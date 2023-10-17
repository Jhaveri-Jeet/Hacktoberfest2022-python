import speech_recognition as sr

def audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError as e:
        return "Could not request results; {0}".format(e)

if __name__ == "__main__":
    audio_file = "your_audio_file.wav"  # Replace with the path to your audio file
    text = audio_to_text(audio_file)
    print("Transcription: " + text)
