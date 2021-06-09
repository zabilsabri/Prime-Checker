answer = []

for i in range(1, number=int(input("PUT YOUR NUMBER IN: "))):
    if number % i == 0:
        answer.append(i)
        
if len(answer) == 1 or len(answer) == 2:
    print("PRIME")
    
else:
    print("NOT PRIME")
