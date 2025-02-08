
#!/usr/bin/python
# 1. Install openvpn
# 2. Download and extract all vpn config files (.ovpn files, .key and .crt) inside the /etc/openvpn/ folder
# 3. Create a new .pia file inside the /root/ directory that stores the username and password for the vpn
# 4. Run this script in crontab under root user. (Ie, use sudo crontab -e)

import os
import random

# openvpn_config_dir = '/root/.pia'
# current_config = os.path.realpath(openvpn_config_dir)
# print(current_config)
# f = open(openvpn_config_dir,'r+')
# d=f.read()
# print(d)

openvpn_config_dir = '/etc/openvpn/'
configs = os.listdir(openvpn_config_dir)
configs.remove('update-resolv-conf')
current_config = os.path.realpath(openvpn_config_dir+"server.conf")
primary_config = random.choice(configs)
while primary_config in current_config:
        primary_config = random.choice(configs)
os.system('rm '+openvpn_config_dir+'server.conf')
command ='ln -s '+openvpn_config_dir+primary_config+' '+openvpn_config_dir+'server.conf'
os.system(command)
f = open(openvpn_config_dir+'server.conf','r+')
contents = f.read()

if '/root/.pia' not in contents:
        contents =contents.replace('auth-user-pass','auth-user-pass /root/.pia')
        print(contents)
f.seek(0)
c=f.write(contents)
print(c)
f.truncate()
f.close()
os.system('service openvpn restart')
print('Done!')