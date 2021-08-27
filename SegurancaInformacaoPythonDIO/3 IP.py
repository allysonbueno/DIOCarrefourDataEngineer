import ipaddress

# ip = '172.20.5.229'
ip = '172.20.5.229/24'

# endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ip, strict=False)

# print(endereco)
# print(endereco + 100)
print(rede)

for ip in rede:
    print(ip)