# Initialize list
Lst = [50, 70, 30, 20, 90, 10, 50]

# Display list
for i in range(1, len(Lst)):    
    pop = -i-1
    print(Lst[-i], end=' ')
    print(Lst[pop])