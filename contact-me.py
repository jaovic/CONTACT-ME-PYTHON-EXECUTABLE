import webbrowser as wb
import random as rd

print('-------------------------')
print('      MEUS CONTATOS:    |')
print('-------------------------')

def randomica():
	ran = rd.randint(1, 5) 
	if ran == 1:
		wb.open('https://www.linkedin.com/in/jo%C3%A3o-victor-martins-22100a164/')
	elif ran == 2:
		wb.open('https://api.whatsapp.com/send/?phone=5531997042924&text&app_absent=0')
	elif ran == 3:
		wb.open('mailto:jvmsf05@gmail.com')
	elif ran == 4:
		wb.open('https://www.instagram.com/joaoviiictoor/')
	elif ran == 5:
		wb.open('https://steamcommunity.com/profiles/76561198070976393/')
	elif ran == 5:
		wb.open('https://www.twitch.tv/xaovic')
		
def main():
	while True:	
		print('LINKEDIN[1], WHATSAPP[2], GMAIL[3], INSTAGRAM[4], STEAM[5], TWITCH[6], RMADOM[7], EXIT[8].')
		x = int(input('>>>'))
		if x == 1:
			wb.open('https://www.linkedin.com/in/jo%C3%A3o-victor-martins-22100a164/')
		elif x == 2:
			wb.open('https://api.whatsapp.com/send/?phone=5531997042924&text&app_absent=0')
		elif x == 3:
			wb.open('mailto:jvmsf05@gmail.com')
		elif x == 4:
			wb.open('https://www.instagram.com/joaoviiictoor/')
		elif x == 5:
			wb.open('https://steamcommunity.com/profiles/76561198070976393/')
		elif x == 6:
			wb.open('https://www.twitch.tv/xaovic')
		elif x == 7:
			randomica()
		elif x == 8:
			input('Aperte enter para sair.')
			break
		else:
			print('Opção não aceita, por favor digite uma opção válida.')
		print()		
main()