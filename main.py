from dataclasses import dataclass
from random import shuffle
from typing import List
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

@dataclass
class Card:
    name: str
    type_name: str
    description: str
    suit: str
    rank: str

@dataclass
class Character:
    name: str
    lives_limit: int
    power: str

@dataclass
class Player:
    number: int
    character: Character
    name: str
    role: str
    gun_range: int
    lives: int
    cards: List[Card]
    cards_in_play: List[Card]
    bangs_played_this_turn: int

@dataclass
class State:
    players: List[Player]
    roles: List[str]
    deck: List[Card]
    discard_pile: List[Card]
    current_player: Player
    actions_taken: List[str]

### Utility functions

def build_deck() -> List[Card]:
    return [
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "A"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "2"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "2"),
        Card("Beer", "play", "Regain 1 life.", "Hearts", "6"),
        # ... For brevity, add more as needed ...
    ] * 10  # Example: make a bigger deck

def build_characters():
    return [
        Character("Willy the Kid", 4, "May play any number of Bang! cards each turn."),
        Character("El Gringo", 3, "When he loses a life due to another player, he draws a random card from their hand."),
        Character("Rose Doolan", 4, "Has a built-in Scope (sees all other players at distance −1)."),
        Character("Bart Cassidy", 4, "Draws a card when he loses a life."),
        Character("Black Jack",4,"During his draw phase, reveal the second card; if it's Heart or Diamond, draw one additional card."),
        Character("Calamity Janet", 4, "Can use Bang! cards as Missed! cards and vice versa."),
    ]

def build_roles(): 
    return ["Sheriff", "Deputy", "Outlaw", "Renegade", "Outlaw"]

### Flask routes

@app.route('/')
def index():
    # Reset game state
    deck = build_deck()
    shuffle(deck)
    roles = build_roles()
    characters = build_characters()
    shuffle(roles)
    shuffle(characters)
    players = []
    actions_taken = []
    discard_pile = []

    # Make user player (number 1)
    user_char = characters.pop()
    user_role = roles.pop()
    user_player = Player(1, user_char, "User", user_role, 1, user_char.lives_limit + (1 if user_role == "Sheriff" else 0), [], [], 0)
    players.append(user_player)
    # AI players
    for i in range(2, 6):
        char = characters.pop()
        role = roles.pop()
        lives = char.lives_limit + (1 if role == "Sheriff" else 0)
        players.append(Player(i, char, f"Player {i}", role, 1, lives, [], [], 0))

    state = State(players, build_roles(), deck, discard_pile, players[0], actions_taken)
    # Save state in session
    app.config['state'] = state
    return redirect(url_for('home'))

@app.route('/home')
def home():
    state = app.config.get('state')
    player = state.current_player
    hand = [card.name for card in player.cards]
    form_html = """
    <h1>Your Turn: {name}</h1>
    <p>Lives: {lives} | Role: {role} | Power: {power}</p>
    <p>Hand: {hand}</p>
    <form method="post" action="/draw">
      <input type="submit" value="Draw 2 Cards"/>
    </form>
    <form method="post" action="/endturn">
      <input type="submit" value="End Turn"/>
    </form>
    """.format(
        name=player.name, role=player.role, lives=player.lives, hand=", ".join(hand), power=player.character.power
    )
    return render_template_string(form_html)

@app.route('/draw', methods=['POST'])
def draw():
    state = app.config.get('state')
    player = state.current_player
    draw_cards(state, 2, player)
    state.actions_taken.append(f"{player.name} drew 2 cards.")
    return redirect(url_for('home'))

@app.route('/endturn', methods=['POST'])
def endturn():
    state = app.config.get('state')
    idx = state.players.index(state.current_player)
    idx = (idx + 1) % len(state.players)
    state.current_player = state.players[idx]
    state.actions_taken.append(f"{state.current_player.name}'s turn.")
    return redirect(url_for('home'))

### Game logic

def draw_cards(state: State, num_cards: int, player: Player):
    for i in range(num_cards):
        if not state.deck:
            state.deck = state.discard_pile
            state.discard_pile = []
            shuffle(state.deck)
        if state.deck:
            card = state.deck.pop()
            player.cards.append(card)

