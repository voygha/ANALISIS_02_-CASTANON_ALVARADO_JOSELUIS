"""register_id,direction,origin,destination,year,date,product,transport_mode,company_name,total_value
id del registro
"""

import csv

exportaciones= []
importaciones=[]
exportacionessea= []
importacionessea=[]
exportacionesair= []
importacionesair=[]
exportacionesrail= []
importacionesrail=[]
exportacionesroad= []
importacionesroad=[]
sea=[]
sea=[]
sea=[]
sea=[]
air=[]
rail=[]
road=[]


with open("synergy_logistics_database.csv", "r") as archivo_csv:
    lector= csv.reader(archivo_csv)
    #cuantas exportacioones se realizaron en total
    #si ejecutamos así, es una lista por cada linea
    
    for linea in lector:
        if linea[9] == "total_value":
            continue

        #CALCULO DEL TOTAL DE ESPORTACIONES E IMPORTACIONES
        if linea[1]=="Exports":
            exportaciones.append(int(linea[9]))
        if linea[1]=="Imports":
            importaciones.append(int(linea[9]))


        #CALCULO DE EXPORTACIONES,IMPORTACIONES POR MAR, Y CALCULO DE CUANTAS VECES SE EXPORTO O IMPORTO POR MAR
        if linea[7] == "Sea":
            sea.append(1)
        if linea[1]=="Exports" and linea[7] == "Sea":
            exportacionessea.append(int(linea[9]))
        if linea[1]=="Imports" and linea[7] == "Sea":
            importacionessea.append(int(linea[9]))

        #CALCULO DE EXPORTACIONES,IMPORTACIONES POR MAR, Y CALCULO DE CUANTAS VECES SE EXPORTO O IMPORTO POR AIRE
        if linea[7] == "Air":
            air.append(1)
        if linea[1]=="Exports" and linea[7] == "Air":
            exportacionesair.append(int(linea[9]))
        if linea[1]=="Imports" and linea[7] == "Air":
            importacionesair.append(int(linea[9]))

        #CALCULO DE EXPORTACIONES,IMPORTACIONES POR MAR, Y CALCULO DE CUANTAS VECES SE EXPORTO O IMPORTO POR CARRIL
        if linea[7] == "Rail":
            rail.append(1)
        if linea[1]=="Exports" and linea[7] == "Rail":
            exportacionesrail.append(int(linea[9]))
        if linea[1]=="Imports" and linea[7] == "Rail":
            importacionesrail.append(int(linea[9]))

        #CALCULO DE EXPORTACIONES,IMPORTACIONES POR MAR, Y CALCULO DE CUANTAS VECES SE EXPORTO O IMPORTO POR CARRETERA
        if linea[7] == "Road":
            road.append(1)
        if linea[1]=="Exports" and linea[7] == "Road":
            exportacionesroad.append(int(linea[9]))
        if linea[1]=="Imports" and linea[7] == "Road":
            importacionesroad.append(int(linea[9]))    
        
print("El total de ingresos de las exportaciones es: ", sum(exportaciones))
print("El total de ingresos de las importaciones es: ", sum(importaciones))
print("\n\n")

print("El total de veces en Mar en importaciones y exportaciones es: ", sum(sea))
a=sum(exportacionessea)
b=sum(importacionessea)
print("El total en las ganancias de exportaciones por mar es: ", sum(exportacionessea))
print("El total en las ganancias de importaciones por mar es: ", sum(importacionessea))
print("El total en ganancias en importaciones y exportaciones en Mar es: ", a+b)
print("\n")

print("El total de veces en Aire en importaciones y exportaciones es: ", sum(air))
a=sum(exportacionesair)
b=sum(importacionesair)
print("El total en las ganancias de exportaciones por aire es: ", sum(exportacionesair))
print("El total en las ganancias de importaciones por aire es: ", sum(importacionesair))
print("El total en ganancias en importaciones y exportaciones en Aire es: ", a+b)
print("\n")

print("El total de veces en carril en importaciones y exportaciones es: ", sum(rail))
a=sum(exportacionesrail)
b=sum(importacionesrail)
print("El total en las ganancias de exportaciones por carril es: ", sum(exportacionesrail))
print("El total en las ganancias de importaciones por carril es: ", sum(importacionesrail))
print("El total en ganancias en importaciones y exportaciones en Carril es: ", a+b)
print("\n")

print("El total de veces en Carretera en importaciones y exportaciones es: ", sum(road))
a=sum(exportacionesroad)
b=sum(importacionesroad)
print("El total en las ganancias de exportaciones por carretera es: ", sum(exportacionesroad))
print("El total en las ganancias de importaciones por carretera es: ", sum(importacionesroad))
print("El total en ganancias en importaciones y exportaciones en Carretera es: ", a+b)
print("\n")
#print("El total es")


exp_vietnam= []
malaysia=[]
singapore=[]
italy=[]
austria=[]
mexico=[]
switzerland=[]
brazil=[]
australia=[]
unitedkingdom=[]
india=[]
spain=[]
china=[]
japan=[]
russia=[]
south_korea=[]
usa=[]
netherlands=[]
france=[]
germany=[]
canada=[]
belgium=[]
with open("synergy_logistics_database.csv", "r") as archivo_csv:
    lector= csv.DictReader(archivo_csv)
    
    
    for linea in lector:
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Vietnam":
            exp_vietnam.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Malaysia":
            malaysia.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Singapore":
            singapore.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Italy":
            italy.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Austria":
            austria.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Mexico":
            mexico.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Switzerland":
            switzerland.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Brazil":
            brazil.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Australia":
            australia.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "United Kingdom":
            unitedkingdom.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "India":
            india.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Spain":
            spain.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "China":
            china.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Japan":
            japan.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Russia":
            russia.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "South Korea":
            south_korea.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "USA":
            usa.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Netherlands":
            netherlands.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "France":
            france.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Germany":
            germany.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Canada":
            canada.append(int(linea["total_value"]))
        #CALCULA EL TOTAL DE IMPORTACIONES Y EXPORTACIONES DEL PAIS DE ORIGEN QUE SE LE DA EN EL PARAMETRO
        if linea["origin"] == "Belgium":
            belgium.append(int(linea["total_value"]))
    
#print(exp_vietnam)
print("Exportaciones e Importaciones totales de Vietnam: ", sum(exp_vietnam))
print("Exportaciones e Importaciones totales de Malaysia: ", sum(malaysia))
print("Exportaciones e Importaciones totales de Singapore: ", sum(singapore))
print("Exportaciones e Importaciones totales de Italy: ", sum(italy))
print("Exportaciones e Importaciones totales de Austria: ", sum(austria))
print("Exportaciones e Importaciones totales de Mexico: ", sum(mexico))
print("Exportaciones e Importaciones totales de Switzerland: ", sum(switzerland))
print("Exportaciones e Importaciones totales de Brazil: ", sum(brazil))
print("Exportaciones e Importaciones totales de Australia: ", sum(australia))
print("Exportaciones e Importaciones totales de United Kindom: ", sum(unitedkingdom))
print("Exportaciones e Importaciones totales de India: ", sum(india))
print("Exportaciones e Importaciones totales de Spain: ", sum(spain))
print("Exportaciones e Importaciones totales de China: ", sum(china))
print("Exportaciones e Importaciones totales de Japan: ", sum(japan))
print("Exportaciones e Importaciones totales de Russia: ", sum(russia))
print("Exportaciones e Importaciones totales de South Korea: ", sum(south_korea))
print("Exportaciones e Importaciones totales de USA: ", sum(usa))
print("Exportaciones e Importaciones totales de Netherlands: ", sum(netherlands))
print("Exportaciones e Importaciones totales de France: ", sum(france))
print("Exportaciones e Importaciones totales de Germany: ", sum(germany))
print("Exportaciones e Importaciones totales de Canada: ", sum(canada))
print("Exportaciones e Importaciones totales de Belgium: ", sum(belgium))

"""
LISTA ORDENADA DE LAS EXPORTACIONES E IMPORTACIONES TOTALES POR PAIS
1.	Exportaciones e Importaciones totales de China:  45210046000 
2.	Exportaciones e Importaciones totales de USA:  23646306000 
3.	Exportaciones e Importaciones totales de Japan:  20042976000 
4.	Exportaciones e Importaciones totales de Germany:  15593233000 
5.	Exportaciones e Importaciones totales de Russia:  14074000000 
6.	Exportaciones e Importaciones totales de Canada:  11253000000 
7.	Exportaciones e Importaciones totales de Italy:  6634684000 
8.	Exportaciones e Importaciones totales de Spain:  6419000000 
9.	Exportaciones e Importaciones totales de México:  6040755000 
10.	Exportaciones e Importaciones totales de Vietnam:  540000000  
11.	Exportaciones e Importaciones totales de Netherlands:  4120369000 
12.	Exportaciones e Importaciones totales de Singapore:  4017684000 
13.	Exportaciones e Importaciones totales de Malaysia:  3560000000 
14.	Exportaciones e Importaciones totales de United Kindom:  3025612000 
15.	Exportaciones e Importaciones totales de Brazil:  2763000000 
16.	Exportaciones e Importaciones totales de India:  2626000000 
17.	Exportaciones e Importaciones totales de Belgium:  2588000000 
18.	Exportaciones e Importaciones totales de Australia:  2570000000 
19.	Exportaciones e Importaciones totales de Switzerland:  2154000000 
20.	Exportaciones e Importaciones totales de France:  19930332000 
21.	Exportaciones e Importaciones totales de South Korea:  18510146000  
22.	Exportaciones e Importaciones totales de Austria:  1155000 

"""