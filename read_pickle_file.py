import pickle

infile = open("datastore.dat","rb")

datastore = pickle.load(infile)

print(type(datastore))

print(datastore)

input()

datastore["retail"] = [{'room-number': 105, 'use': 'closet', 'sq-ft': 50, 'price': 75}]

print(datastore)

outfile = open('datastore.dat','wb')
pickle.dump(datastore,outfile)