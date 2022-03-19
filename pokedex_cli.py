import requests
from time import sleep
from os import system as syst


def infos(poke):
    name = poke['name']
    type = poke['types'][0]['type']['name']
	
    ab_num = 1
	
	print('\n\033[91m╭─━━━━━━━━━━━━━━━━━━━━━━━━─╮\033[m')
	print(f'  \033[32mName:\033[m {name.capitalize()}\t\033[32mType:\033[m {type}')
	print('\n\t- Abilities -')
	for hab in poke['abilities']:
		print(f"  \033[32mAbilitie-{ab_num}:\033[m {hab['ability']['name']}")
		ab_num += 1
		
	print('╰─━━━━━━━━━━━━━━━━━━━━━━━━─╯\n')
	

def main():
	print('\t\033[1;33mPokédex\033[m\n')
	
	while True:
		try:
			pokemon = str(input('[*] Pokemon: ')).lower().strip()
		except (KeyboardInterrupt):
			break
		except:
			print('[ERROR] \033[31mPor favor informe uma informção válida!\033[m')
		else:
			if pokemon in ['', None, ' ']:
				print('[ERROR] \033[31mInforme algum nome!\033[m')
				
			else:
				api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
				res = requests.get(api)
				try:
					poke = res.json()
				except:
					print('[ERROR] \033[0;31mPor favor informe um nome válido!\033[m')
				else:
					sleep(0.6)
					syst('clear')
					infos(poke)
					
	print('\033[32m[*] Saindo...\033[m')
	
	
if __name__ == '__main__':
	main()
