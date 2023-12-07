from statistics import Statistics
from player_reader import PlayerReader
#from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    ### Decorator pattern
    #matcher = And(
    #    HasAtLeast(5, "goals"),
    #    HasAtLeast(20, "assists"),
    #    PlaysIn("PHI")
    #)

    #matcher = And(
    #    Not(HasAtLeast(2, "goals")),
    #    PlaysIn("NYR")
    #)

    #filtered_with_all = stats.matches(All())
    #print(len(filtered_with_all))

    #matcher = Or(
    #    HasAtLeast(45, "goals"),
    #    HasAtLeast(70, "assists")
    #)

    #matcher = And(
    #    HasAtLeast(70, "points"),
    #    Or(
    #        PlaysIn("NYR"),
    #        PlaysIn("FLA"),
    #        PlaysIn("BOS")
    #    )
    #)

    ### Builder pattern

    query = QueryBuilder()
    #matcher = query.build()
    #matcher = query.playsIn("NYR").build()    
    matcher = (query
        .playsIn("NYR")
        .hasAtLeast(10, "goals")
        .hasFewerThan(20, "goals")
        .build()
    )
    
    # kutsutaan luokan statistics metodia matches, joka saa parametrikseen
    # matcher-olion. Metodi matches palauttaa listan pelaajista, jotka
    # täyttävät parametrina annetun ehtolausekkeen.
    for player in stats.matches(matcher):
        print(player)




if __name__ == "__main__":
    main()
