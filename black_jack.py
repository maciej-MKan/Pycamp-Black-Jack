#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-

"""Backjack game simulator."""

from dataclasses import dataclass, field
from random import shuffle
from card_settings import color_list, figure_list, value_list

class OverTwentyOne(Exception):
    """Exception class over 21"""
    def __init__(self, player) -> None:
        super().__init__(player)
        self.stored_cards = player.stored_cards

class BlackJack(Exception):
    """Exception when player has 21 points"""
    def __init__(self, player) -> None:
        super().__init__(player)
        self.stored_cards = player.stored_cards

@dataclass(repr=False, frozen=True)
class Card:
    """A class that describes a playing card."""

    color : str
    figure : str
    value : int = field(init=False, repr=False, default=0)

    def __post_init__(self):
        object.__setattr__(self, 'value', value_list[figure_list.index(self.figure)])

    def __repr__(self) -> str:
        return f'{self.figure}_{self.color}'

class Deck:
    """A class that creates a deck of cards from a list of figures and colors.
Performs shuffling methods and takes a card from the deck.
    """
    def __init__(self) -> None:
        self._card_deck = []
        self._create_deck()
        self.shuffle_cards()

    def _create_deck(self):
        """Creates the deck
        """
        for color in color_list:
            for figure in figure_list:
                self._card_deck.append(f'{color}_{figure}')
                self._card_deck[-1] = Card(color, figure)

    def get_card(self):
        """Takes a card

        Returns:
            Card: first cart from deck.
        """
        return self._card_deck.pop()

    def shuffle_cards(self):
        """Shuffle deck"""
        shuffle(self._card_deck)

    def get_deck(self):
        """Takes all of deck

        Returns:
            list[card]: list of all cards in the deck
        """
        return self._card_deck

class Player():
    """The class creates a player, stores the cards they have collected,
allows them to take cards for 1 and further turns,
and calculates the value of the cards they have collected.
Class value (int) returns the value of the player's cards.
    """
    def __init__(self, name) -> None:
        self.stored_cards = []
        self.deck = Game.deck
        self.name = name

    def __int__(self) -> int:
        return Game.calculate_card_value(self)

    def __str__(self) -> str:
        return self.name

    def draw_card(self):
        """The corse of player's next turn"""
        self.stored_cards.append(self.deck.get_card())

class Game:
    """The class that carries out the course of the game

    Args:
        Player class instances for the dealer and the user
    """
    deck = Deck()
    def __init__(self, croupier, human) -> None:
        self.croupier : Player = croupier
        self.human : Player = human

    def run(self, input_foo, msg : str):
        """The course of game tour

        Args:
            input_foo (funkcjon): input data funkcjon
            msg (str): message for input_foo

        Yields:
            list[Card], list[Card]: lists of player and croupier stored cards
        """
        if not self.human.stored_cards:
            self.first_run()
            yield self.human.stored_cards, self.croupier.stored_cards[0]
        while input_foo(msg) != 'n':
            self.player_run()
            yield self.human.stored_cards, self.croupier.stored_cards[0]
        self.croupier_run()

    def first_run(self):
        """The course of the first round of the game"""
        for player in [self.human, self.croupier]:
            player.draw_card()
            player.draw_card()
            if int(self.human) >= 21:
                raise BlackJack(self.human)

    def player_run(self):
        """The player's next turns"""
        self.human.draw_card()
        if int(self.human) > 21:
            raise OverTwentyOne(self.human)

    def croupier_run(self):
        """The croupier's next turn"""
        while int(self.croupier) <= 16:
            self.croupier.draw_card()
            if int(self.croupier) > 21:
                raise OverTwentyOne(self.croupier)

    def check_winner(self):
        """method for checking who is winner

        Returns:
            Player: player with higest value of points
        """
        players = [self.human, self.croupier]
        players.sort(key=int)
        return players[-1]

    @staticmethod
    def calculate_card_value(player : Player):
        """calculating player's stored cards

        Args:
            player (Player): instance of Player

        Returns:
            int: sum values of cards stored by player
        """
        cards_value = sum([card.value for card in player.stored_cards])
        if [True for card in player.stored_cards if card.figure.upper() == 'A']\
         and cards_value <= 11:
            cards_value +=10
        return cards_value

if __name__ == '__main__':

    gracz = Player('Gracz')
    krupier = Player('Krupier')
    game = Game(krupier, gracz)

    try:
        for player_cards, krupier_card in game.run(input, 'dobierasz kartę? (t/n) '):
            print(f'Masz {player_cards}, krupier ma {krupier_card}')
    except BlackJack as lucky_player:
        print(f'{lucky_player} ma 21. Wygrywa')
        print(lucky_player.stored_cards)
    except OverTwentyOne as lost_player:
        print(f'{lost_player} przekroczył 21. Przegrywa', end=' ')
        print(lost_player.stored_cards)
    else:
        print(f'Masz {gracz.stored_cards}, krupier ma {krupier.stored_cards}')
        print(f'{game.check_winner()} zdobył więcej punktów. Wygrywa')
