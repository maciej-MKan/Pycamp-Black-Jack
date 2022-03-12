#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

"""_summary_

    Returns:
        _type_: _description_
    """
from random import shuffle
from abc import ABC, abstractmethod

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

class Player(ABC):
    """_summary_
    """
    def __init__(self, deck) -> None:
        self._stored_cards = []
        self.deck = deck

    def __int__(self) -> int:
        return self.get_cards_value()

    def first_run(self):
        self._stored_cards.append(self.deck.get_card())
        self._stored_cards.append(self.deck.get_card())

    def play(self):
        if len(self._stored_cards):
            self.draw_card()
        else:
            self.first_run()

    def get_cards_value(self):
        return sum([card.value for card in self._stored_cards])

    @abstractmethod
    def draw_card():
        pass

class Human(Player):
    """_summary_

    Args:
        Player (_type_): _description_
    """
    def __init__(self,deck) -> None:
        super().__init__(deck)

    def draw_card(self):
        self._stored_cards.append(self.deck.get_card())
    
class Croupier(Player):
    def __init__(self,deck) -> None:
        super().__init__(deck)

    def draw_card(self):
        self._stored_cards.append(self.deck.get_card())


if __name__ == '__main__':

    deck = Deck()
    player = Human(deck)
    krupier = Croupier(deck)
    draw_next = 't'
    while draw_next == 't':
        player.play()
        print(f'Masz {player.get_cards_value()} , {player._stored_cards}')
        draw_next = input('dobrać kartę (t/n)? ')
    
    while int(krupier) < int(player):
        krupier.play()
    print(f'krupier ma {krupier.get_cards_value()} , {krupier._stored_cards}')