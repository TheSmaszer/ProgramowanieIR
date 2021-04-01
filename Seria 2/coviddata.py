import matplotlib.pyplot as plt
import numpy as np

def update():
    import requests
    r = requests.get("https://covid.ourworldindata.org/data/jhu/full_data.csv")
    f = open("full_data.csv","w")
    f.write(r.content.decode("utf-8"))
    f.close()

update()
avail_count = {}
with open("full_data.csv") as lista:
    next(lista)
    for line in lista:
        line_sep = line.split(sep=",")
        avail_count[line_sep[1]] = ""

countries = ""
for i in avail_count.keys():
    countries += i + ", "

cases = {}

while(True):
    print("Available countires: ",countries[:-2])
    country = input("Enter country: ")
    if(not cases.get(country)):
        case_count = {}
        with open("full_data.csv") as lista:
            for line in lista:
                line_sep = line.split(sep=",")
                if line_sep[1] == country:
                    case_count[line_sep[0]] = line_sep[2]

        if(case_count):
            cases[country] = case_count
        else:
            print("404 - Country not found")
            continue
    plt.figure(figsize=(12, 8))
    plt.bar(cases[country].keys(),[float(value) for value in cases[country].values()],label=f"New cases in {country}")
    plt.grid()
    plt.legend()
    plt.xticks(range(1,len(cases[country].keys()),40))
    plt.show()