from card_knockout_game.result import Result


class Player:
  name = ''
  games_won = 0
  games_lost = 0
  games_played = 0

  def __init__(self, name):
    self.name = name

  def play_game(self, result):
    self.games_played += 1
    if result == Result.WON:
      self.games_won += 1
    elif result == Result.LOST:
      self.games_lost += 1
