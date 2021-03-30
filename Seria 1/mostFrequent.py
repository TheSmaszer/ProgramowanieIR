def mostFrequent(list):
    n = 0
    for el in list:
        if list.count(el)>n:
            mostfreq = el
            n = list.count(el)
    return mostfreq
a = input("Podaj dowolne elementy listy oddzielone przecinkami: ")
print(mostFrequent(a.split(",")))
