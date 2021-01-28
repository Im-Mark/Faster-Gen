#By Fa$ter Ju$t Mark#3038

from colorama import Fore, Back, Style
import random, string

print(Fore.GREEN + Style.DIM + """╭━━━╮╱╱╱╱╭━━━╮╱╭╮╱╱╱╱╱╱╱╱   ╭━━━╮╱╱╱╱╱╱╱╱        
┃╭━━╯╱╱╱╱┃╭━╮┃╭╯╰╮╱╱╱╱╱╱╱   ┃╭━╮┃╱╱╱╱╱╱╱╱        
┃╰━━╮╭━━╮┃╰━━╮╰╮╭╯╭━━╮╭━╮   ┃┃╱╰╯╭━━╮╭━━╮        
┃╭━━╯┃╭╮┃╰━━╮┃╱┃┃╱┃┃━┫┃╭╯   ┃┃╭━╮┃┃━┫┃╭╮┃        
┃┃╱╱╱┃╭╮┃┃╰━╯┃╱┃╰╮┃┃━┫┃┃╱   ┃╰┻━┃┃┃━┫┃┃┃┃        
╰╯╱╱╱╰╯╰╯╰━━━╯╱╰━╯╰━━╯╰╯╱   ╰━━━╯╰━━╯╰╯╰╯        
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱        
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱        

┏┓░┏┳┓  ░┏┓░░░┏━┓┏┓░  ┏━┳━┓░░░░░░░┏┓░        
┃┗┓┃┃┃  ░┃┃┏┳┓┃━┫┃┗┓  ┃┃┃┃┃┏━┓░┏┳┓┃┣┓        
┃╋┃┣┓┃  ┏┫┃┃┃┃┣━┃┃┏┫  ┃┃┃┃┃┃╋┗┓┃┏┛┃━┫        
┗━┛┗━┛  ┗━┛┗━┛┗━┛┗━┛  ┗┻━┻┛┗━━┛┗┛░┗┻┛        
""")

amount = int(input(Fore.CYAN + Style.BRIGHT + 'Cantidad de Codes Nitro Unchecked a generar:' + Fore.MAGENTA))
value = 1

while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('codes_nitro_unchecked.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'{code}')
    value += 1