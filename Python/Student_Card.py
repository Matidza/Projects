class Student:
    def __init__(self, name, surname, code, degree, skills, campus):
        self.name = name
        self.surname = surname
        self.code = code
        self.degree = degree
        self.skills = skills
        self.campus = campus

    def __str__(self):
        return f"\nNames: {self.name} {self.surname} \nStudent No: {self.degree} \nDegree: {self.code}\nSkills: {self.skills} \nCampus: {self.campus}"
    #name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            raise  TypeError("Names/Surnames must be in letters")
        else:
            self.__name = name
    
    #Surname
    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self,surname):
        if not isinstance(surname, str): raise TypeError("Names/Surnames must be in letters") 
        else:
            self.__surname = surname

    #Code
    @property
    def code(self):
        return self.__code
    
    @code.setter
    def code(self,code):
        if not isinstance(code, int): raise ValueError("Code must be integers.")
        else:
            self.__code = code
            
    #Degree
    @property
    def degree(self):
        return self.__degree
    
    @degree.setter
    def degree(self,degree):
        if not isinstance(degree, str): raise TypeError("Degree must be in letters!")  
        else:
            self.__degree = degree
    #Skills
    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def skills(self, skills):
        self.__skills = skills

    @property
    def campus(self):
        return self.__campus
    
    @campus.setter
    def campus(self, campus):
        if not isinstance(campus, str): raise TypeError("Campus must be in letters!")
        else:
            self.__campus = campus

        
def main():
    student_card = get_card()
    print(student_card)

def get_card():
    name = input("What is your name: ")
    surname = input("What is your surname: ")
    degree = input("What degree are you enrolled in: ")
    code = int(input("Student number: "))
    skills = input("Skills(Space-Seperated): ").title().split()
    campus = input("Campus: ").title()
    return Student(name, surname, degree, code, skills, campus)

if __name__ == "__main__":
    main()        
