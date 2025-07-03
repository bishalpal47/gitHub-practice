'''
Problem: Suggest best travel times to cross Howrah Bridge based on traffic patterns.
- 5 AM to 7 AM: "Light traffic - smooth journey"
- 8 AM to 11 AM: "Heavy traffic - expect delays"
- 12 PM to 4 PM: "Moderate traffic - reasonable time"
- 5 PM to 9 PM: "Peak traffic - consider alternate route"
- 10 PM to 4 AM: "Very light traffic - fastest route"
'''

hour = int(input("Enter travel hour (24-hour format): "))

if 5 <= hour <= 7:
    print("Light traffic - smooth journey")
elif 8 <= hour <= 11:
    print("Heavy traffic - expect delays")
elif 12 <= hour <= 16:
    print("Moderate traffic - reasonable time")
elif 17 <= hour <= 21:
    print("Peak traffic - consider alternate route")
elif 22 <= hour <= 24 or 0 <= hour <= 4:
    print("Very light traffic - fastest route")
else:
    print("Invalid hour")