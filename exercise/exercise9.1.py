class Restaurant:
    """Representasi sederhana dari sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut nama restoran dan jenis masakan."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Menampilkan informasi nama restoran dan jenis masakannya."""
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")

    def open_restaurant(self):
        """Menampilkan pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.restaurant_name} sekarang sudah BUKA!")

# Membuat instance dari class Restaurant
restaurant = Restaurant("Sate Khas Solo", "Masakan Jawa")

# Mencetak kedua atribut secara terpisah
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Memanggil kedua metode
restaurant.describe_restaurant()
restaurant.open_restaurant()