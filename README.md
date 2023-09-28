## Purpose:

Maps the latin alphabet (uppercase + lowercase) + arabic numbers into a new set of "encrypt_symbols". Each encrypt_symbol is comprised of n special_symbols.

special_symbols = latin alphabet (uppercase + lowercase) + arabic numbers + [! " # $ % & ' ( ) * + , - . : ; < = > ? [ \ ] ^ _ { | }]

## Executing the program:

Use python or python3 command depending on your installation:

Command to execute program: python basic_encryption_scheme.py

## Future implementation ideas:

> Prevent list from containing duplicates
> Saves the encrypt_symbols in a file and takes the user's password. Using command-line arguments, allows the user to input their normal password and convert it to its encrypted form.

Flags:
> -h -> Prints helps
> -n N -> Takes sets the number of special symbols per encrypt_symbol
       -> Saves the encrypt_symbol scheme to a file
> -c -> Prompts the user for their password and converts it
     -> If encrypt_symbol scheme is not set yet, the user must set one first

> If the user wants, they can generate a new list of encrypt_symbols
> *Do not save the user's password, convert it during runtime so they can copy/paste it*
> *Backup the encrypt key somehow???*
