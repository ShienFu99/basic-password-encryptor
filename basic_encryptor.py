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

    #List of symbols accepted in messages / encrypt_symbols -> Latin alphabet (case-insensitive) + arabic numerals + spaces + [! " # $ % & ' ( ) * + , - . : ; < = > ? [ \ ] ^ _ { | }]
    symbols = list(map(chr, range(32, 126)))
    #List of dictionaries -> each dictionary contains the original symbol and the new encrypt_symbol it maps to
    encryption_scheme = []
    #Flag that determines if a new encryption scheme needs to be generated
    generate = False

    #Initialize the command-line arguments
    args = init_command_line_args()

    #Try to open the file in "r" mode
    try:
        csv_file = open("encryption_scheme.csv")
        #If the file is empty, an encryption scheme needs to be generated
        if file_empty(csv_file):
            generate = True
            csv_file.close()
        #If the file is not empty, it is important that the user didn't run the -n flag on its own -> If they did, exit the program
        elif args.n != 3 and not args.r:
            csv_file.close()
            print("An encryption scheme already exists. To generate a new encryption scheme, use the -r flag.")
            proceed(1)
    #If no file exists, a file must be generated with a new encryption scheme
    except FileNotFoundError:
        generate = True
        #If -r flag used before a file exists, exit program (avoids conflicting messages later on)
        if args.r:
            print("Cannot generate a new encryption scheme while file DNE. Relaunch program without -r flag to generate a file.")
            proceed(1)

    #Whether the file exists or not, opening it in "a" mode ensures it gets created (without overwriting an already existing file)
    with open("encryption_scheme.csv", "a") as csv_file:
        #If the -r flag is used, confirm the user intends on generating a new encryption scheme
        if args.r:
           print("Are you sure you want to generate a new encryption scheme?")
           print("Any message encrypted with the previous scheme will no longer be decryptable!")
           choice = input("y or n: ").lower()
           print()

           #If they input "y", set generate flag to True - input other than "y" means "n"
           if choice == "y":
               clear_console()
               generate = True

        #If the generate flag is True by this point, clear any contents in the file and generate a new scheme
        if generate == True:
            print("Generating a new scheme.\n")
            sleep(1)
            clear_file(csv_file)
            generate_encryption_scheme(symbols, args.n, encryption_scheme, csv_file)
            print("New encryption scheme generated.")
            proceed(0)

    #The code below gets the encryption_scheme from the csv_file and stores it in a list ("encryption_scheme")
    #Skips this block if generate == True -> The scheme was generated during runtime and saved in encryption_scheme already
    with open("encryption_scheme.csv") as csv_file:
        csv_reader = DictReader(csv_file)

        #encryption_scheme is assigned an empty list again in case the user ran the program without generating a new scheme -> must be read from the file instead
        encryption_scheme = []

        #Parses the csv file's contents and creates individual dictionary entries to append to encryption_scheme
        for line in csv_reader:
            encryption_scheme.append({"symbol": line['symbol'], "encrypt_symbol": line['encrypt_symbol']})

    #If -e flag run, the user wants to encrypt a message
    if args.e:
        #Gets message from the user
        user_message = input("Input a message: ")
        encrypted_message = ""

        #Compare each symbol from the user-inputted message to the dictionary entries in the encryption_scheme
        #When the match is found, add the encrypt_symbol to the end of the encrypted_message -> accumulate until message is fully encrypted
        for ch in user_message:
            for d in encryption_scheme:
                if ch == d["symbol"]:
                    encrypted_message += d["encrypt_symbol"]

        #Print the message and proceed with the program
        print(f"Encrypted message: {encrypted_message}")
        proceed(0)

    #if -d flag inputted, the user wants to decrypt a message using a previous scheme
    if args.d:
        #Gets the encrypted message from the user
        encrypted_user_message = input("Input an encrypted message to be decrypted (if pasted, avoid copying line breaks): ")
        print()

        #Gets the user to input how many symbols were originally used per encrypt_symbol -> default is 3
        while True:
            try:
                num_of_symbols = input("How many symbols were used per encrypt_symbol (if -n flag wasn't used, press Enter): ")
                if not num_of_symbols:
                    num_of_symbols = "3"
                num_of_symbols = int(num_of_symbols)
                break
            except ValueError:
                pass

        #Compares the length of each encrypyt_symbol to num_of_symbols the user-inputted -> If they do not match, then the encryption scheme does not match the message
        #Ie, if each encrypt_symbol is comprised of 3 regular symbols, then they cannot be converted if the user inputs 4
        for d in encryption_scheme:
            if len(d["encrypt_symbol"]) != num_of_symbols:
                print("Number of symbols does match encryption scheme!")
                proceed(1)

        #Divides the encrypted_user_message into a list of segments -> Each segment is of length num_of_symbols -> Stores each segment into a list in encrypt_symbols
        encrypt_symbols = list(map(''.join, zip(*[iter(encrypted_user_message)] * num_of_symbols)))

        decrypted_user_message = ""

        #For each encrypt_symbol, check if it matches what exists in the encryption_scheme -> If it does not, the translation does not exist, resulting in symbols being omitted
        for encrypt_symbol in encrypt_symbols:
            for d in encryption_scheme:
                if encrypt_symbol ==  d["encrypt_symbol"]:
                    decrypted_user_message += d["symbol"]

        #If any symbols were omitted in the previous block of code, the length of the decrypted message will not equal the length of the encrypted message / num_of_symbols
        #Exits the program is this is the case
        if len(decrypted_user_message) != (len(encrypted_user_message) / num_of_symbols):
            print("Encrypted message does not match the encryption scheme!")
            proceed(1)

        #If no errors occured, print the decrypted message
        print(f"Decrypted message: {decrypted_user_message}")

        #Exit the program without error
        proceed(0)


#Working as intended
#Checks if file is empty
def file_empty(file):
    #If the first character of the file cannot be read, return True (file is empty), else False
    if not file.read(1):
        return True
    return False


#Working as intended
#Clears the console
def clear_console():
    #Clears the terminal when run
    system("clear")


#Working as intended
#Press enter to continue -> If int_exit is 1, exit the program, else program continues
def proceed(int_exit):
    choice = askpass("\nPress enter to continue...", mask="")
    clear_console()
    if int_exit:
        exit()

#Initializes the command-line args for this specific program
def init_command_line_args():
    parser = argparse.ArgumentParser(description="Maps a list of ordinary symbols to a list of \"encrypt_symbols\"")
    parser.add_argument("-n", default=3, help="number of symbols per encrypt_symbol - between 2 and 7 (inclusive)", type=int)
    parser.add_argument("-r", help="generate a new encryption scheme", action='store_true')
    parser.add_argument("-e", help="encrypt a message", action='store_true')
    parser.add_argument("-d", help="decrypt a previously encrypted message", action='store_true')

    args = parser.parse_args()

    #Value of -n N must be between 2 and 7 (1 is not secure enough, anything past 7 is impractical)
    try:
        if args.n < 2 or args.n > 7:
            raise ValueError
    except ValueError:
        exit("Number must be between 2 and 7.")

    return args


#Working as intended
#Clears a file
def clear_file(file):
    #Makes the file size 0 bytes
    file.truncate(0)
    #Repositions seek pointer to beginning of file
    file.seek(0)


#Write a docstring later
#Randomly pick N symbols from "symbols" list and returns the string as an encrypt_symbol
#Ie, if N is 3, 'a' -> '%H3'
def generate_encrypt_symbol(num_of_symbols, symbols):
    encrypt_symbol = ""

    #Runs loop N times (N is num_of_symbols) -> Randomly picks N symbols from "symbols" list and accumulates it in encrypyt_symbol
    for _ in range(num_of_symbols):
        encrypt_symbol += str(choice(symbols))
    return encrypt_symbol


#Generates an encryption scheme and saves it in a csv_file
def generate_encryption_scheme(symbols, num_of_symbols, encryption_scheme, csv_file):
    #This for-loop maps each normal symbol to an encrypt_symbol
    for count, ch in enumerate(symbols):

        #Generates an encrypt_symbol of size N (N = num_of_symbols)
        encrypt_symbol = generate_encrypt_symbol(num_of_symbols, symbols)

        #If the encrypt_symbol is a repeat of a previous one, generate a new one until it has a unique value
        for d in encryption_scheme:
            if encrypt_symbol == d["encrypt_symbol"]:
                while encrypt_symbol == d["encrypt_symbol"]:
                    encrypt_symbol = generate_encrypt_symbol(args.n, symbols)

        #Creates a dictionary entry -> "symbol": "encrypt_symbol" -> Appends it to the encryption_scheme list
        encryption_scheme.append({"symbol": str(ch), "encrypt_symbol": encrypt_symbol})

    csv_writer = DictWriter(csv_file, fieldnames=["symbol", "encrypt_symbol"])

    #Writes the fieldnames as the header of the file
    csv_writer.writeheader()

    #Writes each dictionary entry from encryption_scheme to the csv file
    for d in encryption_scheme:
        csv_writer.writerow(d)


if __name__ == "__main__":
    main()
