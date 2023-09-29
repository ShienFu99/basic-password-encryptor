## Purpose:

> First run = generate encryption scheme -> "Encryption scheme saved."
> Subsequent runs = convert regular password using current encryption scheme
> *Can also regenerate previous scheme -> Offer a warning to the user

> How is the scheme saved -> In a regular file -> Stored locally
> How are passwords stored?





This program maps the latin alphabet (uppercase + lowercase) + the arabic numbers into a new list of "encrypt_symbols". Each encrypt_symbol is comprised of n "special_symbols", where n is between 2 and 7.

special_symbols = latin alphabet (uppercase + lowercase) + arabic numbers + [! " # $ % & ' ( ) * + , - . : ; < = > ? [ \ ] ^ _ { | }]

By typing in your regular password, you can get the encrypted form and only have to remember the original version.


## Executing the program:

Use python or python3 command depending on your installation:

Command to execute program: python basic_encryption_scheme.py

## Future implementation ideas:

> Toggle visibility -> Display as ***** or chars
> Take the user's password. Allows the user to input their normal password and convert it to its encrypted form.

Flags:
> -h -> Prints help
> -n N -> Sets the number of special_symbols per encrypt_symbol
       -> Saves the encrypt_symbol scheme to a file
> -r -> Reuse scheme?

> Separate generating encryption scheme vs converting password

> If the user wants, they can generate a new list of encrypt_symbols
> *Do not save the user's password, convert it during runtime so they can copy/paste it*
> *Backup the encrypt key somehow???*
