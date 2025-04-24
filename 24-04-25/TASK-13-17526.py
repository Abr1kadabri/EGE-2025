from ipaddress import ip_network

net = ip_network('172.16.128.0/255.255.192.0')


print(net.network_address)
print(net.broadcast_address)
print(net.netmask)
print(net.num_addresses)
print(net.hosts)

print(16384/2)