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

    def __repr__(self) -> str:
        return f'{self.figure}_{self.color}'

class Deck:
    """_summary_
    """
    def __init__(self) -> None:
        self._card_deck = []
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

if __name__ == '__main__':

    deck = Deck()
    deck.shuffle_cards()
    print(deck.get_deck())
