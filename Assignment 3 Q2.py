count = 0
total = 0
largest = None
smallest = None

while True:
    input1 = input('Enter a number: ')
    if input1 == 'done' : break
    try:
        number = float(input1)
    except:
        print('Invalid input')
    if largest is None or number > largest:
        largest = number
    if smallest is None or number < smallest:
        smallest = number

    count = count + 1
    total = total + number

print(total,count,largest,smallest)
