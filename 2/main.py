with open("input.txt") as f:
    file = f.read().splitlines()
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
