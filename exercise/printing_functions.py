# printing_functions.py

def print_models(unprinted_designs, completed_models):
    """Mencetak tiap desain dan memindahkannya ke completed_models."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Mencetak model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Menampilkan semua model yang sudah dicetak."""
    print("\nModel berikut sudah dicetak:")
    for completed_model in completed_models:
        print(completed_model)