import json
with open('ccNasabah.json', 'r') as x:
    out = json.load(x)
listKey = []
listValue = []
for i in out:
    key = list(i)
    value = list(i.values())
    listKey.append(key)
    listValue.append(value)
    keynya = listValue[1]
    valuenya = listValue[1]
    if valuenya[0] == '4':
        print('yes')
    '''for i in listValue:
        keynya = i[1]
        valuenya = i[1]
        if valuenya[0] == '4':'''