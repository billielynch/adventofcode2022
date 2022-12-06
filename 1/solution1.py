INPUT_FILE = "1/input.txt"
with open(INPUT_FILE) as input_file:
    read_data = input_file.read()

per_elf_data_strs = read_data.split("\n\n")
calories_per_elf = [
    sum([int(datum) for datum in elf_data.split("\n")])
    for elf_data in per_elf_data_strs
]

answer1 = max(calories_per_elf)
answer2 = sum(sorted(calories_per_elf)[-3:])

print(answer1)
print(answer2)
