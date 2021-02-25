import json
file = open("dictionary.txt", "r")
cont = file.read()
dicti = json.loads(cont)
file.close()
freq={}
def get_all_keys(dictio):
    for n, aksia in dictio.items():
        if type(aksia) is dict:
            get_all_keys(aksia)
            if (n in freq):
                freq[n] += 1
            else:
                freq[n]=1
        elif (n in freq):
            freq[n] += 1
        else:
            freq[n]=1
        if type(aksia) is list:
            for i in range(len(aksia)):
                if type(aksia[i]) is dict:
                    get_all_keys(aksia[i])
get_all_keys(dicti)
keyWithMaxValue = max(freq.items(), key=lambda x: x[1])
listOfKeysWithMaxFreq = list()
for key, aksia in freq.items():
    if aksia == keyWithMaxValue[1]:
        listOfKeysWithMaxFreq.append(key)
print(listOfKeysWithMaxFreq)
