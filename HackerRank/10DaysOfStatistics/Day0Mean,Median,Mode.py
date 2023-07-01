import statistics

n = int(input())
x = []
for a in range(n):
    a = int(input())
    x.append(a)

mean = statistics.mean(x)
median = statistics.median(x)
mode = statistics.mode(x)
