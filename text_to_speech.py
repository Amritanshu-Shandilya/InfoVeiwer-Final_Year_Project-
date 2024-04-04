from gtts import gTTS
import os

def text_to_speech(text, filename, lang='en'):
    # Create a text-to-speech object
    tts = gTTS(text=text, lang=lang)
    
    # Save the audio to a file
    tts.save("received/"+filename)
    

if __name__ == "__main__":
    with open(r'C:\Users\Shiv\dev\InfoVeiwer-Final_Year_Project-\received\sample.txt', 'r') as file:
        text = file.read()
    filename = 'sample.mp3'
    text_to_speech(text, filename)
