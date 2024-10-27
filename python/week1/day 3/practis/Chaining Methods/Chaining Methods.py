class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.points = 0 

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Points: {self.points}")
        return self  

    def enroll(self):
        print(f"{self.name} has been enrolled.")
        return self  

    def spend_points(self, amount):
        if amount <= self.points:
            self.points -= amount
            print(f"{self.name} spent {amount} points.")
        else:
            print(f"{self.name} does not have enough points to spend.")
        return self  


user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com")
user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
