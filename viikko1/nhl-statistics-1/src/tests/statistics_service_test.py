import unittest
from statistics_service import StatisticsService, sort_by_points, sort_by_key
from player import Player
from sort_by import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    # ...
    def test_search_returns_player_if_found(self):
        player = self.stats.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")

    def test_search_returns_none_if_player_not_found(self):
        player = self.stats.search("Luukkainen")
        self.assertIsNone(player)

    def test_team_returns_players_of_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

    def test_top_returns_top_scorers(self):
        top_scorers = self.stats.top(3)
        self.assertEqual(len(top_scorers), 3)
        self.assertEqual(top_scorers[0].name, "Gretzky")
        self.assertEqual(top_scorers[1].name, "Lemieux")
        self.assertEqual(top_scorers[2].name, "Yzerman")

    def test_top_sorts_by_points_without_parameter(self):
        top_scorers = self.stats.top(3)
        self.assertEqual(top_scorers[0].name, "Gretzky")
        self.assertEqual(top_scorers[1].name, "Lemieux")
        self.assertEqual(top_scorers[2].name, "Yzerman")

    def test_top_sorts_by_goals_with_points_parameter(self):
        top_scorers = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(top_scorers[0].name, "Gretzky")
        self.assertEqual(top_scorers[1].name, "Lemieux")
        self.assertEqual(top_scorers[2].name, "Yzerman")
    
    def test_top_sorts_by_goals_with_goals_parameter(self):
        top_scorers = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(top_scorers[0].name, "Lemieux")
        self.assertEqual(top_scorers[1].name, "Yzerman")
        self.assertEqual(top_scorers[2].name, "Kurri")
    
    def test_top_sorts_by_goals_with_assists_parameter(self):
        top_scorers = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(top_scorers[0].name, "Gretzky")
        self.assertEqual(top_scorers[1].name, "Yzerman")
        self.assertEqual(top_scorers[2].name, "Lemieux")    

    def test_sort_by_points_returns_points(self):
        player = Player("Semenko", "EDM", 4, 12)
        self.assertEqual(sort_by_points(player), 16)

    def test_sort_by_key_returns_points(self):
        player = Player("Semenko", "EDM", 4, 12)
        self.assertEqual(sort_by_key(player, SortBy.POINTS), 16)

    def test_sort_by_key_returns_goals(self):
        player = Player("Semenko", "EDM", 4, 12)
        self.assertEqual(sort_by_key(player, SortBy.GOALS), 4)
    
    def test_sort_by_key_returns_assists(self):
        player = Player("Semenko", "EDM", 4, 12)
        self.assertEqual(sort_by_key(player, SortBy.ASSISTS), 12)