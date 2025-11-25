from translations import Translations

tr = Translations()

def set_locale(locale: str):
	tr.set_locale(locale)

class Role:
	def from_str(self, txt: str):
		self.role = txt
	
	def __str__(self) -> str:
		return tr.roles

class Player:
	def __init__(self, role: Role) -> None: