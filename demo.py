file = open('Alphabet.file', 'r')
print(file.read(6))
file.close()

file = open('Alphabet.file', 'r')
print(file.readline())
print(file.readline())
file.close()

file = open('Alphabet.file', 'r')
print(file.readlines())
file.close()

file = open('Alphabet.file', 'r')
for x in file:
    print(x)
file.close()

file = open('Alphabet.file', 'r')
file2 = open('Updated_Alphabet.file', 'w')

for line in file.readlines():
    if not (line.startswith('-')):
        print(line)
        file2.write(line)

file.close()
file2.close()

file = open('Alphabet.file', 'r')
file2 = open('Copy.file', 'w')

cont = file.readlines()
type(cont)
for i in range (1, len(cont)+1):
    if (i%2 != 0):
        file2.write(cont [i-1])
    else:
        pass
    
file.close()
file2.close()