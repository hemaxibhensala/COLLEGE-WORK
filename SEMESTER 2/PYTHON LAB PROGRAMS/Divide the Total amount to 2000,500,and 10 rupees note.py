TotalAmount=int(input("ENTER A NUMBER OF AMOUNT:"))
note2000=TotalAmount//2000
rem=TotalAmount%2000
note500=rem//500
rem2=rem%500
print (note2000,"2000 Rs:",note500,"500 Rs:",rem2,"100 Rs:")
