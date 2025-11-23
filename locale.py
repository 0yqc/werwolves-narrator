class Roles:
	@classmethod
	def set_locale(cls, locale: str):
		cls.locale = locale
		if cls.locale == 'de':
			villager = 'Dorfbewohner'
			werewolf = 'Werwolf'
			wild_child = 'Wildes Kind'
			wolf_cub = 'Wolfsjunges'
			white_werewolf = 'Weißer Werwolf'
			vampire = 'Vampir'
			cursed = 'Verfluchter'
			tanner = 'Gerber'
			freemason = 'Freimaurer'
			drunkard = 'Trunkenbold'
			seer = 'Seherin'
			oracle = 'Seher'
			apprentice_seer = 'Seherlehrling'
			aurum_seer = 'Auraseherin'
			witch = 'Hexe'
			healer = 'Magier'
			cupid = 'Amor'
			hunter = 'Jäger'
			jaguar = 'Jaguar'
			priest = 'Priester'
			bodyguard = 'Leibwächter'
			knight_with_rusty_sword = 'Der Ritter mit der rostigen Klinge'
			devoted_servant = 'Magd'
			