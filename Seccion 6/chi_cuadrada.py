def getchi_Cuadrada (data_dict):
    chi_cuadrada = 0
    for i in range (len(data_dict["Observados"])):
        chi_cuadrada += (data_dict["Observados"][i] - data_dict["Esperados"][i])**2 / data_dict["Esperados"][i]
    return chi_cuadrada
independencia = {}
independencia["Observados"] = [68,28,52,37,80,35]
independencia["Esperados"] = [64,32,59.333,29.667,76.667,38.333]

print (getchi_Cuadrada(independencia))