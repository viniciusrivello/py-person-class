class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list: list[Person] = []

    # Criar todas as pessoas primeiro
    for data in people:
        person = Person(data["name"], data["age"])
        person_list.append(person)

    # Criar os relacionamentos wife / husband
    for data in people:
        person = Person.people[data["name"]]

        if "wife" in data and data["wife"] is not None:
            person.wife = Person.people[data["wife"]]

        if "husband" in data and data["husband"] is not None:
            person.husband = Person.people[data["husband"]]

    return person_list
