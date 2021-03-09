import time

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = 0

a1_time = time.perf_counter_ns()
c = a + b
a2_time = time.perf_counter_ns()
print ("Czas dodawania w ns:",a2_time - a1_time)

m1_time = time.perf_counter_ns()
c = a * b
m2_time = time.perf_counter_ns()
print("Czas mnożenia w ns:",m2_time - m1_time)
print("Różnica tych czasów:",m2_time - m1_time - (a2_time - a1_time))