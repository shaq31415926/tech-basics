import os
import time

# this will clear the terminal screen, if you are not using the press play button
os.system("clear") # windows user replace clear with cls

# this is the joke
print("-"*50)
print("Hi :)! Welcome to my joke app")
print("Question: What is Black and White and red all over?")
# this creates a time delay before the statement is printed
time.sleep(1)
print("-")
time.sleep(1)
print("-")
time.sleep(1)
print("-")
time.sleep(1)
print("-")
print("Answer: A newspaper")

# add sound effects - credit to Silas for sharing this code in class
file = "music/drum.wav"  # update file with your music file (.m4a, .mp3, .wav)
os.system("afplay " + file)

print("🥁")
print("-"*50)
