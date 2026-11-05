# printing_models.py
import printing_functions

desain_belum_dicetak = ['casing hp', 'liontin robot', 'dodecahedron']
model_selesai = []

# Memanggil fungsi menggunakan nama modul
printing_functions.print_models(desain_belum_dicetak, model_selesai)
printing_functions.show_completed_models(model_selesai)