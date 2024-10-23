class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self 

    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"{self.first_name} has been enrolled as a rewards member.")
        else:
            print(f"{self.first_name} is already a rewards member.")
        return self  
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f"{self.first_name} does not have enough points to spend {amount}.")
        else:
            self.gold_card_points -= amount
            print(f"{self.first_name} spent {amount} points. Remaining points: {self.gold_card_points}.")
        return self  
user1 = User("John", "Doe", "john.doe@example.com", 30)
user2 = User("Jane", "Smith", "jane.smith@example.com", 28)
user1.display_info().enroll().spend_points(50).display_info()
print()
user2.enroll().spend_points(80).display_info()

