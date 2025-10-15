studenti = [
    ["Mario Rossi", [6, 7, 8, 6], [7, 8, 7, 9], [5, 6, 7, 6]],
    ["Laura Bianchi", [9, 8, 9, 10], [8, 7, 8, 8], [9, 9, 8, 10]],
    ["Giuseppe Verdi", [5, 6, 5, 7], [6, 6, 7, 6], [7, 8, 7, 8]],
    ["Anna Neri", [8, 7, 9, 8], [9, 9, 8, 9], [7, 8, 8, 7]],
    ["Marco Gialli", [4, 5, 6, 5], [6, 5, 6, 7], [5, 5, 6, 6]]
]

materie = ["Matematica", "Italiano", "Inglese"]

def aggiungi_studente(lista_studenti, nome, voti_mat, voti_ita, voti_ing):
    nuovo_studente = [nome, voti_mat, voti_ita, voti_ing]
    lista_studenti.append(nuovo_studente)

def calcola_media_studente(studente):
    somma_totale = 0
    numero_voti = 0

    for materia in studente[1:]:
        for voto in materia:
            somma_totale += voto
            numero_voti += 1

    return somma_totale / numero_voti if numero_voti > 0 else 0

def trova_studenti_insufficienze(lista_studenti) :
    studenti_con_insufficienze = []
    for studente in lista_studenti:
        ha_insufficienza = False 
    for materia in studente[1:]:
        for voto in materia:
            if voto < 6:
                ha_insufficienza = True
                break
        if ha_insufficienza:
            break
    if ha_insufficienza:
        studenti_con_insufficienze.append(studente[0])
    return studenti_con_insufficienze

def migliora_voti_insufficenti(lista_studenti):
    for studente in lista_studenti:
        for i_materia in range(1, 4):
            for i_voto, voto in enumerate(studente[i_materia]):
                if voto < 6:
                    studente[i_materia][i_voto] = min(voto + 1, 10)

def crea_classifica(lista_studenti):
    classifica = []
    
    for studente in lista_studenti:
        nome=studente[0]
        media = calcola_media_studente(studente)
        classifica.append([nome, media])

    classifica.sort(key=lambda x: x[1], reverse=True)
    return classifica

def rimuovi_studente(lista_studenti, nome):
    for studente in lista_studenti:
        if studente[0] == nome:
            lista_studenti.remove(studente)
            return True
    return False

def statistiche_classe(lista_studenti):
    stats = {}
    stats['totale_studenti'] = len(lista_studenti)

    medie =[]
    for studente in lista_studenti:
     medie.append(calcola_media_studente(studente))

    stats['media_classe'] = sum(medie) / len(medie)

    indice_max = medie.index(max(medie))
    stats['miglior_studente'] = lista_studenti[indice_max][0] 
    stats['media_migliore'] = max(medie)

    indice_min = medie.index(min(medie))
    stats['peggior_studente'] = lista_studenti[indice_min][0]
    stats['media_peggiore'] = min(medie)

    eccellenze = 0
    for media in medie:
        if media >= 8:
            eccellenze += 1
    stats['eccellenze'] = eccellenze

    insufficienti = 0
    for media in medie:
        if media < 6:
            insufficienti += 1
    stats['insufficienti'] = insufficienti
    return stats

def inserisci_voto(lista_studenti, nome_studente, materia_index, voto, posizione):
    for studente in lista_studenti:
        if studente[0] == nome_studente:
                materia_index + 1 

                studente[materia_index + 1].insert(posizione, voto)
                return True
    return False

def unisci_classi(classe1, classe2):
    risultato = classe1[:]
    nomi_presenti = []
    for studente in risultato:
        nomi_presenti.append(studente[0])
    for studente in classe2:
        if studente[0] not in nomi_presenti:
            risultato.append(studente)
    return risultato

def resetta_voti_materia(lista_studenti, materia_index):
    for studente in lista_studenti:
        studente[materia_index + 1].clear()
        studente[materia_index + 1].append(0)


print("=== SISTEMA GESTIONE STUDENTI E VOTI ===\n")

print("1. Aggiungi studente")
aggiungi_studente(studenti, "Paolo Blu", [7, 8, 7, 9], [8, 8, 9, 8], [7, 7, 8, 8])
print(f" nuovo studente aggiunto: {studenti[-1] [0]}")

print("\n2. clacola media")
for studente in studenti[:3]:
    media = calcola_media_studente(studente)
    print(f" media di {studente[0]}: media = {media:.2f}")

print("\n3. trova insufficienze")
insufficienze = trova_studenti_insufficienze(studenti)
print(f" studenti con insufficienze: {insufficienze}")

print("\n4. migliora voti")
print(f" prima: Marco Gialli matematica = {studenti[4][1]}")
migliora_voti_insufficenti(studenti)
print(f" dopo: Marco Gialli matematica = {studenti[4][1]}")

print("\n5. claffica studenti")
classifica = crea_classifica(studenti)
for i, (nome, media) in enumerate(classifica [:3], 1):
    print(f" {i}. {nome} - media: {media:.2f}")

print("\n6. rimuovi studente")
rimosso = rimuovi_studente(studenti, "Marco Gialli")
print(f" Marco Gialli rimosso: {rimosso}")
print(f"studenti rimasti: {len(studenti)}")

print("\n7. statistiche classe")
stats = statistiche_classe(studenti)
print(f" totale studenti: {stats['totale_studenti']}")
print(f" media classe: {stats['media_classe']:.2f}")
print(f" miglior: {stats['miglior_studente']} ({stats ['media_migliore']: .2f})")
print(f" eccellenze: {stats['eccellenze']}")
print(f" insufficienti: {stats['insufficienti']}")

print("\n8. inserisci voto")
print(f" prima: Mario Rossi matematica = {studenti[0][1]}")
inserisci_voto(studenti, "Mario Rossi", 0, 9, 2)
print(f" dopo: Mario Rossi matematica = {studenti[0][1]}")

print("\n9. unisci classi")
nuova_classe = ["Carlo Rosa", [7, 8, 9], [8, 8, 8], [7, 9, 8]], ["Mario Rossi", [10, 10, 10], [10, 10, 10], [10, 10, 10]]# duplicato!]
classe_unita = unisci_classi(studenti, nuova_classe)
print(f" studenti classe 1: {len(studenti)}")
print(f" studenti classe 2: {len(nuova_classe)}")
print(f" studenti dopo unione (senza duplicati): {len(classe_unita)}")

print("\n10. resetta voti materia")
print(f" prima: Anna Neri inglese = {studenti[2][3]}")
resetta_voti_materia(studenti, 2)
#resetta inglese (index 2)
print(f" dopo: Anna Neri inglese = {studenti[2][3]}")


                  