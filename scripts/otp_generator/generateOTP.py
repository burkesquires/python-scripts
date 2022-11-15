import random
def otp(num):
    result=""
    if len(str(num)) != 10:
        return "Enter a valid mobile number!"
    for _ in range(6):
        digit=str(random.randint(0,9))
        result=result+digit
    return result
        
print(otp(9874453920))