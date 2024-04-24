import json
print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
a = 3
sum=0
with open('json_sample.json', 'r',encoding='utf-8') as file:
        g = json.load(file)
        for gg in g['imdata']:
                if sum==a:
                 break
                print(gg["l1PhysIf"]['attributes']['dn'], '                             ', gg["l1PhysIf"]['attributes']['fecMode'], '', gg["l1PhysIf"]['attributes']['mtu'])
                sum+=1 