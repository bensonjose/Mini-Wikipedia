import pyttsx3
import wikipedia as w
engine = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty("rate", 200)
engine.setProperty("voice", voice_id)
def speak(text):
    engine.say(text);print(text)
    engine.runAndWait()
while True:
    try:
        engine.say("Please tell me your query: ");engine.runAndWait();query = input("Enter your Query: ")
        if query == "exit":
            break
        else:
            result = w.summary(query, sentences=2)
            speak(result)
    except:
        speak("Result not found Enter valid input or check for spelling errors.")