number=int(input("ENTER A NUMBER OF SECONDS"))
hr=number//3600
remaining=number%3600
min=remaining//60
remaining2=remaining%60
print(hr,":",min,":",remaining2)
