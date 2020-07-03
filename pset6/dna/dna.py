from sys import argv
import csv

if len(argv) != 3:
    print('Usage: python dna.py data.csv sequence.txt')
    exit(0)

csv_file, txt_file = argv[1], argv[2]
memory = []  # To store csv datas
seq = ''  # To store dna sequences
count_of_str = []  # To store count of each str
STR = []

args = argv[1].split('/')
database = args[1]

with open(csv_file) as csvfile:  # read the data from sequences
    reader = csv.DictReader(csvfile)
    if database == 'large.csv':
        for row in reader:
            memory.append([row['name'], row['AGATC'], row['TTTTTTCT'], row['AATG'],
                           row['TCTAG'], row['GATA'], row['TATC'], row['GAAA'], row['TCTG']])
        STR = ['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']

    elif database == 'small.csv':
        for row in reader:
            memory.append([row['name'], row['AGATC'], row['AATG'], row['TATC']])
        STR = ['AGATC', 'AATG', 'TATC']

with open(txt_file) as seq_file:  # read the data from database
    seq = seq_file.readline()  # store it in the seq

for i in range(len(STR)):  # number of longest consecutively repeated sequences
    counter = 0
    pattern = STR[i]
    while pattern in seq:
        counter += 1
        pattern += STR[i]
    count_of_str.append(counter)

count_of_str = [str(x) for x in count_of_str]


def check(count_of_str, memory):  # compare the values
    for i in range(len(memory)):
        if count_of_str == memory[i][1:]:
            return memory[i][0]


if check(count_of_str, memory) != None:
    print(check(count_of_str, memory))
else:
    print('No match')