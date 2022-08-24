start = 22
over = 47
  
for number in range(start, over+1): 
  if number>1: 
    for id in range(2,number): 
        if(number % id==0): 
            break
    else: 
        print(number)