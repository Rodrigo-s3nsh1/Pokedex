import PySimpleGUI as sg
import requests
import base64


def infos(name, poke, window):
	img = poke['sprites']['front_default']
	img = base64.b64encode(requests.get(img).content)
	type = poke['types'][0]['type']['name']
	
	window['pokemon_image'].Update(data=img)
	window['pokemon_name'].Update(f'Name: {name.capitalize()}')
	window['pokemon_type'].Update(f'   Type: {type.capitalize()}')
	window['OUT'].Update('')
	
	num_ab = 1
	window['OUT'].print('\t -Abilities- ', font=('Monopace', 14, 'bold', 'normal'), text_color='red')
	for ab in poke['abilities']:
		window['OUT'].print(f"Ability-{num_ab}: {ab['ability']['name']}")
		num_ab += 1

def pokemon(name, window):
	api = f"https://pokeapi.co/api/v2/pokemon/{name}"
	poke = requests.get(api)
	try:
		poke = poke.json()
	except:
		sg.popup_ok('Pokemon not found!', title='ERROR', background_color='#B22222', button_color='#B22222') 
	else:
		infos(name, poke, window)

# =========== Interface ==========

sg.change_look_and_feel('SystemDefault')

def main():
	layout = [
			[sg.Input(size=(22, 2), key='name'), sg.Button('Search', size=(4,1), key='pesquisar', font=('Arial', 10, 'normal', 'bold'), button_color='#B22222')],
			[sg.Image(key='pokemon_image', background_color='#B22222'), sg.Text(text_color="white", font=("Monospace", 10, "bold", "bold"), background_color='#B22222', key='pokemon_name'),sg.Text(text_color="white", font=("Monospace", 10, "bold", "bold"), background_color='#B22222', key='pokemon_type')],
			[sg.Multiline(size=(50, 7), key='OUT')]
		]
		
	global window
	window = sg.Window('Pokédex', layout=layout, element_justification='c', size=(800, 600), background_color='#B22222', margins=(0, 0))
	return window

main()

while True:
	event, values = window.read(timeout=1)
	if event == sg.WIN_CLOSED:
		break
	if event == 'pesquisar':
		if values['name'] in ['', ' ', None]:
			sg.popup_ok('Pokemon not found!', title='ERROR', background_color='#B22222', button_color='#B22222') 
		else:
			pokemon(values['name'].lower(), window)

window.close()	