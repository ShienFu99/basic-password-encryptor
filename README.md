## Purpose:
This program takes a user's message and encrypts it using a simple encryption scheme. The user can input any message that contains symbols from the latin alphabet (case-insensitively), the arabic numerals, or any of the following symbols -> [! " # $ % & ' ( ) * + , - . : ; < = > ? [ \ ] ^ _ { | }]

The encryption scheme is created based on the user-inputted number, else it defaults to 3. This number represents the number of symbols that are randomly combined to create a new "encrypt_symbol". The regular symbols are mapped to these encrypt symbols for future usage. Afterwards, the user has the option to decrypt their message using the previously saved scheme, or generate a new scheme to use. It is important that the original scheme used to encrypt a message is not lost, or it cannot be reobtained.

> First run = generate encryption scheme
> Subsequent runs = Input a message and encrypt it with the previously generated encryption scheme OR decrypt a message using the previously encryption scheme
> *Can also generate a new scheme -> Offers a warning to the user


## Executing the program:

Use python or python3 command depending on your installation:

Command to execute program: python basic_encryption_scheme.py


## Flags:
> -h -> Prints help
> -n N -> Sets the number of special_symbols per encrypt_symbol
       -> Saves the encrypt_symbol scheme to a file
> -r -> Reuse scheme?
> -d -> Decrypt a previously encrypted message


## Future implementation ideas / improvements:

> Section program off into different parts depending on the flags used

    # Problem: -r being able to run without -n
    # New flag: -e (encrypt a message) -> Ensure the encryption_scheme gets read in for -d if -e is not run at the same time

> Make more code into functions
> Add typehints



1. If file can be opened and it's empty, autogenerate an encryption scheme
    -> Else file can't be opened -> Write a new file + autogenerate an encryption scheme
---
2. If -r flag used, prompt if user wants to generate a new encryption scheme
    3. Empty the file -> Write a new encryption scheme
---

4. Open the file with the encryption scheme -> save it locally in a variable

---

5. Prompt user for a message -> Encrypts the message

---
6. If -d flag used, prompt the user for an encrypted message
    #-> Prompt user for the number of symbols used in the original message (blank = default value)
    -> Might require the user to input their previous user number (extra security / ensures the decoding process is done correctly)
    -> If the encryption scheme doesn't match the message or the length is incorrect, print specific messages for the user
