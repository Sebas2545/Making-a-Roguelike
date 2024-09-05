from __future__ import annotations
from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from exceptions import Impossible

if TYPE_CHECKING:
    from entity import Actor

#holds which letters are unlocked and which word is currently equipped
class Letters(BaseComponent):
    parent: Actor

    def __init__(self) -> None:
        self.letters_unlocked = {x: False for x in 'abcdefghijklmnopqrstuvwxyz'} # creates a dict with keys of every letter in the alphabet, and values of False
        self.letters_unlocked['a'] = True # two letters unlocked from character creation
        self.letters_unlocked['i'] = True

        self._word_equipped = 'a' # default word equipped
        self.word_length = 1

    @property
    def max_word_length(self) -> int:
        return self.word_length
    
    @property
    def word_equipped(self) -> str:
        return self.word_equipped
    
    @word_equipped.setter
    def change_word(self, new_word: str) -> None:
        if len(new_word) > self.max_word_length():
            raise Impossible("This word is too long")
        else:
            self._word_equipped = new_word

   
        