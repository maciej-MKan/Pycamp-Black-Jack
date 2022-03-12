#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

"""_summary_

    Returns:
        _type_: _description_
    """
from random import shuffle

color_list = ['serce', 'karo', 'pik', 'trefl']
figure_list = ['2','3','4','5','6','7','8','9','10','walet','dama','król','as']

class Card:
    """_summary_
    """
    def __init__(self, color, figure) -> None:
        self.color = color
        self.figure = figure
        self.value = figure_list.index(figure) + 2

    def __repr__(self) -> str:
        return f'{self.figure}_{self.color}'

class Deck:
    """_summary_
    """
    def __init__(self) -> None:
        self._card_deck = []
        self._create_deck()
        self.shuffle_cards()
        
    def _create_deck(self):
        for color in color_list:
            for figure in figure_list:
                self._card_deck.append(f'{color}_{figure}')
                self._card_deck[-1] = Card(color, figure)

    def get_card(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._card_deck.pop()

    def shuffle_cards(self):
        """_summary_
        """
        shuffle(self._card_deck)

    def get_deck(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._card_deck

class Player():
    """_summary_
    """
    def __init__(self) -> None:
        self.stored_cards = []
        self.deck = []

    def __int__(self) -> int:
        return self.get_cards_value()

    def play(self):
        if len(self.stored_cards):
            self.draw_card()
        else:
            self.first_run()

    def first_run(self):
        self.stored_cards.append(self.deck.get_card())
        self.stored_cards.append(self.deck.get_card())

    def draw_card(self):
        self.stored_cards.append(self.deck.get_card())

    def get_cards_value(self):
        return sum([card.value for card in self.stored_cards])

class Game:

    def __init__(self, croupier, player) -> None:
        self.croupier = croupier
        self.player = player
        self.croupier.deck = Deck()
        self.player.deck = self.croupier.deck

    def first_run(self):
        self.player.play()
        self.croupier.play()
        return self.player.stored_cards, self.croupier.stored_cards[0]

    def player_run(self):
        self.player.play()
        return self.player.stored_cards

    def croupier_run(self):
        while int(self.croupier) < int(self.player):
            self.croupier.play()
        return self.croupier.stored_cards

if __name__ == '__main__':

    player = Player()
    krupier = Player()
    game = Game(krupier, player)
    player_cards, krupier_card = game.first_run()
    print(f'Masz {player_cards} , krupier ma {krupier_card} ')
    draw_next = input('dobierasz kartę? (t/n) ')
    
    while draw_next == 't':
        print(f'Masz {game.player_run()} , {int(player)} ')
        draw_next = input('dobierasz kartę? (t/n) ')
    
    print(f'krupier ma {game.croupier_run()} , {int(krupier)} ')
