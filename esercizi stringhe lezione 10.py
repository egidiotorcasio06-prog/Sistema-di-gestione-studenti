testo = "guida di python"
title_case_testo = testo.title()
print(title_case_testo)

nome_completo = "mario rossi"
nome_maiuscolo = nome_completo.upper()
print(nome_maiuscolo)
nome_completo = "mario rossi"
parti_del_nome = nome_completo.split()
parti_inverse = parti_del_nome[::-1]
nome_invertito_capitalizzato = ' '.join(parti_inverse).title()
print(nome_invertito_capitalizzato)

print("l'arte della programmazione".title())

print("PyThOn".swapcase())

testo = "Hello World"
prima = testo.swapcase() #hELLO wORLD
seconda = prima.title() #Hello World
print(seconda)

print("   Python   ".strip())

print("   Hello   ".lstrip())

print("***Python***".strip("*"))

print("Hello World".upper())

print("PYTHON".lower())

str1 = "Python"
str2 = "PYTHON"
print(str1.lower() == str2.lower())

print("Java è bello".replace("Java", "Python"))

print("banana".replace("a", "@", 1))

print("H e l l o".replace(" ", ""))

print("http://www.exaple.com".removeprefix("http://"))

print("documento.txt".removesuffix(".txt"))

print("Sig.Rossi".removeprefix("Sig."))

print("apple,banana,cherry".split(","))

print("Hello World Python".split())

print("nome:cognome:età".split(":"))

print("Riga1\nRiga2\nRiga3".splitlines())

print("A\nB\nC".splitlines(keepends=True))

print(" ".join(["python", "è", "facile"]))

print("-".join(["1995", "02", "06"]))

prima, sep, dopo = "hello@world.com".partition("@")
print(prima)
print(sep)
print(dopo)

print("python".find("th"))

pos = "python programming".find ("java")
if pos == -1:
    print("non trovato")
else:
    print(f"Trovato alla posizione {pos}")   

testo = "Hello World"
prima = testo.find("o")  # 4
seconda = testo.find("o", prima + 1)  # 7
print(seconda) 

print("python".startswith("py"))

print("script.py".endswith(".py"))

print("image.jpg".endswith((".jpg", ".png")))

print("banana".count("a"))

print(len("hello world python".split()))

print("192.168.1.1".count("."))

print("12345".isdigit())
print("hello".isalpha())
print("python3".isalnum())

print("PYTHON".isupper())
print("python".islower())
print("Hello World".istitle())

print("    ".isspace())
print("\t\n".isspace())
print("".isspace())

print("python".center(20)) #"       python        "
print("Test".ljust(10, "-")) #"Test------"
print("42".rjust(5, "0")) #"00042"

print("42".zfill(5)) #"00042"
print("-7".zfill(4)) #"-007"
numero = "123"
codice = "PDR" + numero.zfill(5)
print(codice) #"PDR00123"

print("A\tB\tC".expandtabs(4))
print("nome\tCognome\tEtà".expandtabs(10))

bytes_data = "cafè".encode("utf-8")
print(bytes_data)
stringa = b'python'.decode("utf-8")
print(stringa)

vocali = "aeiou"
numeri = "12345"
tabella = str.maketrans(vocali, numeri)
print("hello world".translate(tabella))

import string
rimuovi_punt = str.maketrans('', '', string.punctuation)
print("hello, world!".translate(rimuovi_punt))

print("python"[:3])  #"pyt"
print("programming"[-2:])  #"ng"
print("hello"[::-1])  #"olleh"

print("python"[::2])  #"pto"
print("abcdef"[::2])  #"ace"

password = "python123"
valida = (len(password) >= 8 and
          any(c.isalpha() for c in password) and
            any(c.isdigit() for c in password))
print(f"password valida: {valida}")

#or
#versione migliorata con controllo spazi
password = "python 123"
#requisiti:
#-almeno 8 caratteri
#-almeno una lettera
#-almeno un numero
#-niente spazi


valida = (len(password) >= 8 and 
          any(ch.isalpha() for ch in password) and 
          any(ch.isdigit() for ch in password) and
          not any(ch.isspace() for ch in password) #niente spazi
)
print(f"password valida: {valida}")


