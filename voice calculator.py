import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

engine = pyttsx3.init()

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except (SyntaxError, NameError, ZeroDivisionError, ArithmeticError) as e:
        return f"Error: {str(e)}"

def speech_calculator():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Recognizing...")

    try:
        spoken_text = recognizer.recognize_google(audio)
        print(f"You said: {spoken_text}")

        spoken_text = spoken_text.replace(" ", "")
        spoken_text = spoken_text.lower()


        if all(char in "0123456789+-*/()" for char in spoken_text):
            result = evaluate_expression(spoken_text)
            print(f"Result: {result}")
            engine.say(f"The result is {result}")
        else:
            engine.say("Invalid input. Please speak a valid mathematical expression.")

        engine.runAndWait()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    while True:
        speech_calculator()
