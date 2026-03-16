f = open("date.txt", mode = 'r', encoding = 'utf-8')    # necesita inchidere manuala a fisierului
for line in f:
    print(line.strip())
f.close()


with open("date.txt", mode = 'r', encoding = 'utf-8') as f:  # fisierul se inchide automat
    for line in f:
        print(line.strip())

