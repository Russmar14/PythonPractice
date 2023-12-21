
def fizzBuzz(upTo):
    for i in range(1,upTo + 1):
        if i % 3 == 0 and i%5 == 0:
            print("FizzBuzz",end = " ")
        elif i%3 == 0:
            print("Fizz", end = " ")
        elif i%5 ==0:
            print("Buzz", end = " ")
        else:
            print(i, end = " ")

user_input = int(input('Enter a number to check if each number leading up to it is divisible by 3, 5, both, or neither!'))

fizzBuzz(user_input)