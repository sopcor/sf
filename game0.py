import numpy as np
number=np.random.randint(1,101)
count=0
while True:
    count+=1
    predicate_number=int(input("Введите искомое число: "))
    if predicate_number<number:
        print("Введенное число меньше искомого")
    elif predicate_number>number:
        print("Введенное число больше искомого")
    else: 
        print(f"Введенное число угадано и равно {number}, число пыток {count}")
        
        break


    
    

