import os
os.system('clear')

COLORS = {
  'grey':'\033[30m[GREY]\033[0m',
  'red':'\033[31m[RED]\033[0m',
  'green':'\033[32m[GREEN]\033[0m',
  'brown':'\033[33m[BROWN]\033[0m',
  'blue':'\033[34m[BLUE]\033[0m',
  'purple':'\033[35m[PURPLE]\033[0m',
  'cyan':'\033[36m[CYAN]\033[0m'
}

class Decorator():
  def decorate(self, color, text):
    colors = {
      'grey':'\033[30m{text}\033[0m',
      'red':'\033[31m{text}\033[0m',
      'green':'\033[32m{text}\033[0m',
      'brown':'\033[33m{text}\033[0m',
      'blue':'\033[34m{text}\033[0m',
      'purple':'\033[35m{text}\033[0m',
      'cyan':'\033[36m{text}\033[0m'
    }
    return colors[color]


a = Decorator()
print(a.decorate('grey', 'hola'))
