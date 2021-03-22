import pandas as ps
import os
def getDict (filename, mainpath):
    dataFrame3 = open(os.path.join(mainpath, filename),"r") 
    cols = dataFrame3.readline().strip().split(",")
    #print (cols)
    counter = 0
    main_dict = {}
    for col in cols :
        main_dict[col] = []
    counter = 0
    for line in dataFrame3:
        values = line.strip().split(",")
        for i in range(len (values)):
            main_dict[cols[i]].append(values[i])
        counter += 1
    #print ("El dataset tiene %d filas y %d columnas" %(counter, len(cols)))
    return main_dict

def showSum (covid_dict):
    resultados = covid_dict['"RESULTADO"']
    positivos = 0
    negativos = 0
    pendientes = 0
    for resultado in resultados:
        if resultado == "1":
            positivos +=1
        elif resultado == "2":
            negativos += 1
        elif resultado == "3":
            pendientes += 1

    print ("Casos Positivos:" + str(positivos))
    print ("Casos Negativos:" + str(negativos))
    print ("Casos Pendientes:" + str(pendientes))

def getCasesByDay (covid_dict):
    dates = []
    fechasTotales = covid_dict['"FECHA_SINTOMAS"']
    totalCases = len(fechasTotales)
    for fecha in fechasTotales:
        fecha = fecha.strip("\"")
        if (fecha not in dates):
            dates.append(fecha)
    
    dates.sort()
    casesDict = {}
    for date in dates:
        casesDict[date]=[0,0,0,0]  #Positivos, negativos, pendientes, muertos (por fecha de muerte)
    #print(casesDict)
    id = covid_dict['"ID_REGISTRO"']
    #Result Date
    rs = covid_dict['"RESULTADO"']
    # Deth Date
    dDate = covid_dict['"FECHA_DEF"']  
    #Syntoms Date
    sDate = covid_dict['"FECHA_SINTOMAS"']

    for i in range(totalCases):
        if (rs[i] == "1"):
            casesDict[sDate[i].strip("\"")][0] += 1
            if (sDate[i].strip("\"") == "2020-01-13"):
                print ("Id dia " + str(i+1) + " : " + id[i])
        if (rs[i] == "2"):
            casesDict[sDate[i].strip("\"")][1] += 1
        if (rs[i] == "3"):
            casesDict[sDate[i].strip("\"")][2] += 1
        if (dDate[i] != "\"9999-99-99\"" and rs[i] == "1"):
            casesDict[dDate[i].strip("\"")][3] += 1


    print ("Total de casos reportados: " + str(totalCases))
    return casesDict

def printCasesByDay (casesDict):
    dates = casesDict.keys()
    print ("Fecha de ocurrencia \tCasos Positivos \tCasos Negativos \tCasos Pendientes \tMuertes\n")
    i = 0
    for date in dates:
        print ("%20s\t%16d\t%16d\t%17d\t%7d\n" % (date,casesDict[date][0],casesDict[date][1],casesDict[date][2],casesDict[date][3]))
        

    


    

filename = "200615COVID19MEXICO.csv"
mainpath = "E:/Curso de Python/COVID-19"
covid_dict = getDict(filename,mainpath)
#showSum(covid_dict)
casesDict = getCasesByDay(covid_dict)
printCasesByDay(casesDict)






