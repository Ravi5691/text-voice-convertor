# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()
import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("mayankl ki ja ho mayank ki ja ho ")
# engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()
# import pyttsx3

# engine = pyttsx3.init()

# # List all voices
# voices = engine.getProperty('voices')

# # Select Hindi voice (replace 'hindi_voice_id' with the actual ID from the list)
# for voice in voices:
#     if 'Hindi' in voice.name or 'hi-IN' in voice.languages:  # Adjust depending on your system's voice names
#         engine.setProperty('voice', voice.id)
#         break

# engine.say("नमस्ते, आप कैसे हैं?")
# engine.runAndWait()