current_users = ['admin', 'Jaden', 'sarah', 'Mike', 'emma']
new_users = ['mike', 'EMMA', 'john', 'david', 'luke']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is taken. Enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")