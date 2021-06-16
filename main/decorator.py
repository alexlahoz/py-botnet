# Decorator for terminal
class Decorator():
  def decorate(self, color, text):
    COLORS = {
      'grey':f'\033[30m{text}\033[0m',
      'red':f'\033[31m{text}\033[0m',
      'green':f'\033[32m{text}\033[0m',
      'brown':f'\033[33m{text}\033[0m',
      'blue':f'\033[34m{text}\033[0m',
      'purple':f'\033[35m{text}\033[0m',
      'cyan':f'\033[36m{text}\033[0m'
    }

    return COLORS[color]
