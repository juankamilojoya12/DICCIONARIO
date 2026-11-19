print("Bienvenido a mi diccionario")

meme_dict = {
    "CRINGE": "Algo raro o vergonzoso",
    "LOL": "Algo gracioso",
    "XD": "Expresión de risa",
    "BRO": "Amigo",
    "GG": "Buena partida",
    "NOOB": "Jugador principiante"
}

for i in range(5):
    word = input("Escribe una palabra: ").upper()

    if word in meme_dict:
        print(meme_dict[word])
    else:
        print("No conozco esa palabra")
