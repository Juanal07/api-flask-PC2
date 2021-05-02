import csv    

def scrap():

    with open('csv\/20210502_Centros_de_Atencion_Primaria.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            # print(', '.join(row))
            for i in row:
                print(i)
            print("\n")