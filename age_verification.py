# Age verification assignment

# Introdction so user knows what they are using
print("Hello user.\nI am an age verification program.\nPlease input your age.")
age=int(input())
# Run functions to verify age
if age>18:
    print("You are old enough to drive.")
elif age<18:
    print("You are not old enough to drive.")
else:
    print("You are old enugh to drive.")

if age>18:
    print("You are old enough to vote.")
elif age<18:
    print("You are not old enough to vote.")
else:
    print("You are old enough to vote.")

if age>21:
    print("You are old enough to legally but alcohol.")
elif age<21:
    print("You are not old enough to leally buy alcohol.")
else:
    print("You are old enough to legally but alcohol.")

if age>65:
    print("You are eligible for a senior discount.")
elif age<65:
    print("You are not eligible for a senior discount.")
else:
    print("You are eligible for a senior discount.")