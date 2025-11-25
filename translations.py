import json

with open('./translations.json', 'r') as f:
	raw = f.read().strip()

translations_master = json.loads(raw)
translations = translations_master['en']

def set_locale(locale: str):
	nonlocal translations = translations_master[locale]