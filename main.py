import csv

print("Starting the Tasty Trade Script")

transaction_hash = []

with open('real_data/2017_real_master.csv', newline='') as csvfile:
     spamreader = csv.DictReader(csvfile)
     for row in spamreader:
         #print(', '.join(row))
         print(row['Date'], row['Symbol'])
print("Exiting")
