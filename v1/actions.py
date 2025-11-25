import time, sys
import utils
import data as gdata


def character_action(character: str, data: dict) -> dict:
	dg_action = None
	# ap: short for affected person
	for i in range(2):
		dg_second_action = None
		if character == 'doppelgängerin':
			ap = utils.intinp('Wähle deine gedoppelte Person: ')
			data['doubled_person'] = ap - 1
			data['doubled_role'] = data['roles'][ap - 1]
		elif character in ('amor', 'jaguar'):
			dg_second_action = True
			v1 = utils.intinp('1. Verliebter: ')
			v2 = utils.intinp('2. Verliebter: ')
			data['love'].append((v1, v2))
		elif character == 'wolfskind':
			dg_second_action = True
			print('Wähle dein Idol.')
			input()
		elif character == 'trunkenbold':
			dg_second_action = True
			ap = utils.intinp('Wähle deinen heutigen Nächtigungsort: ')
			if dg_action:
				data['round_protected'].append(data['roles'].index('doppelgängerin'))
				data['round_trunkenbold_doubled'] = ap - 1
			else:
				data['round_protected'].append(data['roles'].index('trunkenbold'))
				data['round_trunkenbold'] = ap - 1
		elif character == 'freimaurer':
			input('Fertig: ')
		elif character == 'kultführer':
			dg_second_action = True
			data['cult'].append(utils.intinp('Füge eine Person zum Kult hinzu: ') - 1)
		elif character in ('priester', 'leibwächter'):
			dg_second_action = True
			data['round_protected'].append(utils.intinp('geschützte Person: ') - 1)
		elif character in ('seherin', 'seher'):
			dg_second_action = True
			ap = utils.intinp('zu erkenennde Person: ')
			print(data['roles'][ap - 1].title())
			time.sleep(1)
		elif character == 'aura-seherin':
			dg_second_action = True
			ap = utils.intinp('zu erkenennde Person: ')
			print('Gut' if data['roles'][ap - 1] in gdata.characters_village else 'Böse')
			time.sleep(1)
		elif character == 'werwolf':
			if data['round_verfluchter_werwolve']:
				print('Der Verfluchte wacht mit auf.')
			ap = utils.intinp('Opfer: ')
			data['round_deaths'].append(ap - 1)
			data['round_werwolve_deaths'].append(ap - 1)
			if data['round_2_werwolve_deaths']:
				ap = utils.intinp('2. Opfer: ')
				data['round_deaths'].append(ap - 1)
				data['round_werwolve_deaths'].append(ap - 1)
		elif character in ('hexe', 'magier'):
			dg_second_action = True
			print(f'Opfer: {', '.join(f'{i+1}. {data['roles'][ap].title()} ({ap + 1})' for i, ap in enumerate(data['round_werwolve_deaths']))}; ')
			if utils.boolinp('Möchtest du das Opfer heilen? '):
				data['witch_potions']['heal'] = False
				if len(data['round_werwolve_deaths']) != 1:
					ap = utils.intinp('Welches Opfer? ') - 1
				else:
					ap = 0
				data['round_deaths'].remove(data['round_werwolve_deaths'][ap])
				data['round_werwolve_deaths'].pop(ap)
			ap = utils.intinp('Opfer: ')
			if ap:
				data['witch_potions']['death'] = False
				data['round_deaths'].append(ap - 1)
		elif character == 'vampir':
			if data['round_verfluchter_vampire']:
				print('Der Verfluchte wacht mit auf.')
			ap = utils.intinp('Opfer: ')
			data['round_vampire_deaths'].append(ap - 1)
		elif character == 'alte vettel':
			dg_second_action = True
			ap = utils.intinp('verfluchte Person: ')
			data['round_altevettel'].append(ap - 1)
		elif character == 'bechwörerin':
			dg_second_action = True
			ap = utils.intinp('beschwörte Person: ')
			data['round_beschwörerin'].append(ap - 1)
		elif character == 'goethe':
			dg_second_action = True
			ap = utils.intinp('vergoethete Person: ')
			data['round_goethe'].append(ap - 1)
		elif character == 'milchmann':
			dg_second_action = True
			ap = utils.intinp('Person: ')
			typ = utils.milkinp('Typ: ')
			data['round_milch'].update({ap - 1: typ})
		elif character == 'weißer werwolf':
			dg_second_action = True
			ap = utils.intinp('Opfer: ')
			if ap:
				data['round_deaths'].append(ap - 1)

		if 'doppelgängerin' in data['roles'] and character == data['doubled_role'] and dg_second_action and i == 0:
			print()
			print('Doppelgängerin-Aktion:')
			dg_action = True
		else:
			break
	return data

def after_night(data: dict) -> dict:
	result = {
		'deaths': []
	}
	for death in data['round_deaths']:
		result['deaths'].append(death)
		for lovers in data['love']:
			if death in lovers:
				result['deaths'].append(lovers[0 if lovers.index(death) else 1])
		if death == data['doubled_person']:
			result['deaths'].append(data['roles'].index('doppelgängerin'))
		elif death == data['roles'].index('jäger'):
			result['deaths'].append(utils.intinp('Jägerschuss: '))
		elif death == data['roles'].index('jaguar'):
			result['deaths'].append(utils.intinp('Jaguarschuss: '))
	for death in result['deaths']:
		if death in data['round_protected']:
			result['deaths'].remove(death)
	for key in data:
		if key.startswith('round_') and not key == 'round_vampire_deaths':
			if type(data[key]) == bool:
				data[key] = False
			elif type(data[key]) == list:
				data[key] = []
			else:
				data[key] = None
	data['alive'].remove(*result['deaths'])
	if set(data['alive']).issubset(set(data['cult'])):
		print('Der Kultführer hat das Spiel alleinig gewonnen.')
		sys.exit()
	tmp = tuple(data['alive_roles'])
	for role in tmp:
		if not role in [data['roles'][i] for i in data['alive']]:
			data['alive_roles'].remove(role)
	for death in result['deaths']:
		if death == data['roles'].index('wolfsjunges'):
			data['round_2_werwolve_deaths'] = True
		elif death == data['roles'].index('verfluchter'):
			if death in data['werwolve_deaths']:
				data['round_verfluchter_werwolve'] = True
				result['deaths'].remove(death)
			elif death in data['vampire_deaths']:
				data['round_verfluchter_vampire'] = True
				result['deaths'].remove(death)
	
	return data