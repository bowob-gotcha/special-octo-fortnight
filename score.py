#You can either try this one

score = input("Enter Score: ")
x = float(score)

try:
    if x > 1.0 or x < 0 :
        print("Out of Range")
    elif x >= 0.9 :
        print("A")
    elif x >= 0.8 :
        print("B")
    elif x >= 0.7 :
        print("C")
    elif x >= 0.6 :
        print("D")
    elif x < 0.6 :
        print("F")
except ValueError:
    print("Not a number")
    
#Or this one

score = input("Enter Score: ")

try:
    x = float(score)
except:
    x = -1
    
if x > 1.0 :
    print("Out of Range")
elif x >= 0.9 :
    print("A")
elif x >= 0.8 :
    print("B")
elif x >= 0.7 :
    print("C")
elif x >= 0.6 :
    print("D")
elif 0 < x < 0.6 :
    print("F")
else:
    print("NOT A NUMBER")
