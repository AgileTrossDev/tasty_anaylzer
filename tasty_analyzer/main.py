# Processes a Tasty Trade CVS file into a

# Impports
import csv
import click

import transaction





#############################################################################@##
# Main
#############################################################################@##

# Main Program
if __name__ == "__main__":
    click.clear()
    print("Starting the Tasty Trade Script")

    path = 'real_data/2017_real_master.csv'
    transaction_map = transaction.build_transaction_map(path)
    transaction.disp_transaction_map(transaction_map)

    # Exit
    print("Exiting")
