# Simple Message Encryptor / Decryptor Built With Python

## Generates a simple encryption scheme used to encrypt or decrypt user-inputted messages.

This project is command-line based and writes a separate file containing an encryption scheme. The inputtable ASCII symbols (latin alphabet, spaces, Arabic numerals, etc) are individually mapped to a combination of N randomly selected symbols. Then, the user can convert their message into encrypted symbols or convert and encrypted phrase back into plain English. There is also an option to generate a new encryption scheme in the file. *DO NOT LOSE THE ORIGINAL ENCRYPTION SCHEME. IT IS THE ONLY WAY TO DECRYPT A MESSAGE AFTER IT IS ENCRYPTED.* Below is a summary of the flags:

* -h    -> Prints help menu
* -n N  -> Sets the number of symbols per encrypted symbol (must be between 2 and 7 - default value is 3)
        -> *If file is empty (does not contain an encryption scheme), this flag can be run alone*
        -> *If an encryption scheme already exists, this flag must be run with -r to work*
* -r    -> Generate a new encryption scheme - gives warning first
* -e    -> Allows the user to input a message to be encrypted using the current encryption scheme
* -d    -> Allows the user to input an encrypted message to be decrypted with the current encryption scheme

This program can be used practically to create stronger passwords without having to remember them. As long as you keep the encryption scheme and remember a simple password, it can be converted to a very complex password. Ie, hello -> tiO`g)YFk1AEq2iGlt}jjiGlt}jj(0D)Ln6

## How to install / use this program:

1. Install Python (programmed with Python 3.11.3)
2. Clone the project from GitHub and access the directory from the command-line
3. Make a virtual environment and install the required package
    -> python3 -m basic_encryptor_venv
    -> source basic_encryptor_venv/bin/activate (activate the virtual environment)
    -> pip install -r requirements.txt
4. Run the program with the following command
    -> python basic_encryptor.py - Generates the encryption scheme in a new file called "encryption_scheme.cvs"
5. For future runs, use the appropriate flags when running the program
6. When finished using the program deactive the virtual environment
    -> Run the command: deactivate

## Future implementation ideas / improvements:

> Make my own version of maskpass so no packages need to be imported -> Adjust the README.md later
> Make more code into functions
> Add typehints
> Unit test?
