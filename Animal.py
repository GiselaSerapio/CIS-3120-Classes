class Animal:
    def __init__(self, name): 
        self.__name = name
        print("hello, I am",self.__name)

    def talk(self):
        print("hi")
    def eat(self):
        print(f"{self.__name} is eating.")

    def sleep(self):
        print(f"{self.__name} is sleeping.")

    def move(self):
        print(f"{self.__name} is moving.")

    def describe(self):
        print(f"{self.__name} is a wonderful animal.")

    def introduce(self):
        print(f"Hello, my name is {self.__name} and I am an animal.")
    

    
