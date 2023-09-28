input = open("input.txt", "r")

sum = 0
elves = []
for line in input:
    if line != "\n":
        sum += int(line)
    else:
        elves.append(sum)
        sum = 0

maximum = max(elves)
print("Elf", elves.index(maximum), "had", maximum)
elves_sorted = list(reversed(sorted(elves)))
print(
    "Sum of calories (top 3):",
    (elves_sorted[0] + elves_sorted[1] + elves_sorted[2]),
)


input.close()
