guests = ['Albert Einstein', 'Marie Curie', 'Nikola Tesla']
print("\nGreat news! I found a bigger dinner table.")

guests.insert(0, 'Galileo Galilei')
guests.insert(2, 'Ada Lovelace')
guests.append('Charles Darwin')

for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner.")