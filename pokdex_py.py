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
                 register_pokemon()
            elif x == 5:
                 close()
                 break
            else:
                 print("\n ! Enter a valid option ! \n")
        except ValueError:
            print("\n ERROR __ the number entered is invalid type ! \n ")



def close ():
    print("\n ! thank you for visiting us, come back soon !")

def back():
    input("\n go back ? \n")


def main():
    proyect_pokemon()



if __name__ == "__main__":
    main()