#Built-in Imports
import argparse
from csv import DictReader, DictWriter
from itertools import chain #chain() is no longer used
from os import system
from random import choice
from sys import exit
from time import sleep


#3rd-party Imports
from maskpass import askpass


def main():
    #Clears console -> User doesn't see the command used to execute the program
    clear_console()

    #List of symbols accepted in messages / encrypt_symbols -> Latin alphabet (case-insensitive) + arabic numerals + [! " # $ % & ' ( ) * + , - . : ; < = > ? [ \ ] ^ _ { | }]
    symbols = list(map(chr, range(33, 126)))
    #Holds a list of dictionaries -> each dictionary contains the original symbol and the new encrypt_symbol it maps to
    encryption_scheme = []
    #Flag that determines if a new encryption scheme needs to be generated
    generate = False

    args = init_command_line_args()

    try:
        csv_file = open("encryption_scheme.csv")
        if file_empty(csv_file):
            generate = True
        csv_file.close()
    except FileNotFoundError:
        generate = True


    #Opening the filename in "a" mode creates it if it doesn't already exist, allowing it to be checked for file contents
    #If the file is empty or the user wants a new scheme, a new encryption_scheme will be generated and saved to the file
    with open("encryption_scheme.csv", "a") as csv_file:
        #if user inputs -r flag -> regenerate file
        if args.r:
           print("Are you sure you want to generate a new encryption scheme?")
           print("Any message encrypted with the previous scheme will no longer be decryptable!")
           choice = input("y or n: ").lower()
           print()
           if choice == "y":
               clear_console()
               generate = True
           else:
               pass

        if generate == True:
            print("Generating a new scheme.\n")
            sleep(1)
            clear_file(csv_file)
            generate_encryption_scheme(symbols, args.n, encryption_scheme, csv_file)

    #Opening the file in "r" mode will not throw an exception here as the previous block of code writes a file with the same name
    with open("encryption_scheme.csv") as csv_file:
        csv_reader = DictReader(csv_file)
        encryption_scheme = []
        for line in csv_reader:
            encryption_scheme.append({"symbols": line['symbol'], "encrypt_symbol": line['encrypt_symbol']})

    user_message = input("Input a message: ")
    encrypted_message = ""

    for ch in user_message:
        for d in encryption_scheme:
            if ch == d["symbols"]:
                encrypted_message += d["encrypt_symbol"]

    print(f"Encrypted message: {encrypted_message}")

    proceed()
    clear_console()


#Working as intended
def file_empty(file):
    #If the first character of the file cannot be read, return True (file is empty), else False
    if not file.read(1):
        return True
    return False


#Working as intended
def clear_console():
    #Clears the terminal when run
    system("clear")


#Working as intended
def proceed():
    choice = askpass("\nPress enter to continue...", mask="")


def init_command_line_args():
    parser = argparse.ArgumentParser(description="Maps a list of ordinary symbols to a list of \"encrypt_symbols\"")
    parser.add_argument("-n", default=3, help="number of symbols per encrypt_symbol - between 2 and 7 (inclusive)", type=int)
    parser.add_argument("-r", help="reuse previous scheme", action='store_true')
    parser.add_argument("-d", help="decrypt a previously encrypted message", action='store_true')

    args = parser.parse_args()

    try:
        if args.n < 2 or args.n > 7:
            raise ValueError
    except ValueError:
        exit("Number must be between 2 and 7.")

    return args


#Working as intended
def clear_file(file):
    #Makes the file size 0 bytes
    file.truncate(0)
    #Repositions seek pointer to beginning of file
    file.seek(0)


#Write a docstring later -> Randomly pick N symbols from symbols and returns the string as an encrypt_symbol
def generate_encrypt_symbol(num_of_symbols, symbols):
    encrypt_symbol = ""
    for _ in range(num_of_symbols):
        encrypt_symbol += str(choice(symbols))
    return encrypt_symbol


def generate_encryption_scheme(symbols, num_of_symbols, encryption_scheme, csv_file):
    #Maps each normal symbol into an encrypt_symbols
    for count, ch in enumerate(symbols):

        #Generates an encrypt_symbol of size num_of_symbols (args.n)
        encrypt_symbol = generate_encrypt_symbol(num_of_symbols, symbols)

        #If the encrypt_symbol is a repeat of a previous one, generate a new one until it's a unique value
        for d in encryption_scheme:
            if encrypt_symbol == d["encrypt_symbol"]:
                while encrypt_symbol == d["encrypt_symbol"]:
                    encrypt_symbol = generate_encrypt_symbol(args.n, symbols)

        #Creates a dictionary entry -> "symbol": "encrypt_symbol"
        encryption_scheme.append({"symbol": str(ch), "encrypt_symbol": encrypt_symbol})

    csv_writer = DictWriter(csv_file, fieldnames=["symbol", "encrypt_symbol"])

    csv_writer.writeheader()

    for d in encryption_scheme:
        csv_writer.writerow(d)


if __name__ == "__main__":
    main()