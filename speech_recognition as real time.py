import speech_recognition as sr
import threading

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`."""
    # Check if recognizer and microphone arguments are of the correct type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    
    # Adjust the recognizer sensitivity to ambient noise
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
    
    # Listening loop
    while True:
        with microphone as source:
            print("Listening...")
            audio = recognizer.listen(source)
        
        # Use a separate thread for recognizing audio
        threading.Thread(target=process_audio, args=(recognizer, audio)).start()

def process_audio(recognizer, audio):
    """Process the audio and print the recognized text."""
    try:
        print("Processing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    try:
        recognize_speech_from_mic(recognizer, microphone)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
