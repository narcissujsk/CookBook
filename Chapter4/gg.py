from netmiko import Netmiko
from getpass import getpass

net_connect = Netmiko(host='10.110.25.250', username='qiqianqian',
                      password="qiqianqian", device_type='huawei')

print(net_connect.find_prompt())
commands=[' interface GigabitEthernet1/0/27',
          'port link-type access',
          'port access vlan 103',
         ]
print("######################################")
#output = net_connect.send_config_set(commands, exit_config_mode=False)
output = net_connect.send_config_set(commands)
output += net_connect.exit_config_mode(exit_config='return', pattern='>')
print(output)
print("######################################")
#net_connect.read_until_pattern(pattern='<')
net_connect.disconnect()