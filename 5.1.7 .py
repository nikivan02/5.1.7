with open('numbers.txt') as f:
    number_lines = f.readlines()

with open('numbers.txt', 'w') as f:
    for line in number_lines:
        line = line.split()
        f.write('{}\n'.format(' '.join(map(lambda x: str(round(float(x) ** 2, 2)), line))))
