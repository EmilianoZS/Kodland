meme_dict= {"LOL" : "Una respuesta a algo gracioso",
            "CRINGE" : "Algo raro o embarazoso",
            "ROFL" : "Una respuesta a una broma",
            "SHEESH" : "Ligera desaprobación",
            "CREEPY" : "Aterrador, siniestro",
            "AGGRO" : "Ponerse agresivo/enojado"}
while True:
    word=input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
        Salida=input("Quieres salir?")
    else:
        print("Lo sentimos, esa palabra no se encuentra en el diccionario")
        print("Pero si sabes la respuesta agregala!!")
        Word_n=input("Nueva palabra(En mayusculas):")
        if Word_n in meme_dict.keys():
            print("Esa palabra ya esta agregada")
        elif Word_n not in meme_dict.keys():
            Sig=input("Significado:")
            New_word ={Word_n : Sig}
            meme_dict.update(New_word)
    if Salida=="Si":
        break
