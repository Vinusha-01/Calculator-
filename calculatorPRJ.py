def add(num1,num2):
   return num1+num2

def subtract(num1,num2):
   return num1-num2

def multiply(num1,num2):
   return num1*num2

def divide(num1,num2):
   try:
      res= num1/num2
      return res   
   except ZeroDivisionError:
      print("it is not divisible by zero")

while True:
   print("operations")
   print("1. Addtion")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")
   choice = input("enter your choice(1/2/3/4): ")

   if choice in ('1','2','3','4'):
      try:
         num1 = float(input("enter the first number: "))
         num2 = float(input("enter the second number: "))

         if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))

         elif choice == '2':
            print(num1,"-",num2,"=",subtract(num1,num2))

         elif choice == '3':
            print(num1,"*",num2,"=",multiply(num1,num2))

         elif choice == '4':
            print(num1,"/",num2,"=",divide(num1,num2))

      except ValueError:
         print("invalid input,please enter a valid number")

   else:
      print("invalid input")

   again = input("do you want to perform another calculation(yes/no): ").lower()

   if again != 'yes':
      print("thankyou for using calculator")
      break
