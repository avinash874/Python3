# 3 question ke liye pyttsx3 module ka use karna hoga. Is module ko install karne ke liye terminal me ye command run kare:
# pip3 install pyttsx3

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Hey Avinash I Love you really much")
engine.runAndWait()