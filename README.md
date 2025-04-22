# Show and Configs for Cisco devices

### ⚠️**DISCLAIMER**⚠️
I´d like to inform that this script was created for studying purposes only! Please take care befor use this on your **production environment!**
My intention is to learn and improve my Python and Cisco automation skills. I used this script with EVE-NG Cisco devices.

I choose to use the Netmiko Python´s library once I´ve found it very useful for the type of scripts I need. The script is very simple to use and also is not complex in terms of coding since I´m not a programming guy.

### **INSTRUCTIONS**
On top of the script, you´ll find a dictionary with the IP and device´s credentials. Just change it for your own.
To run the script, basically, you´ll find the main file called *"basic_cisco.py"*. Once this file is running it will present a simple menu for you to choose to show commands only or to send commands to a device. There are two files where you will fill with your show commands and another one with the commands you want to send. The files are:

1. *sh_commands.txt*
2. *conf_commands.txt*

Once you choose your option, the script will run the corresponding function on file *"cfg_script.py"*... and voilá! The information you filled on steps before will be printed on screen. 


Thank´s for visiting my page!
🙂