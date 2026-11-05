def city_country(city, country):
    """Mengembalikan string 'kota, negara'."""
    return f"{city.title()}, {country.title()}"

print(city_country('santiago', 'chile'))
print(city_country('surakarta', 'indonesia'))
print(city_country('paris', 'prancis'))