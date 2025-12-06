# from bakery import assert_equal
from dataclasses import dataclass
from random import *

from drafter import *

# hide_debug_information()
# set_website_framed(False)

set_website_title("BANG!")
set_website_style("sakura")
set_site_information(
    "Vishmi Rajapaksha",
    """
    Your description can go here.
    """,
    [],
    [],
    [],
)


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
    gun_range: str
    lives: int
    cards: list[Card]
    cards_in_play: list[Card]
    bangs_played_this_turn: int


@dataclass
class State:
    players: list[Player]
    roles: list[Character]
    deck: list[Card]
    discard_pile: list[Card]
    current_player: Player
    actions_taken: list[str]


@route
def index(state: State) -> Page:
    state.deck = [
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "A"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "2"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "3"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "4"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "5"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "6"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "7"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "8"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "9"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "10"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "J"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "Q"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Diamonds", "K"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "2"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "3"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "4"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "5"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "6"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "7"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "8"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "9"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "10"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "J"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "Q"),
        Card("Bang!", "play", "Shoot another player within range for 1 damage.", "Hearts", "K"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "2"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "3"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "4"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "5"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "6"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "7"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "8"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "9"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "10"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "J"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "Q"),
        Card("Missed!", "play", "Cancel a Bang! played against you.", "Spades", "K"),
        Card("Beer", "play", "Regain 1 life.", "Hearts", "6"),
        Card("Beer", "play", "Regain 1 life.", "Hearts", "7"),
        Card("Beer", "play", "Regain 1 life.", "Hearts", "8"),
        Card("Beer", "play", "Regain 1 life.", "Hearts", "9"),
        Card("Beer", "play", "Regain 1 life.", "Hearts", "10"),
        Card("Beer", "play", "Regain 1 life.", "Hearts", "J"),
        Card("Panic!", "play", "Steal a card from a player at distance 1.", "Clubs", "2"),
        Card("Panic!", "play", "Steal a card from a player at distance 1.", "Clubs", "3"),
        Card("Panic!", "play", "Steal a card from a player at distance 1.", "Clubs", "4"),
        Card("Panic!", "play", "Steal a card from a player at distance 1.", "Clubs", "5"),
        Card("Cat Balou", "play", "Discard a card from another player.", "Diamonds", "J"),
        Card("Cat Balou", "play", "Discard a card from another player.", "Diamonds", "Q"),
        Card("Cat Balou", "play", "Discard a card from another player.", "Diamonds", "K"),
        Card("Cat Balou", "play", "Discard a card from another player.", "Hearts", "J"),
        Card("Stagecoach", "play", "Draw 2 cards.", "Diamonds", "6"),
        Card("Stagecoach", "play", "Draw 2 cards.", "Diamonds", "7"),
        Card("Wells Fargo", "play", "Draw 3 cards.", "Diamonds", "8"),
        Card("General Store", "play", "Reveal cards equal to players; pick one.", "Diamonds", "9"),
        Card("General Store", "play", "Reveal cards equal to players; pick one.", "Diamonds", "10"),
        Card("Jail", "use", "Place in front of a player; they must test at the start of their turn.", "Spades", "10"),
        Card("Jail", "use", "Place in front of a player; they must test at the start of their turn.", "Hearts", "4"),
        Card("Jail", "use", "Place in front of a player; they must test at the start of their turn.", "Spades", "J"),
        Card("Indians!", "play", "All other players discard a Bang! or lose 1 life.", "Clubs", "J"),
        Card("Indians!", "play", "All other players discard a Bang! or lose 1 life.", "Clubs", "Q"),
        Card("Duel", "play", "Target another player; exchange Bang! until someone fails.", "Spades", "6"),
        Card("Duel", "play", "Target another player; exchange Bang! until someone fails.", "Spades", "7"),
        Card("Duel", "play", "Target another player; exchange Bang! until someone fails.", "Spades", "8"),
        Card("Saloon", "play", "All players regain 1 life.", "Diamonds", "K"),
        Card("Gatling", "play", "Shoot all other players for 1 life.", "Hearts", "2"),
        Card("Dynamite", "use", "At start of turn, test; explodes for 3 damage.", "Hearts", "2"),
        Card("Barrel", "use", "Flip top card when hit by Bang!; Heart = Missed.", "Spades", "Q"),
        Card("Mustang", "use", "Others see you at +1 distance.", "Hearts", "8"),
        Card("Scope", "use", "You see others at -1 distance.", "Clubs", "9"),
        Card("Volcanic", "gun", "Range 1. Allows unlimited Bang! cards.", "Spades", "10"),
        Card("Schofield", "gun", "Range 2.", "Spades", "K"),
        Card("Schofield", "gun", "Range 2.", "Clubs", "J"),
        Card("Remington", "gun", "Range 3.", "Clubs", "Q"),
        Card("Winchester", "gun", "Range 5.", "Spades", "8"),
        Card("Rev. Carabine", "gun", "Range 4.", "Clubs", "A")
    ]
    return Page(state, [Header("BANG!"), Button("Start Game",assignment)])


@route
def assignment(state: State) -> Page:
    roles = ["Sheriff", "Deputy", "Outlaw", "Renegade", "Outlaw"]

    characters = [
        # coded
        Character("Willy the Kid", 4, "May play any number of Bang! cards each turn."),
        Character("El Gringo", 3, "When he loses a life due to another player, he draws a random card from their hand."),
        Character("Rose Doolan", 4, "Has a built-in Scope (sees all other players at distance −1)."),
    
        Character("Bart Cassidy", 4, "Draws a card when he loses a life."),
        Character("Black Jack",4,"During his draw phase, reveal the second card; if it's Heart or Diamond, draw one additional card.",),
        Character("Calamity Janet", 4, "Can use Bang! cards as Missed! cards and vice versa.")
        
        
    ]
    
    """
        Character("Jesse Jones", 4, "May draw his first card from the deck or randomly from another player's hand."),
        Character("Jourdonnais", 4, "Has a built-in Barrel; when targeted by a Bang!, flip the top card to avoid it."),
        Character(
            "Kit Carlson", 4, "During his draw phase, look at the top 3 cards, choose 2 to draw, and replace the other."
        ),
        Character("Lucky Duke", 4, "When drawing, flip two cards and choose one (for Barrel, Dynamite, Jail, etc.)."),
        Character("Paul Regret", 3, "Has a built-in Mustang (others must be distance 2 to target him)."),
        Character("Pedro Ramirez", 4, "May draw his first card from the discard pile instead of the deck."),
        Character("Sid Ketchum", 4, "May discard two cards to regain 1 life."),
        Character("Slab the Killer", 4, "Players need to play two Missed! cards to avoid his Bang! cards."),
        Character("Suzy Lafayette", 4, "Whenever she plays her last card, she immediately draws a card."),
        Character("Vulture Sam", 4, "Whenever a player dies, he takes all of their cards."),
        """
    
    shuffle(roles)
    shuffle(characters)

    player = Player(1, characters[-1], "User", roles[-1], 1, 0, [], [], 0)

    if player.role == "Sheriff":
        player.lives = player.character.lives_limit + 1
    else:
        player.lives = player.character.lives_limit

    roles.pop()
    characters.pop()

    state.players.append(player)

    for i in range(2, 6):
        player = Player(i, characters[-1], "Player " + str(i), roles[-1], 1, 0, [], [], 0)

        if player.role == "Sheriff":
            player.lives = player.character.lives_limit + 1

        else:
            player.lives = player.character.lives_limit

        if player.character.name == "Rose Doolan":
            player.gun_range += 1

        roles.pop()
        characters.pop()
        state.players.append(player)

    return home(state,state.players[0])


@route
def draw_cards(state: State, num_cards: int, player: Player):
    for i in range(num_cards):
        if state.deck == []:
            state.deck = state.discard_pile
            state.discard_pile = []
            shuffle(state.deck)

        drawn_card = state.deck[-1]
        state.deck.pop()
        player.cards.append(drawn_card)


@route
def home(state: State, player: Player) -> Page:
    if not state.current_player.name == player.name:
        draw_cards(state, 2, player)
        state.current_player = player
        player.bangs_played_this_turn = 0

        if state.actions_taken:
            last_action = state.actions_taken[-4:]
        else:
            last_action = "You make the first move."
    else:
        last_action = state.actions_taken[-1]

    options = []
    hand = ""

    for card in player.cards:
        hand += card.name + ": "
        hand += card.description
        hand += "\n"
        options.append(card.name)

    in_play_cards = ""
    for card in player.cards_in_play:
        in_play_cards += card.name + ": "
        in_play_cards += card.description
        in_play_cards += "\n"

    targets = ["N/A"]
    for player in state.players:
        if not player.name == player.name:
            targets.append(player.name)

    return Page(
        state,[
        Header("Your Turn"),
        Span(
            last_action,
            LineBreak(),
            "Lives Left: " + str(player.lives),
            "\n",
            "Your role: " + player.role,
            "\n",
            "Your power: " + player.character.power,
            "\n",
            "Your cards in play:",
            "\n",
            in_play_cards,
            LineBreak(),
            "The cards in your hand:",
            hand,
            "\n",
            LineBreak(),
            "What card do you want to play? ->",
            SelectBox("card_to_play", options, options[0]),
            LineBreak(),
            "Who do you want to target? ->",
            SelectBox("target_player", targets, targets[0]),
            LineBreak(),
            Button("Play Card", play_card),
            " ",
            Button("Discard", discard_card),
            LineBreak(),
            LineBreak(),
            Button("Use Power", use_power),
            " ",
            Button("End Turn", other_player_turn),
        )
    ])


@route
def use_power(state: State, player: Player) -> Page:
    if player.character.name == "Bart Cassidy":
        draw_cards(state, 1, player)

    return home(state)


@route
def play_card(state: State, player: Player) -> Page:
    card_played = Card("", "", "", "", "")
    for card in player.cards:
        if card.name == card_to_play:
            player.cards.remove(card)
            state.discard_pile.append(card)
            break

    if card_played.name == "Bang!":
        if player.bangs_played_this_turn < 1 or player.character.name == "Willy the Kid":
            for enemy in state.players:
                if enemy.name == target_player:
                    if in_range(player, enemy):
                        if enemy.cards.count("Missed!") > 0:
                            enemy.cards.remove("Missed!")
                        else:
                            enemy.lives -= 1
                            state.actions_taken.append(player.name + " played Bang! on " + enemy.name + ".")
                            if enemy.character.name == "El Gringo":
                                enemy.cards.append(player.cards[-1])
                                player.cards.pop()
                    else:
                        state.actions_taken.append(enemy.name + " is out of range.")
                    break

        player.bangs_played_this_turn += 1

    elif card_played.type_name == "gun":
        player.gun_range = int(card_played.description.split(" ")[1].strip("."))
        if player.character.name == "Rose Doolan":
            player.gun_range += 1
        state.actions_taken.append(player.name + " equipped " + card_played.name + ".")

    elif card_played.name == "Beer":
        if player.lives < player.character.lives_limit:
            player.lives += 1
            state.actions_taken.append(player.name + " played Beer and regained 1 life.")
        else:
            state.actions_taken.append(player.name + " is already at max lives.")

    return home(state)


@route
def in_range(player: Player, enemy: Player) -> bool:
    distance = abs(player.number - enemy.number)
    if distance <= player.gun_range:
        return True
    return False


@route
def discard_card(state: State, player: Player) -> Page:
    return home(state)


@route
def other_player_turn(state: State, player: Player) -> Page:
    if len(played.cards) > player.lives:
        state.actions_taken.append("You must discard down to " + str(player.lives) + " cards.")
        return home(state)
    if state.current_player.name == "Player 5":
        state.current_player = "User"
    return home(state)


start_server(State([],[],[],[],Player(0,Character("",0,""),"","","",0,[],[],0),[]))

