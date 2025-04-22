import os
from netmiko import ConnectHandler
from  cfg_script import *

os.system("cls")

device = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.56.160',
    'username' : 'cisco',
    'password' : 'cisco',
    'secret' : 'cisco',
    # Multiple all of the delays by a factor of two
    "global_delay_factor": 1
    }

print ('BEFORE START, PLEASE CHECK AND FILL BOTH sh_commands.txt AND/OR conf_commands.txt')
print ('')
os.system("pause")
os.system("cls")

try:
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    sh_name = net_connect.send_command('sh running-config | include hostname')
    #device_ip = {device['ip']}
    print (f'Connection established with device {sh_name}\n')
except:
    print (f"Connection to {device['ip']} not possible. Please check and try again")
    net_connect.disconnect()

# SELECT OPTIONS
template = ''
temp_check = True

while temp_check == True:
    print('1 - SHOW COMMANDS ONLY\n'
          '2 - SEND CONFIG COMMANDS')
    template = input('\nCHOOSE TEMPLATE NUMBER: ')

    if template == '' or template >= '3' or template <= '0':
        print('\n[ERROR]: PLEASE CHOOSE 1 or 2 ONLY!')
    
    elif template == '1':
        temp_check = False
        sh_comms(net_connect)
        break
    
    elif template == '2':
        temp_check = False
        conf_comms(net_connect)
        break


os.system("pause")