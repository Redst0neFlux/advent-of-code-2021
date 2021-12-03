with open("input.txt") as f:
    file = f.read().splitlines()

#part one
depth = 0
horizontal = 0
for command in file:
    if command.startswith("forward"):
        horizontal += int(command[-1])
    elif command.startswith("up"):
        depth -= int(command[-1])
    elif command.startswith("down"):
        depth += int(command[-1])
print(depth * horizontal)

#part two
horizontal_2 = 0
aim = 0
depth_2 = 0
for command in file:
    if command.startswith("forward"):
        horizontal_2 += int(command[-1])
        depth_2 += aim * int(command[-1])
    elif command.startswith("up"):
        aim -= int(command[-1])
    elif command.startswith("down"):
        aim += int(command[-1])
print(depth_2 * horizontal_2)