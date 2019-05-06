def check_happy_num(n):
    list_to_avoid_loop = []
    sum1 = sum_of_digits(n)

    while(True):
        if sum1 == 1:
            return True
        elif sum1 not in list_to_avoid_loop:
            list_to_avoid_loop.append(sum1)
            sum1 = sum_of_digits(sum1)
        else:
            return False



def sum_of_digits(number):
    sum = 0
    while(number>0):
        digit = number%10
        number = number//10
        sum += digit**2
    return sum

def find_no_of_happy_num(number1):
    i = 2
    while(number1>0):
        if check_happy_num(i):
            print(i,end=' ')
            number1 -= 1
        i += 1


if __name__ == '__main__':
    num = int(input('Enter a number to find whether it is happy or not!\n'))
    find_no_of_happy_num(num)