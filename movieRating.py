'''
Question: Ask the user to enter a movie rating out of 5 and provide a message based on the following conditions - 
5.0: "Bhai masterpiece dekh liya 🔥"
4.0 to 4.9: "Bhai badiya movie thi 👌"
3.0 to 3.9: "Theek thaak thi, timepass 😐"
2.0 to 2.9: "Meh! Bore ho gaya yaar 😴"
Below 2.0: "Mat dekhna bhai, time barbaad 🚫"
'''

rating = float(input("Movie rating (out of 5): "))
if rating == 5:
    print("Bhai masterpiece dekh liya 🔥")
elif rating >= 4:
    print("Bhai badiya movie thi 👌. Adding some random text.")
elif rating >= 3:
    print("Theek thaak thi, timepass 😐")
elif rating >= 2:
    print("Meh! Bore ho gaya yaar 😴. Ghum peye gache. Aar khide legeche.")
else:
    print("Mat dekhna bhai, time barbaad 🚫")
