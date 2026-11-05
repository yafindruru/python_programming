guests = ['Galileo Galilei', 'Albert Einstein', 'Ada Lovelace', 'Marie Curie', 'Nikola Tesla', 'Charles Darwin']
print("\nUnfortunately, the new table won't arrive in time, and I can only invite two people.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can no longer invite you to dinner.")

for guest in guests:
    print(f"Dear {guest}, you are still invited!")

del guests[1]
del guests[0]
print(guests)