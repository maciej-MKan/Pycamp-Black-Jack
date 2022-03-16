#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

"""Backjack game simulator."""

from dataclasses import dataclass, field
from random import shuffle
from card_settings import color_list, figure_list, value_list

class OverTwentyOne(Exception):
    """Exception class"""
    def __init__(self, player_obiect, *args: object) -> None:
        super().__init__(*args)
        self.player = player_obiect

    def __str__(self):
        return f'{self.player.name} przekroczył 21 punktów.'

class BlackJack(Exception):
    """Exception when player has 21 points"""

@dataclass(repr=False, frozen=True)
class Card:
    """A class that describes a playing card."""

    color : str
    figure : str
    value : int = field(init=False, repr=False, default=0)

    def __post_init__(self):
        object.__setattr__(self, 'value', value_list[figure_list.index(self.figure)])

    def __repr__(self) -> str:
        return f'{self.figure} _ {self.color}'

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

    def first_run(self):
        """The course of the first round of the game

        Returns:
            tupe(list[Card]): collected player's cards, one of the dealer's cards
        """
        for player in [self.human, self.croupier]:
            player.draw_card()
            player.draw_card()
        return self.human.stored_cards, self.croupier.stored_cards[0]

    def player_run(self):
        """The player's next turns

        Returns:
            list[Card]: player's stored cards
        """
        self.human.draw_card()
        if int(self.human) > 21:
            raise OverTwentyOne(self.human)
        return self.human.stored_cards

    def croupier_run(self):
        """The croupier's next turn

        Returns:
            list[Card]: croupier's stored cards
        """
        while int(self.croupier) <= 16:
            self.croupier.draw_card()
            if int(self.croupier) > 21:
                raise OverTwentyOne(self.croupier)
        return self.croupier.stored_cards

    @staticmethod
    def calculate_card_value(player : Player):
        """calculating player's stored cards

        Args:
            player (Player): instance of Player

        Returns:
            int: sum values of cards stored by player
        """
        cards_value = sum([card.value for card in player.stored_cards])
        if [True for card in player.stored_cards if card.figure.upper() == 'AS']\
         and cards_value <= 11:
            cards_value +=10
        if cards_value == 21:
                raise BlackJack(f'Black Jack! {player.name} wygrywa')
        return cards_value

if __name__ == '__main__':

    gracz = Player('Gracz')
    krupier = Player('Krupier')
    game = Game(krupier, gracz)
    try:
        player_cards, krupier_card = game.first_run()
    except BlackJack as message:
        print(message)
        print(gracz.stored_cards)
    else:
        try:
            print(f'Masz {player_cards} {int(gracz)}, krupier ma {krupier_card} {int(krupier)}')
            draw_next = input('dobierasz kartę? (t/n) ')
        except OverTwentyOne as message:
            print(message)
            print(gracz.stored_cards)
        else:
            try:
                while draw_next == 't':
                    print(f'Masz {game.player_run()} , {int(gracz)} ')
                    draw_next = input('dobierasz kartę? (t/n) ')

                print(f'krupier ma {game.croupier_run()} , {int(krupier)} ')
                if int(krupier) > int(gracz):
                    print('Przegrywasz')
                else:
                    print('WYGRYWASZ')
            except OverTwentyOne as message:
                print(message)
                print(gracz.stored_cards)
