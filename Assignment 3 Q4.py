count = 0
total = 0

filename = input('Enter the file name: ')
try:
    fhand = open(filename)
except FileNotFoundError:
    print('File cannot be opened: ', filename)
    quit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        colpos = line.find(':')
        number = line[colpos+1:].strip()
        SPAM_C = float(number)
        total = total + SPAM_C

average = total / count
print('Average spam confidence: ', average)
