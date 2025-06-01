#a program that asks for two numbers using input 
#and divides them. ue an infinite loop to keep asking until a valid input is provided


while True:
     price = int(input('Enter price: '))
     quantity = int(input('Enter quantity: '))
     try:
       tax = float(price/quantity)
     except ZeroDivisionError:
         print('cannot divide by a zero, please enter quantity that is above zero!')
     else:
         print(str(tax))
         print('Tax successfully calculated')
         break
