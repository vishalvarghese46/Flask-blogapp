from random import choice

class Person:
    def __init__(self, name):
        self.name = name

    def print(self):
        return self.make_greeting()

    def make_greeting(self):
        return "Hello {}".format(self.name)


def main():
    people = [
        Person("Ben"),
        Person("Vishal"),
        Person("Bibin")
    ]
    ob1 = choice(people)
    print(ob1.print())


if __name__ == "__main__":
    main()
