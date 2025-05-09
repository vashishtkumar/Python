# Dictionaries are used to store data in key value pairs
# They are unordered , mutlable(changes are allowed) and duplicate keys are not allowed


info={
    "name":"Vashish Kumar",
    "age":20,
    "Degree":[10,12,"BE CSE"],
    "BE subjects":{
        "JAVA":(98,89,70),
        "DSA":(89,97)
    },

}

print(info)
print(info["name"])
print(info["Degree"][2])
print(info["BE subjects"]["JAVA"][1])

info["Home"]="Patna, Bihar"
info[801503]="Pin code"

print(info)

more={
    "PS":"Shahpur",
    "Near By School":"D.P.S",
    ("Company","Location"):["Beehyv", "Hyderabad"]
}

print(more[("Company","Location")])
print(more[("Company","Location")][1])



# Dictionary Methods
print(info.keys())  # returns all the keys of that particular dict
print(info.values()) # returns all the values of that particular dict
print(info.items()) # returns all the (keys, value ) pair as tuple
print(info.get("nam")) # if that particular keys is not available then it will not throw error and say None
print(info.update(more))

print(info)
