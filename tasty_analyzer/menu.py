import sys, os
import transaction
import readchar

# Main definition - constants
menu_actions  = {}
transaction_map = {}
# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')

    print ("Welcome,\n")
    print ("Please choose the menu you want to start:")
    print ("1. Load CSV file from Tasty Trade")
    print ("2. Display all transactions")
    print ("3. Display all Underlyings traded")
    print ("4. Display Underlying history")
    print ("5. Calculate Underlying Profit")
    print ("\nQ. Quit")
    choice = input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return

# # Menu 1
# def menu1():
#     print ("Hello Menu 1 !\n")
#     print ("9. Back")
#     print ("0. Quit")
#     choice = input(" >>  ")
#     exec_menu(choice)
#     return
#
#
# # Menu 2
# def menu2():
#     print ("Hello Menu 2 !\n")
#     print ("9. Back")
#     print ("0. Quit")
#     choice = input(" >>  ")
#     exec_menu(choice)
#     return

# Back to main menu
def back():
    menu_actions['main_menu']()


def load_csv():
    csv_path = input(" path to csv >>  ")
    global transaction_map
    if os.path.isfile(csv_path):
        transaction_map = transaction.build_transaction_map(csv_path)
    else:
        print ("Following CSV File doe not exist: ", csv_path)
        dirpath = os.getcwd()
        print("current directory is : " + dirpath)


    press_key_to_continue()
    menu_actions['main_menu']()
    return


# Blocks until user presses the enter key to continue
# TODO:  Press anykey and don't display output
def press_key_to_continue():
    #key = input('Press any ENTER to continue')
    print("\n\nPress any key to continue")
    repr(readchar.readchar())


def disp_transactions():
    global transaction_map
    transaction.disp_transaction_map(transaction_map)

    press_key_to_continue()
    menu_actions['main_menu']()
    return

def disp_underlyings():
    global transaction_map
    transaction.disp_underlyings(transaction_map)

    press_key_to_continue()
    menu_actions['main_menu']()
    return


def disp_underlying_history():
    global transaction_map
    symbol = input('Underyling Symbol >> ')
    transaction.disp_underlying_history(transaction_map,symbol)

    press_key_to_continue()
    menu_actions['main_menu']()
    return


def calc_underlying_profit():
    global transaction_map
    symbol = input('Underyling Symbol >> ')
    transaction.calc_profit_for_underlying(transaction_map,symbol)

    press_key_to_continue()
    menu_actions['main_menu']()
    return


# def return_to_main_menu():
#     press_key_to_continue()
#     menu_actions['main_menu']()


# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': load_csv,
    '2': disp_transactions,
    '3': disp_underlyings,
    '4': disp_underlying_history,
    '5': calc_underlying_profit,
    '9': back,
    'Q': exit,
    'q': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
