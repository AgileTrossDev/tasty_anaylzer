import csv

class Transaction:
    def __init__(self,**kwargs):
        if kwargs is not None:
             for key, value in kwargs.items():
                setattr(self, key, value)

    def disp(self):
        print(self.date)


#############################################################################@##
# Builds a trasnaction map by openning a file and parsing it's records.
#############################################################################@##
def build_transaction_map(path):
    transaction_map = {}

    print ("Loading Transactions from File: ", path)
    with open(path, newline='') as csvfile:
         spamreader = csv.DictReader(csvfile)
         for row in spamreader:

             if 'Symbol' in row:
                key = row['Symbol'].split(" ")[0]
             else:
                print("Can't handle row: ", row)
                continue




             record = Transaction(    date = row['Date'],
                 trans_type = row['Type'],
                 action = row['Action'],
                 symbol = row['Symbol'],
                 instrument = row['Instrument Type'],
                 description = row['Description'],
                 value = row['Value'],
                 quantity = row['Quantity'],
                 avg_price = row['Average Price'],
                 commisions = row['Commissions'],
                 fees = row['Fees'],
                 multiplier = row['Multiplier'],
                 underlying = row['Underlying Symbol'],
                 expiration = row['Expiration Date'],
                 strike = row['Strike Price'],
                 option = row['Call or Put'])

             if key in transaction_map:
                transaction_map[key].append(record)
             else:
                transaction_map[key] = []
                transaction_map[key].append(record)

    print ("CSV File loaded!")
    return transaction_map

#############################################################################@##
# Displays a transaction map to stdout
#############################################################################@##
def disp_transaction_map(transaction_map):
    print ("Now Diplaying Transaciton Hash...")
    for k,v in transaction_map.items():
         print(k,':')
         for rec in v:
             rec.disp()


#############################################################################@##
# Display just the Underylings that exist in the Transaction Map
#############################################################################@##
def disp_underlyings(transaction_map):
    print ("Now diplaying Underlyings...")
    for k,v in transaction_map.items():
         print(k)




#############################################################################@##
# Display just the Underylings that exist in the Transaction Map
#############################################################################@##
def disp_underlying_history(transaction_map,symbol):
    print ("Now diplaying %s history...", symbol)

    for rec in transaction_map[symbol]:
        rec.disp()
