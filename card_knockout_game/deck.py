import numpy as np


class Deck:
  cards = []

  def __init__(self, number_cards = 52):
    identic_cards = np.arange(1, int(number_cards / 4) + 1)
    self.cards = np.concatenate((identic_cards, identic_cards, identic_cards, identic_cards))
    self.shuffle_cards()

  def shuffle_cards(self):
    np.random.shuffle(self.cards)
