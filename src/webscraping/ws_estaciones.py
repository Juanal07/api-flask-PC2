import csv
import mariadb
import sys

def scrap():
    #Conexión con BBDD
    try:
        conn = mariadb.connect(
            user="pr_softlusion",
            password="Softlusion",
            host="2.139.176.212",
            port=3306,
            database="prsoftlusion"
        )
        print("Conexión a BBDD")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
    
    with open('listado-estaciones-completo-sel.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            code = row[0]
            # codeInt = int(code) 
            name = row[1]
            dir = row[2]
            city:str = row[3]
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
            idMunicipality = 0
            # query = ("SELECT idMunicipality FROM municipality WHERE name= '%s'")
            # tupla:tuple = (city)
            # cur.execute(query,tupla)
            # cur.execute("SELECT idMunicipality FROM municipality WHERE name=?", (city))
            query = "SELECT idMunicipality FROM municipality WHERE name= '"+ city+ "'"
            cur.execute(query)
            for (idMunicipality) in cur:
                print(idMunicipality)
            # print(', '.join(row))


    # conn.commit()
    conn.close()
    return None