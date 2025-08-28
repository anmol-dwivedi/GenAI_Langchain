from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int


new_person: Person = {'name':'Anmol',
                      'age': 29}

print(new_person) # (this code will run even if we put age as str)