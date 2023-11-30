class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        # equal score
        if self.m_score1 == self.m_score2:
            return self.equal_score()
        # advantage or win
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.advantage_or_win()
        # normal score        
        else:
            return self.normal_score()

    def equal_score(self):
        scores = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]
        if self.m_score1 >= 3: # Deuce
            return scores[3]
        return scores[self.m_score1]
        
    def advantage_or_win(self):
        scores = {1: "Advantage player1", -1: "Advantage player2", 2: "Win for player1", -2: "Win for player2"}
        minus_result = self.m_score1 - self.m_score2
        
        if minus_result == 1 or minus_result == -1:
            return scores[minus_result]
        elif minus_result >= 2: 
            return scores[2]
        else:
            return scores[-2]
        
    def normal_score(self):
        scores = ["Love", "Fifteen", "Thirty", "Forty"]
        return scores[self.m_score1] + "-" + scores[self.m_score2]