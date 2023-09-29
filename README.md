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


## Future implementation ideas:

> Take the user's password. Allows the user to input their normal password and convert it to its encrypted form.
> Section program off into different parts depending on the flags used
> Make more code into functions
> Add typehints
