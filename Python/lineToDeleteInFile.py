filename = "C:/Estudos/Python/arquivo1.txt"
line_to_delete = 2
initial_line = 1
file_lines = {}

with open(filename) as f:
    content = f.readlines() 

for line in content:
    file_lines[initial_line] = line.strip()
    initial_line += 1

f = open(filename, "w")
for line_number, line_content in file_lines.items():
    if line_number != line_to_delete:
        f.write('{}\n'.format(line_content))

f.close()
print('Deleted line: {}'.format(line_to_delete))

arquivo = open("C:/Estudos/Python/arquivo1.txt")
#texto = arquivo.read()
print(arquivo.read())