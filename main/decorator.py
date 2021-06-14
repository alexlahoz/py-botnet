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

class SetColor():
  def __init__(self):
    self.text = ""
    self.grey = f'\033[30m {self.text} \033[0m'

  def set_grey(self, text):
    # return f'\033[30m {text} \033[0m'
    self.text = text
    return self.grey

grey = SetColor()

print(grey.set_grey("hi!"))
