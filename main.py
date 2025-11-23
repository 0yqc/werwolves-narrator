from locale import Translations as Tr
import utils

Tr.set_locale(utils.inp(f'{Tr.Misc.language_inp} ', allowed = ('de', 'en')))
print(Tr.Roles.villager)