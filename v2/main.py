import translations, data, nightcycle, utils
from translations import Translations
from data import Player, Role

tr = Translations()
locale = utils.inp(f'{tr.misc.language_inp} ', allowed = ('de', 'en'))
tr.set_locale(locale)
data.set_locale(locale)

player_list = ()


while True:
	nightcycle.night()