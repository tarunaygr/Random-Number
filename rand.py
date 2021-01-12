import time
x=input("Enter max number:")
x=int(x)+1
num = int(round(time.time() * 1000%int(x)))
print (num)