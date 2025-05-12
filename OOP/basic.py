class Student:                                    #Declaring an class
    name="Vashisht Kumar"
    age="2-12-2004"

    #def __init__(self):                            #default constructor
    #    self.college="Chitkara University" 

    def __init__(self,rent):                       # The self parameter indicates that it inclues to this particular object
        self.rent=rent
        self.college="Chitkara University"
    
    def hello(self):                               # Normal functions
        print("Hi Hello is printing all these things "+ s1.name +" My college is "+s1.college+" And currently I am in "+s1.rent)

s1=Student("Hyderabad")                                      #Declaring objects
print(s1.name +" My college is "+s1.college+" And currently I am in "+s1.rent)      # Accessing the objects
s1.hello()