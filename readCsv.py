import csv
def createCSVFile(text, nomeFile):
    with open(nomeFile + '.csv', 'a', newline='', errors='ignore') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(text)

nome = 'csv_partition'
path = input('Write the csv file path you want to read or split:\n')
pieces = input('How many lines do you want in each file?\n')
with open(path, 'r', newline='', encoding='UTF-8') as file:
    cont = 0;
    nomePartition = nome + str(cont)
    line = csv.reader(file)
    #createCSVFile(line)
    for row in line:

        createCSVFile(row, nomePartition)
        cont = cont + 1
        if cont % pieces == 0:
            nomePartition = nome + str(cont/pieces)
            print(str(cont/pieces) + ' csv files created')



