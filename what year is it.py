import time                                             # imports time module
def age(ask):                                           # defining calculating function
    year = time.localtime().tm_year                     # get year
    num = year - ask                                    # calculation itself
    print(f"You are {num} years old.")                  # prints result
    return                                              # ends function

def main():                                             # define the main program
    while True:                                         # while True loops indefinitely
        ask = int(input("\nWhat year were you born? ")) # asks what year user was born
        age(ask)                                        # performs calculations from calculating function
    
if __name__ == "__main__":                              # creates a condition for the main program to start
    main()                                              # the main program
