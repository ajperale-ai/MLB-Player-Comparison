from dataclasses import dataclass
from drafter import *


# -------------------------
# Dataclasses
# -------------------------

@dataclass
class Player:
    name: str
    season: int
    batting_average: float
    home_runs: int
    rbi: int
    obp: float
    slg: float
    ops: float


@dataclass
class State:
    players: list[Player]
    selected_player1: str
    selected_player2: str
    selected_season: str
    message: str


# -------------------------
# Player Data
# -------------------------

players = [
    Player("Aaron Judge", 2024, 0.322, 58, 144, 0.458, 0.701, 1.159),
    Player("Shohei Ohtani", 2024, 0.310, 54, 130, 0.390, 0.646, 1.036),
    Player("Juan Soto", 2024, 0.288, 41, 109, 0.419, 0.569, 0.989),
    Player("Mookie Betts", 2024, 0.289, 19, 75, 0.372, 0.491, 0.863),
    Player("Bobby Witt Jr.", 2024, 0.332, 32, 109, 0.389, 0.588, 0.977),
    Player("Gunnar Henderson", 2024, 0.281, 37, 92, 0.364, 0.529, 0.893),
    Player("Vladimir Guerrero Jr.", 2024, 0.323, 30, 103, 0.396, 0.544, 0.940),
    Player("Yordan Alvarez", 2024, 0.308, 35, 86, 0.392, 0.567, 0.959),
    Player("Marcell Ozuna", 2024, 0.302, 39, 104, 0.378, 0.546, 0.925),
    Player("Jose Ramirez", 2024, 0.279, 39, 118, 0.335, 0.537, 0.872),
    Player("Brent Rooker", 2024, 0.293, 39, 112, 0.365, 0.562, 0.927),
    Player("Kyle Schwarber", 2024, 0.248, 38, 104, 0.366, 0.485, 0.851),
    Player("Anthony Santander", 2024, 0.235, 44, 102, 0.308, 0.506, 0.814),
    Player("Ketel Marte", 2024, 0.292, 36, 95, 0.372, 0.560, 0.932),
    Player("Francisco Lindor", 2024, 0.273, 33, 91, 0.345, 0.500, 0.845),
    Player("Pete Alonso", 2024, 0.240, 34, 88, 0.329, 0.459, 0.788),
    Player("Aaron Judge", 2025, 0.331, 53, 114, 0.457, 0.688, 1.144),
    Player("Shohei Ohtani", 2025, 0.282, 55, 102, 0.392, 0.622, 1.014),
    Player("Juan Soto", 2025, 0.263, 43, 105, 0.396, 0.525, 0.921),
    Player("Mookie Betts", 2025, 0.258, 20, 82, 0.326, 0.406, 0.732),
    Player("Bobby Witt Jr.", 2025, 0.295, 23, 88, 0.351, 0.501, 0.852),
    Player("Gunnar Henderson", 2025, 0.274, 17, 68, 0.349, 0.438, 0.787),
    Player("Vladimir Guerrero Jr.", 2025, 0.292, 23, 84, 0.381, 0.467, 0.848),
    Player("Yordan Alvarez", 2025, 0.273, 6, 27, 0.367, 0.430, 0.797),
    Player("Marcell Ozuna", 2025, 0.232, 21, 68, 0.355, 0.400, 0.755),
    Player("Jose Ramirez", 2025, 0.283, 30, 85, 0.360, 0.503, 0.863),
    Player("Brent Rooker", 2025, 0.262, 30, 89, 0.335, 0.479, 0.814),
    Player("Kyle Schwarber", 2025, 0.240, 56, 132, 0.365, 0.563, 0.928),
    Player("Anthony Santander", 2025, 0.175, 6, 18, 0.271, 0.294, 0.565),
    Player("Ketel Marte", 2025, 0.283, 28, 72, 0.376, 0.517, 0.893),
    Player("Francisco Lindor", 2025, 0.267, 31, 86, 0.346, 0.466, 0.812),
    Player("Pete Alonso", 2025, 0.272, 38, 126, 0.347, 0.524, 0.871),
    Player("Aaron Judge", 2023, 0.267, 37, 75, 0.406, 0.613, 1.019),
    Player("Shohei Ohtani", 2023, 0.304, 44, 95, 0.412, 0.654, 1.066),
    Player("Juan Soto", 2023, 0.275, 35, 109, 0.410, 0.519, 0.930),
    Player("Mookie Betts", 2023, 0.307, 39, 107, 0.408, 0.579, 0.987),
    Player("Bobby Witt Jr.", 2023, 0.276, 30, 96, 0.319, 0.495, 0.813),
    Player("Gunnar Henderson", 2023, 0.255, 28, 82, 0.325, 0.489, 0.814),
    Player("Vladimir Guerrero Jr.", 2023, 0.264, 26, 94, 0.345, 0.444, 0.788),
    Player("Yordan Alvarez", 2023, 0.293, 31, 97, 0.407, 0.583, 0.990),
    Player("Marcell Ozuna", 2023, 0.274, 40, 100, 0.346, 0.558, 0.905),
    Player("Jose Ramirez", 2023, 0.282, 24, 80, 0.356, 0.475, 0.831),
    Player("Brent Rooker", 2023, 0.246, 30, 69, 0.329, 0.488, 0.817),
    Player("Kyle Schwarber", 2023, 0.197, 47, 104, 0.343, 0.474, 0.817),
    Player("Anthony Santander", 2023, 0.257, 28, 95, 0.325, 0.472, 0.797),
    Player("Ketel Marte", 2023, 0.276, 25, 82, 0.358, 0.485, 0.844),
    Player("Francisco Lindor", 2023, 0.254, 31, 98, 0.336, 0.470, 0.806),
    Player("Pete Alonso", 2023, 0.217, 46, 118, 0.318, 0.504, 0.821)
]

set_website_title("MLB Player Comparison")

set_site_information(
    author="Anthony Perales",
    description="Compare statistics from different MLB players and seasons.",
    sources="MLB statistics from Baseball Reference and MLB.com.",
    planning=["CS1 Final Project Design.docx"],
    links=["https://github.com/ajperale-ai/your-repository"]
)

hide_debug_information()
set_website_framed(False)

# -------------------------
# Helper Functions
# -------------------------

def find_player(state: State, player_name: str) -> Player:
    """Finds a player by name."""
    for player in state.players:
        if player.name == player_name:
            return player

    return state.players[0]


def compare_stat(stat1: float, stat2: float) -> str:
    """Compares two stats."""
    if stat1 > stat2:
        return "Player 1"
    elif stat2 > stat1:
        return "Player 2"
    else:
        return "Tie"



# -------------------------
# Route 1: Home Page
# -------------------------

@route
def index(state: State) -> Page:
    """Shows the home page."""
    return Page(state, [
        Header("MLB Player Comparison"),
        Text("Compare your favorite MLB hitters!"),
        Text("Choose two players and compare their statistics."),
        Button("Start Comparing", "player_select"),
        Button("View All Players", "player_list"),
        Button("Stat Leaders", "stat_leaders")
    ])


# -------------------------
# Route 2: Player Selection
# -------------------------

@route
def player_select(state: State) -> Page:
    """Lets users choose players."""
    player_names = []

    for player in state.players:
        player_names.append(player.name)

    return Page(state, [
        Header("Choose Your Players"),
        Text("Select the first player:"),
        SelectBox("selected_player1", player_names),
        Text("Select the second player:"),
        SelectBox("selected_player2", player_names),
        Text("Select a season:"),
        SelectBox("selected_season", ["2023", "2024", "2025"]),
        Text(state.message),
        Button("Compare Players", "compare_players"),
        Button("Back Home", "index")
    ])


# -------------------------
# Route 3: Compare Players
# -------------------------

@route
def compare_players(state: State, selected_player1: str,
                    selected_player2: str, selected_season: str) -> Page:
    """Checks the player selections."""


    state.selected_player1 = selected_player1
    state.selected_player2 = selected_player2
    state.selected_season = selected_season
    

    if state.selected_player1 == state.selected_player2:
        state.message = "Please select two different players."
        return Page(state, [
            Header("Invalid Selection"),
            Text(state.message),
            Button("Go Back", "player_select")
        ])

    state.message = "Comparison completed!"

    return Page(state, [
        Header("Comparison Ready"),
        Text("Your players have been selected."),
        Button("View Results", "results"),
        Button("Choose Different Players", "player_select")
    ])


# -------------------------
# Route 4: Results Page
# -------------------------

@route
def results(state: State) -> Page:
    """Shows the player comparison."""
    player1 = find_player(state, state.selected_player1)
    player2 = find_player(state, state.selected_player2)

    return Page(state, [
        Header("Player Comparison Results"),

        Text("Player 1: " + player1.name),
        Text("Player 2: " + player2.name),

        Header("Statistics"),

        Text("Batting Average"),
        Text(str(player1.batting_average) + " vs " +
             str(player2.batting_average)),
        Text("Higher: " + compare_stat(
            player1.batting_average, player2.batting_average)),

        Text("Home Runs"),
        Text(str(player1.home_runs) + " vs " +
             str(player2.home_runs)),
        Text("Higher: " + compare_stat(
            player1.home_runs, player2.home_runs)),

        Text("Runs Batted In"),
        Text(str(player1.rbi) + " vs " + str(player2.rbi)),
        Text("Higher: " + compare_stat(player1.rbi, player2.rbi)),

        Text("On Base Percentage"),
        Text(str(player1.obp) + " vs " + str(player2.obp)),
        Text("Higher: " + compare_stat(player1.obp, player2.obp)),

        Text("Slugging Percentage"),
        Text(str(player1.slg) + " vs " + str(player2.slg)),
        Text("Higher: " + compare_stat(player1.slg, player2.slg)),

        Text("OPS"),
        Text(str(player1.ops) + " vs " + str(player2.ops)),
        Text("Higher: " + compare_stat(player1.ops, player2.ops)),

        Button("View Player Details", "player_details"),
        Button("Compare Again", "player_select"),
        Button("Home", "index")
    ])


# -------------------------
# Route 5: Player Details
# -------------------------

@route
def player_details(state: State) -> Page:
    """Shows one player's stats."""
    player = find_player(state, state.selected_player1)

    return Page(state, [
        Header(player.name),
        Text("Season: " + str(player.season)),
        Text("Batting Average: " + str(player.batting_average)),
        Text("Home Runs: " + str(player.home_runs)),
        Text("RBI: " + str(player.rbi)),
        Text("OBP: " + str(player.obp)),
        Text("SLG: " + str(player.slg)),
        Text("OPS: " + str(player.ops)),
        Button("Back to Results", "results"),
        Button("Home", "index")
    ])


# -------------------------
# Route 6: Player List
# -------------------------

@route
def player_list(state: State) -> Page:
    """Shows all available players."""
    content = [Header("Available MLB Players")]

    for player in state.players:
        content.append(Text(player.name))
        content.append(Text("Season: " + str(player.season)))
        content.append(Text("AVG: " + str(player.batting_average)))
        content.append(Text("Home Runs: " + str(player.home_runs)))

    content.append(Button("Compare Players", "player_select"))
    content.append(Button("Home", "index"))

    return Page(state, content)


# -------------------------
# Route 7: Stat Leaders
# -------------------------

@route
def stat_leaders(state: State) -> Page:
    """Finds the top players in stats."""
    highest_home_runs = state.players[0]
    highest_average = state.players[0]

    for player in state.players:
        if player.home_runs > highest_home_runs.home_runs:
            highest_home_runs = player

        if player.batting_average > highest_average.batting_average:
            highest_average = player

    return Page(state, [
        Header("Stat Leaders"),
        Text("Home Run Leader: " + highest_home_runs.name),
        Text("Home Runs: " + str(highest_home_runs.home_runs)),
        Text("Batting Average Leader: " + highest_average.name),
        Text("Batting Average: " + str(highest_average.batting_average)),
        Button("View All Players", "player_list"),
        Button("Compare Players", "player_select"),
        Button("Home", "index")
    ])


# -------------------------
# Start Website
# -------------------------

initial_state = State(
    players,
    "",
    "",
    "2024",
    ""
)

start_server(initial_state)


