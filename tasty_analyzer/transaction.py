import csv

class Transaction:
    # date = row['Date'],
    # trans_type = row['Type'],
    # action = row['Action'],
    # symbol = row['Symbol'],
    # instrument = row['Instrument Type'],
    # description = row['Description'],
    # value = row['Value'],
    # quantity = row['Quantity'],
    # avg_price = row['Average Price'],
    # commisions = row['Commissions'],
    # fees = row['Fees'],
    # multiplier = row['Multiplier'],
    # underlying = row['Underlying Symbol'],
    # expiration = row['Expiration Date'],
    # strike = row['Strike Price'],
    # option
    def __init__(self,**kwargs):
        if kwargs is not None:
             for key, value in kwargs.items():
                setattr(self, key, value)

    # Simple display of date of transaction and description of it
    def disp(self):
        print('{0} | {1}'.format(self.date,self.description))


#############################################################################@##
# Builds a trasnaction map by openning a file and parsing it's records.
#
# TODO: Currently only processes Equity Options.  Need to build separate keys
#       for Equity, Equity Option, and Money Transfer, etc
#############################################################################@##
def build_transaction_map(path):
    transaction_map = {}

    print ("Loading Transactions from File: ", path)
    with open(path, newline='') as csvfile:
         spamreader = csv.DictReader(csvfile)
         for row in spamreader:

             if 'Underlying Symbol' in row:
                key = row['Underlying Symbol']
             else:
                print("Can't handle row: ", row)
                continue

             if ('Trade' ==row['Type'] and 'Equity Option' == row['Instrument Type']):

                 record = Transaction(date = row['Date'],
                     trans_type = row['Type'],
                     action = row['Action'],
                     symbol = row['Symbol'],
                     instrument = row['Instrument Type'],
                     description = row['Description'],
                     value = float(row['Value'].replace(",","")),
                     quantity = float(row['Quantity'].replace(",","")),
                     avg_price = float(row['Average Price'].replace(",","")),
                     commisions = float(row['Commissions'].replace(",","")),
                     fees = float(row['Fees'].replace(",","")),
                     multiplier = float(row['Multiplier'].replace(",","")),
                     underlying = row['Underlying Symbol'],
                     expiration = row['Expiration Date'],
                     strike = row['Strike Price'],
                     option = row['Call or Put'])
             else:
                  continue

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
def calc_profit_for_underlying(transaction_map,symbol):
    print ("Now calculating the profit for Underlying %s...", symbol)

    result = 0
    for rec in transaction_map[symbol]:
        print ("{} {} {} at {}".format(rec.action,symbol,rec.option,rec.value) )
        result = result + rec.quantity * ( rec.value + rec.commisions + rec.fees)
        #result = result + rec.quantity * ( rec.value )
        #print ("Updated Result: ",result)

    print ("\n\nTOTAL (including Fees and commission): ", result)

#############################################################################@##
# Display just the Underylings that exist in the Transaction Map
#############################################################################@##
def disp_underlying_history(transaction_map,symbol):
    print ("Now diplaying %s history...", symbol)

    for rec in transaction_map[symbol]:
        rec.disp()
