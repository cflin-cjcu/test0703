def avg(n):
    a = [int(input()) for i in range(n)]
    average = sum(a) / len(a)
    return average

num = int(input())
print(avg(num))