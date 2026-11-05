import random
print("nama saya: Ndruru")
mahasiswa = ["ndruru", "ndaru", "adib"]
tinggi_badan = [169, 176, 188]
print("Data Awal", tinggi_badan)
print(mahasiswa[1])
tinggi_badan.append(190)
print(tinggi_badan)
for i in range (98):
  tinggi_badan.append(int(random.uniform(150, 200)))
print("panjang data" , len(tinggi_badan))
print("data terbaru", tinggi_badan)