import json


class Translations:
	def __init__(self, locale: str = 'en', translations: dict = None):
		self.locale = locale
		with open('./translations.json', 'r') as f:
			txt = f.read()
		try:
			self.translations_root = json.loads(txt)
		except json.decoder.JSONDecodeError as e:
			print(f'Invalid JSON translation data ({e})')
			exit(1)
		except FileNotFoundError as e:
			print(f'Translations file not found ({e}) Are you in the correct CWD?')

		if translations:
			self.translations = translations
		else:
			try:
				self.translations = self.translations_root[self.locale]
			except KeyError as e:
				print(f'Locale not found ({e}) Did you type it correctly and does it have support?')
				del self

	def set_locale(self, locale: str):
		try:
			self.translations = self.translations_root[locale]
		except KeyError as e:
			print(f'Locale not found ({e}) Did you type it correctly and does it have support?')

	def __getattr__(self, item):
		value = self.translations[item]
		if type(value) == str:
			return value
		else:
			return Translations(locale = self.locale, translations = value)
