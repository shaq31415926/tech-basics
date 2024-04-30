# ask the user for a star sign
user_sign = input("What is your star sign?:")
# if you do not add a lower case t
user_sign = user_sign.lower()

# create a dictionary where the key is the star sign and the value is a horoscope
horoscope_dict = {
    "aries": "You’ll be buzzing with more energy than you’ve had in a while after your cosmic custodian, mobilizing Mars, zips into your sign today for the first time in two years. Between now and June 9, you’ll be fired up to make your dreams a concrete reality. Don’t fly by the seat of your pants though, Ram. Create a solid game plan. When you clarify your vision, you have a much better chance of manifesting it precisely how you see it. When you’ve figured out where you’re going, put the word out on social media. Don’t hesitate to publicize your own endeavors—if not now, when? But since your red-hot ruler can come on too strong, be mindful of stepping on toes as you race up the ladder.",
    "taurus": "Your mind is in great turmoil right now, Taurus, so it isn't surprising that you can't pay much attention to anything. It's as though your concept of the world has been inexorably changed and you see your love life and career with new eyes. Even so, you feel compelled to pick up the pieces of the past and save them. The day ahead should help you let go of the old world.",
    "gemini": "The day will be fairly quiet for you, Gemini. You're likely to yoke yourself to a task and continue working on it until evening. If someone tries to persuade you to take a break, it won't be all that difficult to resist. This is one day when you should follow your instincts, keep your head down, and focus on the task at hand.",
    "cancer": "You should use the day to ponder your professional future, Cancer. Many forces seem to be working together to clarify your ideas on the subject. Rather than rebelling at the slightest provocation, as you've been doing lately, it would be much more reasonable for you to think first about the basic material needs of you and your family.",
    "leo": "Today is no time for dreaming, Leo! Quite the contrary. You can expect to have to settle a number of minor technical problems involving communications or transmissions. On the whole, it will be a somewhat trying day, but at least your mind will be occupied, leaving no room for the difficult internal questions that have been bothering you so much lately.",
    "virgo": "Are you getting hit with obstacles, Virgo? Could it be that you simply need to allot yourself more time to complete the monumental tasks you take on? This might be difficult for you to tolerate. You don't know how to deal with times like these when you must continue doing the same thing over and over until you get results. There's a lesson here for you. Remember that patience is a virtue.",
    "libra": "Are you having some problems with authority, Libra? Are you having a hard time making yourself understood? If so, have you thought about explaining your projects in detail to the people that you hope will follow you in your adventure? You can't expect others to follow you blindly. They, too, have their lives to live, as well as their own objectives and priorities.",
    "scorpio": "Yes, Scorpio, your projects have taken some time to get set up. This is because you haven't been concentrating hard enough. You are doing several things at once, with the result that things have been moving more slowly than you expected. Your change in orientation requires you to focus your energy in a single direction. However, the question remains - what direction?",
    "sagittarius": "You don't have to create everything alone, Sagittarius. Life isn't an individual sport. To live life fully, you must participate. Often this involves interacting with other people. This is an exercise in confidence. Do you want to be with us - yes or no? Regardless of your answer, outside events will lead you in a direction that you can neither predict nor imagine.",
    "capricorn": "When we have found our path, we naturally want to start to walk down it, Capricorn. The reverse isn't true despite what you seem to believe. It's quite futile to learn how to walk when you don't know which path to walk upon. This may seem a little obscure to you, and yet it's true. Desire is what creates aptitude, not the reverse.",
    "aquarius": "The astral energy is encouraging you to open up more to your world, culture, and ways of thinking, Aquarius. You don't have to go off alone in the desert to reinvent everything. For you, this would be the easy way out, because it would allow you to hide! Develop your curiosity about what exists in this society. Your opinion will carry weight later on."
}

# print the users star sign
if user_sign in horoscope_dict.keys():
    print("Your star sign is....")
    print(" ")
    print(horoscope_dict[user_sign])
else:
    print("THAT IS NOT A STAR SIGN")
