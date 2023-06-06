#Zeckondorf numbers
#make fibonacci sequence in a list by adding i and i + 1

fibonacci = [1,1]
num = int(input('Input a number:'))


#list of fibonaccis
for i in range(num):
  fibonacci.append(fibonacci[i]+fibonacci[i+1])
print('List of fibonacci sequence/',fibonacci)


fib = fibonacci[1:] #remove 1 cus 1 is the same
print('Unique fib sequence', fib)



#def fibsmaller(num,fibonacci):
#   return min(fibonacci,key=lambda x:abs(x-num))

#print(fibsmaller(num,fibonacci))

#bigfib = fibsmaller(num,fibonacci) > num
#print("bigfib", bigfib)
#f1, f2, f3 = 0, 1, 1
#while (f3 <= n):
#   f1 = f2;
#   f2 = f3;
#   f3 = f1 + f2;
# return f2;


    
def fibsmaller(num, numbers):
    for chosenfib in reversed(numbers):
        if chosenfib <= num:
            return chosenfib
    
def zeckondorf(num):
    distincts = []
    while num > 0:
        calculation = fibsmaller(num,fib)
        num -= calculation
        distincts.append(calculation)
    print(distincts)

    
print('Distinct Values:')
zeckondorf(num)