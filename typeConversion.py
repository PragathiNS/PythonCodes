#I have an integer variable and I want to use it in print statement which prints the whole statement which is a string

price = 10
#print("I bought this package for $" + price) #this will give you an error 

# So we convert the type of price variable from int to string using str()
print("I bought this package for $" + str(price))
