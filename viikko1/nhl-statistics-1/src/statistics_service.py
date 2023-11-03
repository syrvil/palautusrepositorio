#from player_reader import PlayerReader
from sort_by import SortBy

def sort_by_points(player):
    return player.points

def sort_by_key(player, sort_by):
    if sort_by == SortBy.GOALS:
        return player.goals
    elif sort_by == SortBy.ASSISTS:
        return player.assists
    # else SortBy.POINTS: 
    else:
        return player.points 

class StatisticsService:
    def __init__(self, reader):
        #reader = PlayerReader()
        self._reader = reader

        #self._players = reader.get_players()
        self._players = self._reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    #def top(self, how_many):
    #    sorted_players = sorted(
    #        self._players,
    #        reverse=True,
    #        key=sort_by_points
    #    )

    #    result = []
    #    i = 0
    #    #while i <= how_many: # bug
    #    while i < how_many:
    #        result.append(sorted_players[i])
    #        i += 1

    #    return result
    
    def top(self, how_many, sort_by=None):
        if sort_by is None:
            sorted_players = sorted(
                self._players,
                reverse = True,
                key = sort_by_points)           
        else:
            sorted_players = sorted(
                self._players,
                reverse = True,
                key = lambda player: sort_by_key(player, sort_by))

        result = sorted_players[:how_many]
        return result