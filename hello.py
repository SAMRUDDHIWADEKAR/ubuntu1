def fact(n):
   if n == 0:
       return 1
   else :
       return n*fact(n-1)
       
num = 5
result = fact(num)
print(f"The factorial of (num) is (result).")

    
