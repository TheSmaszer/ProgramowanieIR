def update():
    import requests
    r = requests.get("https://covid.ourworldindata.org/data/jhu/full_data.csv")
    f = open("full_data.csv","w")
    f.write(r.content.decode("utf-8"))
    f.close()

# update()

# print(lista[0].split(sep=","))
# print(lista[50].split(sep=","))

with open("full_data.csv") as lista:
    for line in lista:
        line_sep = line.split(sep=",")
        case_pol = {}
        if line_sep[1] == "Poland":
            case_pol = {case_pol,line_sep[0]:line_sep[2]}

print(case_pol)