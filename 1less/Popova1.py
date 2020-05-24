import datetime

print("Hi, dear friend")
print("What's your name? ")
name=input("Name user: ")
name=name.strip()    
print("Nice to meet you. How old is " + name.title()+ "?")
Age1=input("Age user: ")
Age1=int(Age1)
print("It's perfect! Now you have to input year")
Year2=input("Year: ")
Year2=int(Year2)
Year1=datetime.datetime.now().year
Age2=Year2-Year1+Age1
Age2=int(Age2)
print("Well done. You will be " + str(Age2) + " years old in " + str(Year2)) 


