import speech_recognition as sr

def real_time_speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Continuously listen for audio input
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)  
            audio_data = recognizer.listen(source)
            print("Processing...")

        try:
            # Convert speech to text
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    real_time_speech_to_text()