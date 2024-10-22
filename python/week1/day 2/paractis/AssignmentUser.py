class user:
    def __init__(self, first_name, last_name, email,age,  is_reward_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name 
        self.email = email
        self.age = age
        self.is_reward_menber = is_reward_member
        self.gold_card_points = gold_card_points 

    def display_info(self):
        print(f"first name:{self.first_name}")
        print(f"last name:{self.last_name}")
        print(f"email:{self.email}")
        print(f"age : {self.age}")
        print(f"rewards member : {self.is_reward_member}")
        print(f"gold card points : {self.gold_card_points}")
    
    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"{self.first_name} has been enrolled as a rewards member.")
        else:
            print(f"{self.first_name} is already a rewards member.")

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f"{self.first_name} does not have enough points to spend {amount}.")
        else:
            self.gold_card_points -= amount
            print(f"{self.first_name} spent {amount} points. Remaining points: {self.gold_card_points}.")

user1 = user("yassine", "bali", "yassine.bali@example.com", 30)
user2 = user("Jane", "Smith", "jane.smith@example.com", 28)
user3 = user("Alice", "Johnson", "alice.johnson@example.com", 25)    







