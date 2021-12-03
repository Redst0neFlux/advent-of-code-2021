with open("input.txt") as f:
    file = f.read()
file = [int(x) for x in file.splitlines()]

#Part one
prev_1 = file[0]
count_1 = 0
for num in file:
    if num > prev_1:
        count_1 += 1
    prev_1 = num
print(count_1)

#Part two
prev_2 = 100000
count_2 = 0
for x in range(len(file)-2):
    sum_var = sum(file[x:x+3])
    if sum_var > prev_2:
        count_2 += 1
    prev_2 = sum_var
print(count_2)
