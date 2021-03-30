import math

def average(args):
    return float(sum(args))/max(len(args),1)


def ispeed(func, *args):
    import time
    results = []
    aver = []
    for x in args:
        run_x = []
        for i in range(5):
            start = time.perf_counter_ns()
            a = func(int(x))
            stop = time.perf_counter_ns()
            run_x.append(stop-start)
        results.append(a)
        aver.append(average(run_x))
     
    return (results,aver)

def f(x):
    import cmath
    return cmath.sqrt(x)
def sin(x):
    import math
    return math.sin(x)

# print(ispeed(ispeed,sin,2))
# print(ispeed(sin,0,3.14))