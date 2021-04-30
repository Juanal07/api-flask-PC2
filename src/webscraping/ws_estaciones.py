import csv

def scrap():
    with open('listado-estaciones-completo-sel.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            code = row[0]
            # codeInt = int(code) 
            name = row[1]
            dir = row[2]
            city = row[3]
            cercanias = row[4]
            if cercanias=="SI":
                cercaniasInt = 1
            else:
                cercaniasInt = 0
            feve = row[5]
            if feve =="NO":
                feveInt = 0
            else:
                feveInt = 1
            print(code,", ",name,", ",name,", ",dir,", ",city,", ",cercaniasInt,", ",feveInt)
            # print(', '.join(row))



    
    return None