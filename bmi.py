mass = float(input("Podaj swoją masę w kg: "))
height = float(input("Podaj swój wzrost w m: "))

bmi = mass/height**2
bmi = round(bmi,1)

print("Twoje BMI to: ",bmi)
if(bmi<=18.5):
    a = "niedowagę"
elif(18.5<bmi<=25):
    a = "wagę prawidłową"
elif(25<bmi<=30):
    a = "nadwagę"
elif(bmi>30):
    a = "otyłość"
print("To oznacza, że masz:",a)
