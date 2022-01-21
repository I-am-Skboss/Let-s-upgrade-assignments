from pickle import LIST, TUPLE
value1 = -45
value2 = 45.0
output = (value1 == value2 )
list = [value1,value2,"class10",21,10] #these are mutable
tuple = {value1,value2,"class10",21,10} #these are immutables
set1 = set([value1,value2,"class10",21,10])
dictionary = {
    value1 : "Random number",
    "Name" : "Shivam"}
print (" This is integer example : %s, this is float example : %s this is a boolean example : %s this is a list example : %s this is a tuple example : %sthis is a set example : %s this is a dictionary example : %s" %(value1,value2,output,list,tuple,set1,dictionary))
print ("This is integer example : "+ str(value1) +", this is float example : "+ str(value2) +" this is a boolean example : "+ str(output))
print (f"This is integer example : {value1}, this is float example : {value2} this is a boolean example : {output} this is a list example : {list} this is a tuple example : {tuple}this is a set example : {set1}")
print ("This is integer example : {1}, this is float example : {0} this is a boolean example : {2}this is a list example : {3} this is a tuple example : {4}this is a set example : {5}".format(value2,value1,output,list,tuple,set1))