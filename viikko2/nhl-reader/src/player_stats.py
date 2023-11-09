class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        players_by_nationality = filter(
            lambda player: player.nationality == nationality, players )
       
        return sorted(players_by_nationality,
                      key=lambda player: player.goals + player.assists,
                      reverse=True)
