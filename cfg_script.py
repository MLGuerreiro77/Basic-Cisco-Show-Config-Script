# FUNCTION FOR SHOW COMMANDS ONLY
def sh_comms(net_connect):
    with open("sh_commands.txt", encoding = 'utf-8' ) as file:
        file = file.readlines()
        for comms in file:
            output = net_connect.send_multiline (file)
            #print('\n\r')       
            print (output)
            #print('\n\r')       


# FUNCTION FOR SENDING CONFIG COMMANDS
def conf_comms(net_connect):
    cfg_file = 'conf_commands.txt'
    output = net_connect.send_config_from_file(cfg_file)
    print (output)



'''
if __name__ == '__main__':
    sh_comms()
    conf_comms()

'''