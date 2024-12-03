import re

def part_1():
    file_path = 'input.txt'
    with open(file_path, "r") as file:
        input = file.read()
    reg = r"mul\((\d+),(\d+)\)"
    values = re.findall(reg, input)
    result = sum([int(a) * int(b) for a, b in values])
    print(result)

def part_2():
    file_path = 'input.txt'
    with open(file_path, "r") as file:
        input = file.read()
    reg = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))"
    values = re.findall(reg, input)
    valid = []

    ignore = False
    for val in values:
        if val == "don't()":
            ignore = True
        elif val == "do()":
            ignore = False
        elif val.startswith('mul') and not ignore:
            nums = re.findall(r"\d+", val)
            prod = int(nums[0]) * int(nums[1])
            valid.append(prod)
    result = sum(valid)
    print(result)

part_1()
part_2()