import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    #print("Oliot:")
    print("Players from FIN:")

    for player in sorted(players, key=lambda player: player.goals + player.assists, reverse=True):
        if player.nationality == "FIN":
            print(player)

if __name__ == "__main__":
    main()
