# Lista de hashes MD5 encontrados en el sistema
hashes_encontrados = [
    "d41d8cd98f00b204e9800998ecf8427e",
    "5d41402abc4b2a76b9719d911017c592",
    "5d41402abc4b2a76b9719d911017c592",  # Duplicado
    "098f6bcd4621d373cade4e832627b4f6"
]

hashes_sospechosos = []

for hash_md5 in hashes_encontrados:
    if hashes_encontrados.count(hash_md5) > 1 and hash_md5 not in hashes_sospechosos:
        hashes_sospechosos.append(hash_md5)

print("Hashes duplicados encontrados (posibles infecciones repetidas):")
for h in hashes_sospechosos:
    print(f"⚠️  {h}")
