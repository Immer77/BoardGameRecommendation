import csv
import tkinter as tk
from tkinter import ttk
from tkinter import *

def load_board_games(filename):
    board_games = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            board_games.append(row)
    return board_games

def find_recommendation(board_games, category, players, complexity):
    recommendations = []
    for game in board_games:
        if game['category'] == category and \
           game['players'] == players and \
           int(game['complexity']) <= complexity:
            recommendations.append(game)
    if len(recommendations) > 0:
        return sorted(recommendations, key=lambda x: int(x['complexity']))[0]
    else:
        return None

def recommend_board_game():
    category = category_var.get()
    players = players_var.get()
    complexity = complexity_var.get()
    recommendation = find_recommendation(board_games, category, players, complexity)
    if recommendation is not None:
        result_label.config(text=f'We recommend playing {recommendation["name"]} - {recommendation["description"]}')
    else:
        result_label.config(text='Sorry, we could not find a suitable recommendation for you.')

if __name__ == '__main__':
    # Load board games from CSV file
    board_games = load_board_games('board_games.csv')

    # Create GUI
    root = tk.Tk()
    root.geometry("700x609")
    root.title('Brætspils anbefaleren x2000x')

    bgimg = PhotoImage(file = "ScaledLogog.png")
    limg = Label(root, i=bgimg)
    limg.place(x=0,y=0)

    

    # Category dropdown
    category_label = ttk.Label(root, text='Kategori:')
    category_label.pack()
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(root, textvariable=category_var, values=list(set([game['category'] for game in board_games])), state='readonly')
    category_dropdown.pack()

    # Players dropdown
    players_label = ttk.Label(root, text='Antal af Spillere:')
    players_label.pack()
    players_var = tk.StringVar()
    players_dropdown = ttk.Combobox(root, textvariable=players_var, values=list(set([game['players'] for game in board_games])), state='readonly')
    players_dropdown.pack()

    # Complexity slider
    complexity_label = ttk.Label(root, text='Kompleksitet (1-5):')
    complexity_label.pack()
    complexity_var = tk.IntVar(value=3)
    complexity_slider = ttk.Scale(root, variable=complexity_var, from_=1, to=5, orient='horizontal', length=200)
    complexity_slider.pack()

    # Recommend button
    recommend_button = ttk.Button(root, text='Anbefal', command=recommend_board_game)
    recommend_button.pack()

    # Result label
    result_label = ttk.Label(root, text='')
    result_label.pack()

    # Start GUI
    root.mainloop()
