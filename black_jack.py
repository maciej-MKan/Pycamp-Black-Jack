#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

"""Backjack game simulator."""

from random import shuffle

color_list = ['serce', 'karo', 'pik', 'trefl']
figure_list = ['2','3','4','5','6','7','8','9','10','walet','dama','król','as']

class Card:
    """A class that describes a playing card."""

    def __init__(self, color, figure) -> None:
        self.color = color
        self.figure = figure
        self.value = figure_list.index(figure) + 2

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
    def __init__(self) -> None:
        self.stored_cards = []
        self.deck = []

    def __int__(self) -> int:
        return self.get_cards_value()

    def first_run(self):
    """The course of the player's first turn"""

        self.stored_cards.append(self.deck.get_card())
        self.stored_cards.append(self.deck.get_card())

    def draw_card(self):
    """The corse of player's next turn"""
        self.stored_cards.append(self.deck.get_card())

    def get_cards_value(self):
    """Calculate value of player's card

    Returns:
        int: sum values of player's catds
    """
        return sum([card.value for card in self.stored_cards])

class Game:
    """The class that carries out the course of the game
    
    Args:
        Player class instances for the dealer and the user
    """

    def __init__(self, croupier, player) -> None:
        self.croupier = croupier
        self.player = player
        self.croupier.deck = Deck()
        self.player.deck = self.croupier.deck

    def first_run(self):
    """The course of the first round of the game"""
        self.player.first_run()
        if int(self.player) >= 21:
            raise Exception
        self.croupier.first_run()
        return self.player.stored_cards, self.croupier.stored_cards[0]

    def player_run(self):
    """The player's next turns
    
    Returns:
        list[Card]: player's stored cards
    """
        self.player.draw_card()
        if int(self.player) > 21:
            raise Exception
        return self.player.stored_cards

    def croupier_run(self):
    """The croupier's next turn
    
    Returns:
        list[Card]: croupier's stored cards
    """
        while int(self.croupier) <= int(self.player):
            self.croupier.draw_card()
            if int(self.croupier) >21:
                raise Exception
        return self.croupier.stored_cards

if __name__ == '__main__':

    player = Player()
    krupier = Player()
    game = Game(krupier, player)
    try:
        player_cards, krupier_card = game.first_run()
    except:
        print('!!!BLACK JACK!!!')
    else:
        try:
            print(f'Masz {player_cards} , krupier ma {krupier_card} ')
            draw_next = input('dobierasz kartę? (t/n) ')
        except:
            print('Przegrywasz')
        else:
            try:
                while draw_next == 't':
                    print(f'Masz {game.player_run()} , {int(player)} ')
                    draw_next = input('dobierasz kartę? (t/n) ')
            
                print(f'krupier ma {game.croupier_run()} , {int(krupier)} ')
                if int(krupier) > int(player):
                    print('Przegrywasz')
                else:
                    print('WYGRYWASZ')
            except:
                print('Wygrywasz')
