"""
    Date (YYYY-MM-DD): 2023-09-28
    Description: Maps a basic set of symbols (latin alphabet + arabic numbers) to a new list of "encrypt_symbols"
    > The user inputs a number -> Represents how many "special_symbols" comprise an encrypt_symbol
    > Example: if the user inputs 3, the letter "a" could become "!^&"
"""

#Built-in Imports
from itertools import chain
from random import choice


def main():
    #List of normal symbols -> the latin alphabet + numbers 0-9
    normal_symbols = list(chain(list(map(chr, range(97, 123))), list(map(chr, range(65, 90))), range(10)))
    #Normal symbols + special symbols -> ! " # $ % & ' ( ) * + , - . : ; < = > ? [ \ ] ^ _ { | }
    special_symbols = list(chain(list(map(chr, range(33, 47))), list(map(chr, range(58, 64))), list(map(chr, range(91, 96))), list(map(chr, range(123, 126))), normal_symbols))
    encrypt_symbol = ""
    encrypt_symbols = {}

    #Prompts user for a number -> Represents the number of special_symbols to represent each normal_symbols
    #Reprompts if integer value not inputted
    while True:
        try:
            num_of_symbols = int(input("How many symbols per encrypt_symbol (ie: if 3, \"a\" -> $#@): "))
            break
        except ValueError:
            pass

    #Converts each normal symbol to n encrypt_symbols -> n represents num of symbols
    for count, ch in enumerate(normal_symbols):
        for _ in range(num_of_symbols):
            encrypt_symbol += str(choice(special_symbols))
        encrypt_symbols[str(ch)] = encrypt_symbol
        encrypt_symbol = ""

    for key, val in encrypt_symbols.items():
        print(f"{key},{val}")

if __name__ == "__main__":
    main()
