import json

# Open the log file and load any existing data
log_file = 'board_game_recommendations.json'
try:
    with open(log_file, 'r') as f:
        board_game_counts = json.load(f)
except FileNotFoundError:
    board_game_counts = {}

# Implement a function to recommend board games
def recommend_board_game():
    # Your board game recommendation logic goes here
    recommended_game = 'Settlers of Catan'

    # Increment the count for the recommended game
    if recommended_game in board_game_counts:
        board_game_counts[recommended_game] += 1
    else:
        board_game_counts[recommended_game] = 1

    # Log the board game counts to the file
    with open(log_file, 'w') as f:
        json.dump(board_game_counts, f, indent=4)

    return recommended_game