mydict = {}
with open("input.txt") as f:
    for line in f:
        (key, val) = line.strip().split(None, 1)
        mydict[key] = val
print(mydict)

def decrypt(cipher,key):
    result = ""
    for i in range(len(cipher)):
        char = cipher[i]
        if (char.isupper()):
            result += chr((ord(char) - key - 65) % 26 + 65)
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    return result

print(decrypt('ROZO',3))

emblem = {
    'SPACE' : 'GORILLA',
    'LAND' : 'PANDA',
    'AIR' : 'OWL',
    'WATER' : 'OCTOPUS',
    'ICE' : 'MAMMOTH'
}

key_list = list(emblem.keys())
val_list = list(emblem.values())

lst = []

def check(animal,text):
    count = 0
    for i in range(0,len(animal)):
        if animal[i] in text:
            count += 1
    if count == len(animal):
        lst.append(key_list[val_list.index(animal)])


for k in mydict.keys():
    check(emblem.get(k),decrypt(mydict.get(k),len(emblem.get(k))))

print(lst)
