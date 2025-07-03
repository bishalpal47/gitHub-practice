'''
Problem: Write a program that suggests which Kolkata Metro line to take based on your destination.
- If destination is "Esplanade" or "Park Street" → "Take Blue Line"
- If destination is "Kalighat" or "Rabindra Sadan" → "Take Blue Line (Extension)"
- If destination is "Salt Lake Stadium" → "Take Green Line"
- Otherwise → "Check metro map for other lines"
'''


destination = input("Enter your destination: ").lower()

if destination == "Esplanade" or destination == "Park Street":
    print("Take Blue Line")
elif destination == "Kalighat" or destination == "Rabindra Sadan":
    print("Take Blue Line (Extension)")
elif destination == "Salt Lake Stadium":
    print("Take Green Line")
else:
    print("Check metro map for other lines")