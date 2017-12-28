import csv

print("Starting the Tasty Trade Script")

transaction_map = {}

with open('real_data/2017_real_master.csv', newline='') as csvfile:
     spamreader = csv.DictReader(csvfile)
     for row in spamreader:
         key = row['Symbol'].split(" ")[0]
         if key in transaction_map:
            transaction_map[key].append(row['Date'])
         else:
            transaction_map[key] = []
            transaction_map[key].append(row['Date'])


print ("Now Diplaying Transaciton Hash...")
for k,v in transaction_map.items():
     print(k,':',v)


print("Exiting")
