try:import random;from colorama import Fore;from requests import post,get
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()
def saver(user):
    ID=''#Telegram id
    token=''#Telegram bot token
    try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=• New username’s Claimed @{user} 🦦\n\nBy\t@TweakPY\t-\t@vv1ck')
    except:pass
    with open('Available.txt', 'a') as x:
        x.write(user+'\n')
def with_list():
	error,count,done=0,0,0
	try:file=open('user.txt', 'r')
	except FileNotFoundError:exit('[!] No users File Detected - Note users file must be in user.txt File ..')
	while True:
		user=file.readline().split('\n')[0]
		ru=get(f"https://xboxgamertag.com/search/{user}",headers={'Host': 'xboxgamertag.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Cache-Control': 'max-age=0','Te': 'trailers'}).text
		if f"<h1>Gamertag doesn't exist</h1>" in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			done+=1
			count+=1
			saver(user)
		elif f'<title>{user} - Xbox Gamertag</title>' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			error+=1
			count+=1
		else:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			error+=1
			count+=1
def without_list():
	count,done,error=0,0,0
	user=""
	lena=input('[?] Length: ');length=(int(lena))
	chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
	while True:
		for user in range(1):
			user=""
			for item in range(length):
				user+=random.choice(chars)
		ru=get(f"https://xboxgamertag.com/search/{user}",headers={'Host': 'xboxgamertag.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Cache-Control': 'max-age=0','Te': 'trailers'}).text
		if f"<h1>Gamertag doesn't exist</h1>" in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			done+=1
			count+=1
			saver(user)
		elif f'<title>{user} - Xbox Gamertag</title>' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			error+=1
			count+=1
		else:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			error+=1
			count+=1
print("""
██╗  ██╗██████╗  ██████╗ ██╗  ██╗      ██████╗██╗  ██╗
╚██╗██╔╝██╔══██╗██╔═══██╗╚██╗██╔╝     ██╔════╝██║  ██║
 ╚███╔╝ ██████╔╝██║   ██║ ╚███╔╝█████╗██║     ███████║
 ██╔██╗ ██╔══██╗██║   ██║ ██╔██╗╚════╝██║     ██╔══██║
██╔╝ ██╗██████╔╝╚██████╔╝██╔╝ ██╗     ╚██████╗██║  ██║
╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝      ╚═════╝╚═╝  ╚═╝
                                              
        By @TweakPY - @vv1ck                          
""")
LW=int(input("[1] without List\n[2] with List\n---------------\nEnter > : "))
if LW==1:without_list()
elif LW==2:with_list()
else:exit('\n[!] Exit... \n\nBy @TweakPY - @vv1ck')
