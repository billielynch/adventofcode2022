ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"
WIN = "WIN"
LOSE = "LOSE"
DRAW = "DRAW"


BAD_DECODER = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

CORRECT_DECODER = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN,
}

MOVE_SCORER = {ROCK: 1, PAPER: 2, SCISSORS: 3}

RESULT_MAP = {
    (ROCK, ROCK): DRAW,
    (SCISSORS, SCISSORS): DRAW,
    (PAPER, PAPER): DRAW,
    (ROCK, PAPER): WIN,
    (PAPER, SCISSORS): WIN,
    (SCISSORS, ROCK): WIN,
    (SCISSORS, PAPER): LOSE,
    (ROCK, SCISSORS): LOSE,
    (PAPER, ROCK): LOSE,
}

ENGINEERED_RESULTS_MAP = {
    (opposition_move, result): player_move
    for (opposition_move, player_move), result in RESULT_MAP.items()
}

RESULT_SCORER = {DRAW: 3, WIN: 6, LOSE: 0}


def game_score_total(game):
    _, player_move = game
    my_move_score = MOVE_SCORER[player_move]
    results_score = RESULT_SCORER[RESULT_MAP[game]]
    return my_move_score + results_score


def decode_games(games, decoder):
    decode_game = lambda game: (decoder[game[0]], decoder[game[1]])
    return [decode_game(game) for game in games]


INPUT_FILE = "2/input.txt"
with open(INPUT_FILE) as input_file:
    read_data = input_file.read()

encoded_games = [game.split(" ") for game in read_data.split("\n")]

# Part 1
badly_decoded_games = decode_games(encoded_games, BAD_DECODER)
answer1 = sum([game_score_total(game) for game in badly_decoded_games])
print(answer1)

# Part 2
properly_decoded_games = decode_games(encoded_games, CORRECT_DECODER)
inferred_games = [
    (opposition_move, ENGINEERED_RESULTS_MAP[(opposition_move, result)])
    for opposition_move, result in properly_decoded_games
]
answer2 = sum([game_score_total(game) for game in inferred_games])
print(answer2)
