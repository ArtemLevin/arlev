# with open("data.txt") as file:
#     lines = file.readlines()
#     print(filter(max(sorted(lines), key=lambda x: len(x)), lines)

with open("lines.txt") as file:
    lines = file.readlines()
    max_len = len(list(max(sorted(lines), key=lambda x: len(x))))
    for line in lines:
        if len(list(line)) == max_len:
            print(line.strip())