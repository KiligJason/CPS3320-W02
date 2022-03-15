class person():

    #initiate all personal information
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height

    #input function
    def input_person_data():
        print("Enter name: ")
        person.name=str(input())
        print("Enter age: ")
        person.age=str(input())
        print("Enter weight: ")
        person.weight=str(input())
        print("Enter height: ")
        person.height=str(input())
    
    #print the result
    def get_person_data():
        print("This person's information is: "+person.name+", "+person.age+" years old, "
        +person.weight +" (g), "+person.height+" (cm)")
    

    def main():
        person_info = person.input_person_data()
        person_result = person.get_person_data()

if __name__ == '__main__':
    person.main()