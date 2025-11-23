class Translations:
	"""
	Includes all text translations in different locales categorized in subclasses.
	
	Set locale using Translations.set_locale().
	"""
	locale = None

	class Roles:
		"""
		Contains translations for the specific roles. Only set after calling Translations.set_locale()
		"""
		villager = None
		werewolf = None
		wild_child = None
		wolf_cub = None
		white_werewolf = None
		vampire = None
		cursed = None
		tanner = None
		freemason = None
		drunkard = None
		seer = None
		oracle = None
		apprentice_seer = None
		aurum_seer = None
		witch = None
		healer = None
		cupid = None
		hunter = None
		jaguar = None
		priest = None
		bodyguard = None
		knight_with_rusty_sword = None
		devoted_servant = None
		old_hag = None
		conjurer = None
		goethe = None
		milkman = None

	class Misc:
		"""
		Miscellaneous texts, mostly only set after calling Translations.set_locale()
		"""
		language_inp = None
		inp_wrong_type = None
		inp_empty = None
		inp_not_allowed = None
	
	class Technical:
		"""
		Technical texts, e.g. bugs in the code. Mostly displayed in English only
		"""
		inp_type_takes_no_arguments = f'Error: The given typ does not take arguments. Ignoring typ argument typ.'

	@classmethod
	def set_locale(cls, locale: str):
		"""
		Set the locale of all translations.
		
		:param locale: One of 'de', 'en'
		:return: None
		"""
		cls.locale = locale
		if cls.locale == 'en':
			cls.Roles.villager = 'Villager'
			cls.Roles.werewolf = 'Werewolf'
			cls.Roles.wild_child = 'Wild Child'
			cls.Roles.wolf_cub = 'Wolf Cub'
			cls.Roles.white_werewolf = 'White Werewolf'
			cls.Roles.vampire = 'Vampire'
			cls.Roles.cursed = 'Cursed One'
			cls.Roles.tanner = 'Tanner'
			cls.Roles.freemason = 'Freemason'
			cls.Roles.drunkard = 'Drunkard'
			cls.Roles.seer = 'Seer'
			cls.Roles.oracle = 'Oracle'
			cls.Roles.apprentice_seer = 'Apprentice Seer'
			cls.Roles.aurum_seer = 'Aurum Seer'
			cls.Roles.witch = 'Witch'
			cls.Roles.healer = 'Healer'
			cls.Roles.cupid = 'Cupid'
			cls.Roles.hunter = 'Hunter'
			cls.Roles.jaguar = 'Jaguar'
			cls.Roles.priest = 'Priest'
			cls.Roles.bodyguard = 'Bodyguard'
			cls.Roles.knight_with_rusty_sword = 'The Knight with the Rusty Sword'
			cls.Roles.devoted_servant = 'Maid'
			cls.Roles.old_hag = 'Old Hag'
			cls.Roles.conjurer = 'Conjurer'
			cls.Roles.goethe = 'Goethe'
			cls.Roles.milkman = 'Milkman'
			cls.Misc.language_inp = 'Language:'
			cls.Misc.wrong_type = 'Wrong type. Please enter a value of the following type:'
			cls.Misc.inp_empty = 'Please enter a value.'
			cls.Misc.inp_not_allowed = 'Value is not allowed, please enter any of:'
		elif cls.locale == 'de':
			cls.Roles.villager = 'Dorfbewohner'
			cls.Roles.werewolf = 'Werwolf'
			cls.Roles.wild_child = 'Wildes Kind'
			cls.Roles.wolf_cub = 'Wolfsjunges'
			cls.Roles.white_werewolf = 'Weißer Werwolf'
			cls.Roles.vampire = 'Vampir'
			cls.Roles.cursed = 'Verfluchter'
			cls.Roles.tanner = 'Gerber'
			cls.Roles.freemason = 'Freimaurer'
			cls.Roles.drunkard = 'Trunkenbold'
			cls.Roles.seer = 'Seherin'
			cls.Roles.oracle = 'Seher'
			cls.Roles.apprentice_seer = 'Seherlehrling'
			cls.Roles.aurum_seer = 'Auraseherin'
			cls.Roles.witch = 'Hexe'
			cls.Roles.healer = 'Magier'
			cls.Roles.cupid = 'Amor'
			cls.Roles.hunter = 'Jäger'
			cls.Roles.jaguar = 'Jaguar'
			cls.Roles.priest = 'Priester'
			cls.Roles.bodyguard = 'Leibwächter'
			cls.Roles.knight_with_rusty_sword = 'Der Ritter mit der rostigen Klinge'
			cls.Roles.devoted_servant = 'Magd'
			cls.Roles.old_hag = 'Alte Vettel'
			cls.Roles.conjurer = 'Beschwörerin'
			cls.Roles.goethe = 'Goethe'
			cls.Roles.milkman = 'Milchmann'
			cls.Misc.language_inp = 'Sprache:'
			cls.Misc.wrong_type = 'Falscher Typ. Bitte gebe ein Wert mit dem folgenden Typ ein:'
			cls.Misc.inp_empty = 'Bitte mache eine Eingabe.'
			cls.Misc.inp_not_allowed = 'Wert ist nicht erlaubt, bitte gebe einen der folgenden ein:'
