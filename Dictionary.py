'''
#Dictionary
These are mutable data structures that allows to store key:value pairs.
Dictionary can be created using the dict() or curly braces {}.
A dictionary is a collection which is ordered, changeable and do not allow duplicates.
'''
'''
#Creating a dictionary
thedict = {
    "company": "Aurobindo",
    "Industry":"Pharma",
    "Location":"Pashmylaram",
}
print(thedict)
'''
'''
#Dictionary Length
To deterimine how many items a dictionary has, use the len() function.
thedict = {
    "company": "Aurobindo",
    "Industry":"Pharma",
    "Location":"Pashmylaram",
}
print(len(thedict))
'''
'''
#Dictionary-Data types
#The values im dictionary can be of any data type.
thedict = {
    "company": "Aurobindo",
    "Existence":False,
    "Pincode":521001,
    "IndustryType":["Pharma", "Finance", "Technology"]
}
print(thedict)
'''
'''
#Datatype of a dictionary
thedict = {
    "company": "Aurobindo",
    "Existence":False,
    "Pincode":521001,
    "IndustryType":["Pharma", "Finance", "Technology"]
}
print(type(thedict))
'''
'''
#Creating a dictionary using dict() constructor
thedict = dict(name = "Vasu", age = "23", country = "India")
print(thedict)
'''
#Accessing Items of a dictionary
'''
1)Using Sqare brackets
thedict = {
    "company": "Aurobindo",
    "Existence":False,
    "Pincode":521001,
    "IndustryType":["Pharma", "Finance", "Technology"]
}
print(thedict["Pincode"])

2)sing get()
thedict = {
    "company": "Aurobindo",
    "Existence":False,
    "Pincode":521001,
    "IndustryType":["Pharma", "Finance", "Technology"]
}
print(thedict.get("Existence"))
'''
'''
#Get Keys
#This method returns list of all keys in the Dictionary
thedict = {
    "company": "Aurobindo",
    "Existence":False,
    "Pincode":521001,
    "IndustryType":["Pharma", "Finance", "Technology"]
}
print(thedict.keys())
'''
#Get Values
#The Values() method will return list of all the values in the dictionary.
thedict = {
    "company": "Aurobindo",
    "Existence":False,
    "Pincode":521001,
    "IndustryType":["Pharma", "Finance", "Technology"]
}
print(thedict.values())