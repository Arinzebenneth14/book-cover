
 
# Dictionary
dictionary = {
    "key" : "value"
}

person = { 
"name" :"Tomi" ,
"nationality" :"Togo",
"religion": "Traditionalist",
"gender" : "Male",
"extra_details" : {
    "nin" : 9990566677888,
    "date of birth" : "14 April 1999",
    "bvn": 4456765566778889
}
  }

person["name"] = "Segun"
person["height"] = 1.75

a = {}
print("First:",a)

# added values 
a["key"] = 1
a["age"] = 20

print ("Second",a)

 # deleting a key
del a["age"]

print("Third:",a)

 # clear every value
  # a.clear()

print("Fourth:",a)
 
  # Delete the dictionary

  # del a

 # print("fifth: "a )


output = a.get("key",)



 # List
collection = ["Abel","Kane",12,114.3,True,[1,"tame",14,["Tomi,42"]]]

 # print (collection[-1][-1][0])
 # print(collection[5][[3]{0})
       
collection.insert(0,"Arsenal")  # add a value to a specific index
collection.pop(4)  # takes out a value with a specific index
collection.remove(True)  # takes out a value by taking out the value
collection[0] = "Liverpool"  # update a value

 # print(collection)

 # Membership
  # in boolean

checks = "Arsenal" in collection

 # contenation
concat_list = [1,2,3,4,5],[6,7,8,9,0]
print(concat_list)

 # Repition
item = ["Hi"]
repeat_list = item * 4
 # print(repeat_list)

  # lenght - uses len to checklenght og list
print(len(concat_list))

 #slicing
numbers = [0,1,2,3,4,5,6,7,8.9,10,11,12,13,14,15]
numbers.append(16)
numbers.insert(17,3)
slice_items_in_List = numbers[-4:]
print(slice_items_in_List)

print(numbers)