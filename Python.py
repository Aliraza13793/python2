hello:str = "Ali";
print(hello)
# father_name:str = "Muhammad Akram" // always start with smalll letters 
name : str = 'Ali Raza Akram'
fatherName: str = 'Akram'
education: str ='Master in AI'
age : int = 29

card : str = f"""PIAIC student Card
Student Name: {name}
Father Name: {fatherName}
Student Age: {age}
Student Education: {education}
Total {1 + 2 + 3 + 4}
"""
print(card) 
# with f do any thing or add palce holder means k veriable add kr sakty hain easy sy SB SY ADVANCE TARIQA HAI YE

namee : str = "Ali rAza AkRaM"
print(namee.capitalize())
print(namee.lower())

a = 7
b = 8
# {} place holder

"Pakistan value a = {} and value b = {}".format(a,b)


card : str = """PIAIC student Card
Student Name: {1}
Father Name: {0}
Student Age: {3}
Student Education: {2}

""".format(fatherName, name ,education, age)
#               0       1       2        3
print(card) 

a :list[str] = [i for i in dir(str) if "..." not in i]
print(a)
print(len(a))
