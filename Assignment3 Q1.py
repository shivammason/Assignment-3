
count = 0
total = 0
largest = None
smallest = None

while True:
    input_number = input('Enter number: ')
    if input_number == 'done' : break
    try:
        number = float(input_number)
    except:
        print('Invalid input')

    count = count + 1
    total = total + number

average = total / count

print(total,count,average)