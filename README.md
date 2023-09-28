## Purpose:

Maps the latin alphabet (uppercase + lowercase) + arabic numbers into a new set of "encrypt_symbols". Each encrypt_symbol is comprised of n special_symbols.

special_symbols = latin alphabet (uppercase + lowercase) + arabic numbers + [! # $ % & ( ) * + , - . : ; < = > ? [ \ ] ^ _ { | }]

## Executing the program:

Use python or python3 command depending on your installation:

Command to execute program: python basic_encryption_scheme.py

## Future implementation ideas:


> Take the user's password. Allows the user to input their normal password and convert it to its encrypted form.

Flags:
> -h -> Prints help
> -n N -> Sets the number of special_symbols per encrypt_symbol
       -> Saves the encrypt_symbol scheme to a file

> If the user wants, they can generate a new list of encrypt_symbols
> *Do not save the user's password, convert it during runtime so they can copy/paste it*
> *Backup the encrypt key somehow???*
