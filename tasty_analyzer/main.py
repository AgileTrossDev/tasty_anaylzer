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

    path = 'real_data/tastyworks_transactions_x6557_2017-01-01_2018-05-14.csv'
    transaction_map = transaction.build_transaction_map(path)
    transaction.disp_transaction_map(transaction_map)

    # Exit
    print("Exiting")
