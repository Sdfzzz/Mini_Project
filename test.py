from typing import List # Import the List type
class Person():
    def __init__(self, name):
        self.name = name
def greet_person(person: Person):
    print(f"Hello {person.name}")
person1 = Person("Jane")
person2 = Person("Sam")
people = [person1, person2]
def greet_people(people: List[Person]):
    for person in people:
        greet_person(person)
greet_people(people)