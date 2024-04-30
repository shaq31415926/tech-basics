# ask the user for input
user_sign = input("What is your star sign?:")
user_sign = user_sign.lower()  # this will lowercase your input

# create a dictionary
horoscope_dict = {
    "aries": "Today will be a great day",
    "taurus": "Fiery Mars will be in low-power mode in your twelfth house of rest and retreat as of today, so heed the signals your body is sending you between now and June 9. There’s no need to RSVP “yes” to social gatherings when all you have the energy for is communing with your couch at home base. Your decisions should be about what YOU feel up to, not what others expect of you. This is an ideal period for focusing on spirituality, dream journaling, art and other intuitive, imaginative activities. Give buried emotions space to bubble up to the surface so you can face them head-on. And resist the impulse to indulge in unhealthy escapes like over imbibing. You’ve gotta deal to heal!",
    "gemini": "",
    "cancer": "",
    "leo": "",
    "virgo": "",
    "libra": "",
    "scorpio": "Yes, Scorpio, your projects have taken some time to get set up. This is because you haven't been concentrating hard enough. You are doing several things at once, with the result that things have been moving more slowly than you expected. Your change in orientation requires you to focus your energy in a single direction. However, the question remains - what direction?",
    "sagittarius": "",
    "capricorn": "",
    "aquarius": "",
    "pisces": ""}

# if else statement that picks up if the user sign exists in the dictionary keys
if user_sign in horoscope_dict.keys():
    print("Your horoscope is...")
    print("-")
    print(horoscope_dict[user_sign])
else:
    print("DOES NOT EXIST")
