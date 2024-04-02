import time
import os

# welcome the user
print("HI! Welcome to my Joke App 😹")

# print the first joke
print("Question: What is Black and White and red all over?")

# add a time delay of 5 seconds before printing the answer
print("-")
time.sleep(1)
print("-")
time.sleep(1)
print("-")
time.sleep(1)
print("-")
time.sleep(1)
print("-")
time.sleep(1)

# print the answer
print("Answer: A newspaper!")
# add sound effects - credit to Silas for sharing this code in class
file = "music/laugh.m4a"   # update file with your music file (.m4a, .mp3, .wav)
os.system("afplay " + file)
print("Let's try another joke....")
time.sleep(4)
print("If at first you don’t succeed, call it version 1.0")
print("🥁"*50)
file = "music/drum.wav"   # update file with your music file (.m4a, .mp3, .wav)
os.system("afplay " + file)
print("-"*50)
