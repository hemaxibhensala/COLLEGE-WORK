num1=int(input("ENTER A STARTING NUMBER FOR A RANGE"))
num2=int(input("ENTER A ENDING NUMBER FOR A RANGE"))
while(num1<=num2):
   flag=0
   i=2
   while(i<num1):
      if(num1%2==0):
        break;
      i=i+1
   else:
      print(num1,end=',')
   num1=num1+1