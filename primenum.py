from math import sqrt

def prime (num) :
    prime = True
    for i in range(2, round(sqrt(num) + 1 )):
        if num % i == 0:
            prime = False
            break
        return prime

def main():
    print ("This program prints all prime numbers less than ")
    print(" or equal to a number")
    num = eval(input ("Enter a number: "))

    print ("These are prime numbers less than or equal to "+ str(
num) + ":")
    for i in range(2, num + 1):
        if prime(i):
            if i == 2:
                print(2, end = "")
        else:
            print(",", i, end = "")
    print()
main()
