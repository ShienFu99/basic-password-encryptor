"""
    Date (YYYY-MM-DD): 2023-09-28
    Description: Maps a basic set of symbols (latin alphabet + arabic numbers) to a new list of "encrypt_symbols"
    > The user inputs a number -> Represents how many "special_symbols" comprise an encrypt_symbol
    > Example: if the user inputs 3, the letter "a" could become "!^&"
"""

#Built-in Imports
import argparse
from csv import DictReader, DictWriter
from itertools import chain
from random import choice
from sys import exit


def main():
    #List of normal symbols -> the latin alphabet + numbers 0-9
    normal_symbols = list(chain(list(map(chr, range(97, 123))), list(map(chr, range(65, 90))), range(10)))
    #Normal symbols + special symbols -> ! " # $ % & ' ( ) * + , - . : ; < = > ? [ \ ] ^ _ { | }
    special_symbols = list(chain(list(map(chr, range(33, 47))), list(map(chr, range(58, 64))), list(map(chr, range(91, 96))), list(map(chr, range(123, 126))), normal_symbols))

    #encrypt_scheme hold a list of dictionaries -> each dictionary contains the original symbol and the new combination of special_symbols to map it too
    encrypt_scheme = []

    generate = False


    parser = argparse.ArgumentParser(description="Maps a list of ordinary symbols to a list of \"encrypt_symbols\"")
    parser.add_argument("-n", default=3, help="number of special_symbols per encrypt_symbol - between 2 and 7 (inclusive)", type=int)
    parser.add_argument("-r", help="reuse previous scheme", action='store_true')

    args = parser.parse_args()

    try:
        if args.n < 2 or args.n > 7:
            raise ValueError
    except ValueError:
        exit("Number must be between 2 and 7.")

    try:
        csv_file = open("encrypt_scheme.csv")
        if file_empty(csv_file):
            generate = True
        csv_file.close()
    except FileNotFoundError:
        generate = True


    #Opening the filename in "a" mode creates it if it doesn't already exist, allowing it to be checked for file contents
    #If the file is empty or the user wants a new scheme, a new encrypt_scheme will be generated and saved to the file
    with open("encrypt_scheme.csv", "a") as csv_file:
        #if user inputs -r flag -> regenerate file
        if args.r or generate == True:
            print("User wants to generate a new scheme.")
            clear_file(csv_file)
            generate_encrypt_scheme(normal_symbols, special_symbols, args.n, encrypt_scheme, csv_file)

    #Opening the file in "r" mode will not throw an exception here as the previous block of code writes a file with the same name
    with open("encrypt_scheme.csv") as csv_file:
        csv_reader = DictReader(csv_file)
        encrypt_scheme = []
        for line in csv_reader:
            encrypt_scheme.append({"normal_symbol": line['normal_symbol'], "encrypt_symbol": line['encrypt_symbol']})

    user_password = input("Input your regular password: ")
    encrypted_password = ""

    for ch in user_password:
        for d in encrypt_scheme:
            if ch == d["normal_symbol"]:
                encrypted_password += d["encrypt_symbol"]

    print(f"Encrypted password: {encrypted_password}")


#Working as intended
def file_empty(file):
    #If the first character of the file cannot be read, return True (file is empty), else False
    if not file.read(1):
        return True
    return False


#Working as intended
def clear_file(file):
    #Makes the file size 0 bytes
    file.truncate(0)
    #Repositions seek pointer to beginning of file
    file.seek(0)


#Write a docstring later -> Randomly pick N symbols from special_symbols and returns the string as an encrypt_symbol
def generate_encrypt_symbol(num_of_symbols, special_symbols):
    encrypt_symbol = ""
    for _ in range(num_of_symbols):
        encrypt_symbol += str(choice(special_symbols))
    return encrypt_symbol


def generate_encrypt_scheme(normal_symbols, special_symbols, num_of_symbols, encrypt_scheme, csv_file):
    #Maps each normal symbol into an encrypt_symbols
    for count, ch in enumerate(normal_symbols):

        #Generates an encrypt_symbol of size num_of_symbols (args.n)
        encrypt_symbol = generate_encrypt_symbol(num_of_symbols, special_symbols)

        #If the encrypt_symbol is a repeat of a previous one, generate a new one until it's a unique value
        for d in encrypt_scheme:
            if encrypt_symbol == d["encrypt_symbol"]:
                while encrypt_symbol == d["encrypt_symbol"]:
                    encrypt_symbol = generate_encrypt_symbol(args.n, special_symbols)

        #Creates a dictionary entry -> "normal_symbol": "encrypt_symbol"
        encrypt_scheme.append({"normal_symbol": str(ch), "encrypt_symbol": encrypt_symbol})

    csv_writer = DictWriter(csv_file, fieldnames=["normal_symbol", "encrypt_symbol"])

    csv_writer.writeheader()

    for d in encrypt_scheme:
        csv_writer.writerow(d)


if __name__ == "__main__":
    main()
