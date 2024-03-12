mass = 5
quest = input("che pianeta vuoi scegliere?")
gravita = {
    "mercurio": 3.7,
    "venere": 8.8,
    "terra": 9.8,
    "marte": 3.7,
    "giove": 24.8,
    "saturno": 8.9,
    "uranio": 8.7,
    "nettuno": 11
}

if quest in gravita:
    print(f"la pallina di massa {mass}kg dentro il pianeta {quest} ha un peso pari ha {mass*gravita[quest]}")
