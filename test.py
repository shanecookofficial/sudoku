import json
with open('saved_games/131.05.Easy.json') as f:
    data = json.load(f)
    board = data['board']
    for i in board:
        print(i)