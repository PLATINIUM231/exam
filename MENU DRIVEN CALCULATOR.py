
print("Hi, This is the Basic console based calculator!\n")
while True: 
  print("Please select which of the following arithmetic  operation you want me to perform-\n\n" \
  "1. Add\n" \
  "2. Subtract\n" \
  "3. Multiply\n" \
  "4. Divide\n" \
  "5. Exit\n")

  operation = float(input(" Enter your choice of operation you want to perform: 1, 2, 3, 4 or 5 :\n"))
  if operation == 1:
    num_1 = float(input('Please, Enter the first number: \n'))
    num_2 = float(input('Please, Enter the second number: \n'))
    print('\nAddition of {} + {} = '.format(num_1, num_2), add(num_1, num_2),"\n")
  elif operation == 2:
    num_1 = float(input('Please, Enter the first number: \n'))
    num_2 = float(input('Please, Enter the second number: \n'))
    print('\nSubtraction of {} - {} = '.format(num_1, num_2), subtract(num_1, num_2),"\n")
  elif operation == 3:
    num_1 = float(input('Please, Enter the first number: \n'))
    num_2 = float(input('Please, Enter the second number: \n'))
    print('\nMultiplication of {} * {} = '.format(num_1, num_2), multiply(num_1, num_2),"\n")
  elif operation == 4:
    num_1 = float(input('Please, Enter the first number: \n'))
    num_2 =float(input('Please, Enter the second number: \n'))
    print('\nDivision of {} / {} = '.format(num_1, num_2), divide(num_1, num_2),"\n")
  elif operation == 5:
    print("Thank you for using this calculator...")
    break
  else:
    print("\nPlease enter Valid input\n")
    
print('Addition of {} + {} = '.format(num_1, num_2))
print(num_1 + num_2)
print(' Subtraction of {} - {} = '.format(num_1, num_2))
print(num_1 - num_2)

print('Multiplication of {} * {} = '.format(num_1, num_2))
print(num_1 * num_2)

print('Division of {} / {} = '.format(num_1, num_2))
print(num_1 / num_2)
def add(num_1, num_2):
   return num_1 + num_2

def subtract(num_1, num_2):
   return num_1 - num_2

def multiply(num_1, num_2):
   return num_1 * num_2

def divide(num_1, num_2):
   return num_1 / num_2