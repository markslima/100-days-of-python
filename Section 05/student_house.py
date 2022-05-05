class Student:
    
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} of House {self.house} is a student at Oxford"

    #create student without calling student method first
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    # Setter
    @property
    def name(self):
        return self._name

    # Getter
    @name.setter
    def name(self, name):
        if not name: 
            raise ValueError("You didn't enter a name.")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main() 

