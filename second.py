test_str = "Geeks"
test_int = 4     
print("The original string is : " + test_str)
  
# printing number
print("The original number : " + str(test_int))  
# Inserting number in string 
res = test_str + str(test_int) + test_str
  
# printing result 
print("The string after adding number is  : " + str(res))