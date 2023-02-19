import os
import getpass
while True:
  login = input('login: ')
  if login == 'list':
    print('''╔═══════╦══════════╦═════════════════════════╦═════════════════╗
║ Login ║ Password ║ Desc                    ║ Devs use?       ║
╠═══════╬══════════╬═════════════════════════╬═════════════════╣
║ user  ║ 123      ║ A normal user for new   ║ yes             ║
╠═══════╬══════════╬═════════════════════════╬═════════════════╣
║ root  ║ toor     ║ Root mode. (no su)      ║ yes (sometimes) ║
╠═══════╬══════════╬═════════════════════════╬═════════════════╣
║ 123   ║ 123      ║ a basic user            ║ no              ║
╠═══════╬══════════╬═════════════════════════╬═════════════════╣
║ abcd  ║ efgh     ║ a basic user            ║ no              ║
╠═══════╬══════════╬═════════════════════════╬═════════════════╣
║ login ║ password ║ for these who dont know ║ no              ║
╚═══════╩══════════╩═════════════════════════╩═════════════════╝''')
  else:
    password = getpass.getpass()
  
  if login == 'root' and password == 'toor':
    os.system('clear')
    os.system('bash ../successlogin.sh')
  elif login == 'user' and password == '1234':
    os.system('clear')
    os.system('bash ../successlogin.sh')
  elif login == '123' and password == '123':
    os.system('clear')
    os.system('bash ../successlogin.sh')
  elif login == 'abcd' and password == 'efgh':
    os.system('clear')
    os.system('bash ../successlogin.sh')
  elif login == 'login' and password == 'password':
    os.system('clear')
    os.system('bash ../successlogin.sh')
  else:
    print("login failure\nDont know any password and login?\ntype 'list' in login input\nor read our README.md in github")