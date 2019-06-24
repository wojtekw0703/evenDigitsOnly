#Written by wojtekw0703
def evenDigitsOnly(n):
    while n!=0:
        digit = n%10
        n //=10
        if digit%2>0:
            return False
            break


    return True


print(evenDigitsOnly(248622))
