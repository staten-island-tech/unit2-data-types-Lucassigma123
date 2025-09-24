# sentence = input("Write a sentence") #asks person to write a sentence
# words = sentence.split() # split breaks the sentence into separate words
# print(len(words)) #len counts the words or letters 


# x = (int(input("write a number"))) #int makes it a integer
# even = (x % 2)== 0
# if even:
#     print("even")
# else: print("odd")

# x= input("The bill will be 100$ how was the service")
# if x =="bad":
#      print ("0 tip")
# if x=="okay":
#      print("15% tip")
# if x=="good":
#      print("20% tip")
# if x=="great" :
#      print("25% tip")

# x= (int(input("write a number"))) 
# for i in range(1,x+1): # i is representing the numbers inside the parenthesis
#     if x%i==0: #checks if the number is a factor of x
#         print(i) # if it is it prints the number

x= (int(input("write a number"))) 
y= (int(input("write a number")))
for i in range(min(x, y), 0, -1): #min is find the smallest number x or y and its goes down by 1 and stops at 0
    if x%i ==0 and y%i==0: #checks if x divide by y has no remainder
        print(i)
        break #stops loop
 
