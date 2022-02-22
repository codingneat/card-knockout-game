import numpy as np
from card_knockout_game.result import Result
from card_knockout_game.deck import Deck


class CardKnockoutGame:
  deck = None
  player_1 = None
  player_2 = None
  cards_player_1 = []
  cards_player_2 = []
  result = ''
  score = None

  def __init__(self, player_1, player_2, number_cards=52):
    self.deck = Deck(number_cards)
    self.number_cards = number_cards
    self.player_1 = player_1
    self.player_2 = player_2
    cards = self._deal_cards()
    self.cards_player_1 = cards[0]
    self.cards_player_2 = cards[1]
    self.result = self._resolve_game()

  def check_result(self):
    return f'{self.result} won!' if self.result != 'DRAW' else 'We have a draw'

  def _resolve_game(self):
    players_cards = zip(self.cards_player_1, self.cards_player_2)
    game = [self._compare_cards(card_player_1, card_player_2) for (card_player_1, card_player_2) in players_cards]
    return self._get_game_winner(game)

  def _deal_cards(self):
    half_deck = int(self.number_cards / 2)
    return (self.deck.cards[:half_deck], self.deck.cards[half_deck:])

  def _compare_cards(self, card_player_1, card_player_2):
    result = card_player_1 - card_player_2
    if result == 0:
        return 'Draw'
    return self.player_1.name if result > 0 else self.player_2.name

  def _get_game_winner(self, game):
    (unique, counts) = np.unique(game, return_counts=True)
    results = dict(zip(unique, counts))

    self.score = results

    if self.player_1.name in results and (not self.player_2.name in results or results[self.player_1.name]  > results[self.player_2.name]):
      self.player_1.play_game(Result.WON)
      self.player_2.play_game(Result.LOST)
      return self.player_1.name
    elif self.player_2.name in results and (not self.player_1.name in results or results[self.player_2.name]  > results[self.player_1.name]):
      self.player_1.play_game(Result.LOST)
      self.player_2.play_game(Result.WON)
      return self.player_2.name
    else:
      self.player_1.play_game(Result.DRAWN)
      self.player_2.play_game(Result.DRAWN)
      return 'DRAW'
