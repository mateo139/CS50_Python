expresion = input ("Please input arithmetic expresion, formated as #number# space $sign$ space #number#")

x, y, z = expresion.split(" ")

#print (x, y, z)

x = int(x)
z = int(z)

if y == "+":
    result = float(x + z)

elif y == "-":
    result = float (x - z)

elif y == "*":
    result = float (x * z)

elif y == "/" and z != 0:
    result = x / z
    result = round(result, 1)

elif z == 0:
    print ("Don't divide by ZERO")

else:
    pass

if z == 0:
    pass
else:
    #print (x, y, z, "=", result)
    print (result)