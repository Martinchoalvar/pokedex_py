pokedex = {
    1: {"name": "Bulbasaur", "type": "poison", "level": 5},
    2: {"name": "Ivysaur", "type": "poison", "level": 16},
    3: {"name": "Venusaur", "type": "poison", "level": 32},
    4: {"name": "Charmander", "type": "fire", "level": 5},
    5: {"name": "Charmeleon", "type": "fire", "level": 16},
    6: {"name": "Charizard", "type": "fire", "level": 36},
    7: {"name": "Squirtle", "type": "water", "level": 5},
    8: {"name": "Wartortle", "type": "water", "level": 16},
    9: {"name": "Blastoise", "type": "water", "level": 36},
    23: {"name": "Ekans", "type": "poison", "level": 10},
    24: {"name": "Arbok", "type": "poison", "level": 22},
    25: {"name": "Pikachu", "type": "electric", "level": 25},
    26: {"name": "Raichu", "type": "electric", "level": 30},
    37: {"name": "Vulpix", "type": "fire", "level": 12},
    38: {"name": "Ninetales", "type": "fire", "level": 28},
    54: {"name": "Psyduck", "type": "water", "level": 15},
    74: {"name": "Geodude", "type": "rock", "level": 12},
    75: {"name": "Graveler", "type": "rock", "level": 25},
    76: {"name": "Golem", "type": "rock", "level": 36},
    135: {"name": "Jolteon", "type": "electric", "level": 30}
}

print ("\n ---------------------------" \
       "\n ------ pokedeck v0.1 ------" \
       "\n ---------------------------" )

def proyect_pokemon():
    
    
    while True:
        try:
            x = int (input ( "\n 1) search pokemon " \
                             "\n 2) types " \
                             "\n 3) bag " \
                             "\n 4) register pokemon " \
                             "\n 5) exit \n _" ))
            if x == 1:
                 searchPokemon()
            elif x == 2:
                 types()
            elif x == 3 :
                 bag()
            elif x == 4:
                 registerpokemon()
            elif x == 5:
                 close()
                 break
            else:
                 print("\n ! Enter a valid option ! \n")
        except ValueError:
            print("\n ERROR __ the number entered is invalid type ! \n ")


def searchPokemon():
    pokemon = input ("\n what pokemon need search ? \n ").strip()

    encontrado = None

    if pokemon.isdigit():
        id_pokemon = int(pokemon)
        if id_pokemon in pokedex:
            encontrado = pokedex[id_pokemon]
    else: 
        for dates in pokedex.values():
            if dates["nombre"].lower() == pokemon.lower():
                encontrado = dates 
                break

    if encontrado:
        print(f"\n ! founded ! dates : {encontrado}")
        
    else:
        print("\n ! the pokemon is not registered !")

    back()

def types():
    pass

def bag():
    print("\n ----  bag  ---- "\
          "\n                 "\
          "\n _  pokeball     "\
          "\n _    berry      "\
          "\n _     egg       "\
          "\n                 ")
    back()

def registerPokemon():
    pass

def close ():
    print("\n ! thank you for visiting us, come back soon !")

def back():
    input("\n go back ? \n")


def main():
    proyect_pokemon()



if __name__ == "__main__":
    main()