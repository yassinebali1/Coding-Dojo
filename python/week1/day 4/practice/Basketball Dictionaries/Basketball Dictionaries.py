class Player:
    def __init__(self, player_info):
        self.name = player_info.get("name")  
        self.age = player_info.get("age")    
        self.position = player_info.get("position")  
        self.team = player_info.get("team")  
players = [
    {
        "name": "Kevin Durant", 
        "age": 34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age": 24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age": 32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age": 33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age": 32,
        "position": "Power Forward", 
        "team": "Philadelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]
player_objects = [Player(player) for player in players]
for player in player_objects:
    print(f"{player.name}, Age: {player.age}, Position: {player.position}, Team: {player.team}")


# Challenge 2

class Player:
    def __init__(self, player_info):
        self.name = player_info.get("name")
        self.age = player_info.get("age")
        self.position = player_info.get("position")
        self.team = player_info.get("team")

# Player dictionaries
kevin_durant = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}

jason_tatum = {
    "name": "Jason Tatum", 
    "age": 24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}

kyrie_irving = {
    "name": "Kyrie Irving", 
    "age": 32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

damian_lillard = {
    "name": "Damian Lillard", 
    "age": 33,
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
}

joel_embiid = {
    "name": "Joel Embiid", 
    "age": 32,
    "position": "Power Forward", 
    "team": "Philadelphia 76ers"
}

demar_derozan = {
    "name": "DeMar DeRozan",
    "age": 32,
    "position": "Shooting Guard",
    "team": "Chicago Bulls"
}
kd = Player(kevin_durant)
jt = Player(jason_tatum)
ki = Player(kyrie_irving)
dl = Player(damian_lillard)
je = Player(joel_embiid)
dd = Player(demar_derozan)

players = [kd, jt, ki, dl, je, dd]
for player in players:
    print(f"{player.name}, Age: {player.age}, Position: {player.position}, Team: {player.team}")


# chalange 3
class Player:
    def __init__(self, player_info):
        self.name = player_info.get("name")
        self.age = player_info.get("age")
        self.position = player_info.get("position")
        self.team = player_info.get("team")

# List of player dictionaries
players = [
    {
        "name": "Kevin Durant", 
        "age": 34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age": 24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age": 32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age": 33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age": 32,
        "position": "Power Forward", 
        "team": "Philadelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]
player_instances = []
for player_info in players:
    player_instances.append(Player(player_info))
for player in player_instances:
    print(f"{player.name}, Age: {player.age}, Position: {player.position}, Team: {player.team}")
