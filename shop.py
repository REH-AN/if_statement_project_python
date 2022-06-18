print ("----------WELCOME TO COMPUTER BAZAR----------")
print ("--------house full of tech--------")

print ("----laptop we have----")
print ("DELL ")
print ("TOSIBA ")
print ("MAC")




enteredlaptop=input ("enter name of laptop")

if (enteredlaptop=='dell'):
    print("it costs rs.80,000")
elif (enteredlaptop=='tosiba'):
    print("it costs rs.30,000")
elif (enteredlaptop=='mac'):
    print("it costs rs. 50,000")

if (enteredlaptop=='dell'):
    enteredlaptop=80000
elif (enteredlaptop=='tosiba'):
    enteredlaptop=30000
elif (enteredlaptop=='mac'):
    enteredlaptop=50000



quantity=input ("enter no. of quantity")

print ("delivery options: home,pickup")



delivery_options=input ("enter delivery options")


if (delivery_options=='home'):
    print("IT WILL COST YOU rs.1000 ")
elif (delivery_options=='pickup'):
    print("IT IS FREE")

if (delivery_options=='home'):
    delivery_options=1000
elif (delivery_options=='pickup'):
    delivery_options=0



print ("location where we deliver: kathmandu,lalitpur,bhaktapur")


location=input ("type location you want your product to be delivered")


if (location=='kathmandu'):
    print(" 13% VAT is included ")
elif (location=='lalitpur'):
    print("it is free")
elif (location=='bhaktapur'):
    print("it is free")

if (location == 'kathmandu'):
    location = 13
elif (location == 'tosiba'):
    location =0
elif (location == 'mac'):
    location = 0


print("packing option we have")
print("plastic=rs.500")
print("bag=rs.1000")
print("gift box=rs.5000")




package=input ("enter how you want your laptop to be packed")

if (package=='plastic'):
    print("it will cost you rs500")
elif (package=='bag'):
    print("it will cost you rs1000")
elif (package=='giftbox'):
    print("it will cost you rs5000")

if (package == 'plstic'):
    package = 500
elif (package == 'bag'):
    package = 1000
elif (package == 'giftbox'):
    package= 50000




total=enteredlaptop+delivery_options+package
total=(int(total))
print (total)
total_tax=total+(location/100)*total
print ('total with tax is ',total_tax)
