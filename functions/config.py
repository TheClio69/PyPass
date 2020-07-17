# Imports of required files.
from functions.generate import *
from colored import fg, bg, attr
# Color definitions for the following uses: information message (input and print), error messages, ...
red = fg('red')
white = fg('white')
# Definition of the "config" function.
def config():
    # First loop: containing all the "config" function as well as a verification of the properties defined by the user.
    while True:
        try:
            # Second loop: Ask the user how many passwords they want to generate.
            while True: 
                try:
                    numberofpasswords = input(white + '\nHow many passwords do you want to generate?\n')
                    if numberofpasswords.isnumeric():
                        if numberofpasswords <= "0":
                            print(red + 'Please enter a number greater than 0.')
                            pass
                        else:
                            break
                    else:  
                        print(red + 'Please enter only numbers.')
                        pass
                except:
                    pass
            # Third loop: Asks the user if the password must contain lowercase letters.
            while True: 
                try:
                    includelowercaseletters = input(white + '\nMust the password contain lowercase letters? Respond with "yes" or "no".\n')
                    if includelowercaseletters.isalpha():
                        if includelowercaseletters.lower() == "yes":
                            break
                        elif includelowercaseletters.lower() == "no":
                            break
                        else:
                            print(red + 'Please answer only with "yes" or "no".')
                    else:  
                        print(red + 'Please enter only letters.')
                        pass
                except:
                    pass
            # Fourth loop: Asks the user if the password must contain uppercase letters.
            while True: 
                try:
                    includecapitalletters = input(white + '\nMust the password contain capital letters? Respond with "yes" or "no".\n')
                    if includecapitalletters.isalpha():
                        if includecapitalletters.lower() == "yes":
                            break
                        elif includecapitalletters.lower() == "no":
                            break
                        else:
                            print(red + 'Please answer only with "yes" or "no".')
                    else:  
                        print(red + 'Please enter only letters.')
                        pass
                except:
                    pass
            # Fifth loop: Asks the user if the password must contain numbers.
            while True: 
                try:
                    includenumbers = input(white + '\nMust the password contain numbers? Respond with "yes" or "no".\n')
                    if includenumbers.isalpha():
                        if includenumbers.lower() == "yes":
                            break
                        elif includenumbers.lower() == "no":
                            break
                        else:
                            print(red + 'Please answer only with "yes" or "no".')
                    else:  
                        print(red + 'Please enter only letters.')
                        pass
                except:
                    pass
            # Sixth loop: Asks the user if the password must contain symbols.
            while True: 
                try:
                    includesymbols = input(white + '\nMust the password contain symbols? Respond with "yes" or "no".\n')
                    if includesymbols.isalpha():
                        if includesymbols.lower() == "yes":
                            break
                        elif includesymbols.lower() == "no":
                            break
                        else:
                            print(red + 'Please answer only with "yes" or "no".')
                    else:  
                        print(red + 'Please enter only letters.')
                        pass
                except:
                    pass
            # Checking if the properties of the password defined by the user are not all null (otherwise, password empty).
            if ((includelowercaseletters == "no") & (includecapitalletters == "no") & (includenumbers == "no") & (includesymbols == "no")):
                pass
            else:
                break
        except:
            pass
# --- End of file --- #