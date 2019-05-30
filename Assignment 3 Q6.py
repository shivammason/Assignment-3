fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count += 1
print('%d lines in file with From as the first word' % count)