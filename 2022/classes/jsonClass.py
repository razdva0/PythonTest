import json


class Tournament:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)


tournaments = {
    'Aeroflot Open': 2010,
    'FIDE World Cup': 2018,
    'FIDE Grand Prix': 2016
}

t1 = Tournament('Aeroflot Open', 2010)

json_data = json.dumps(tournaments, indent=2)
print(json_data)
json_d = json.dumps(t1.__dict__)
print(json_d)
t2 = Tournament(**json.loads(json_d))
print(t2.name, t2.year)
loaded = json.loads(json_data)
print(type(loaded))
print(loaded)


class ChessPlayers:

    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data):
        tournaments = list(map(Tournament.from_json, json_data['tournaments']))
        return cls(tournaments)


t1 = Tournament('Aeroflot Open', 2010)
t2 = Tournament('FIDE World Cup', 2018)
t3 = Tournament('FIDE Grand Prix', 2016)
p1 = ChessPlayers([t1, t2, t3])

json_data = json.dumps(p1, default=lambda obj: obj.__dict__)
decoded_player = ChessPlayers(json.loads(json_data))
print(decoded_player)
player_tournament = decoded_player.tournaments
print(type(player_tournament))
print(player_tournament)

with open('player.json', 'w') as file:
    json.dump(p1, file, default=lambda obj: obj.__dict__)

with open('player.json', 'r') as read_file:
    data = json.load(read_file)

print(data)
decoded_player = ChessPlayers.from_json(data)
print(decoded_player)
print(decoded_player.tournaments)

import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)

print(todos)
