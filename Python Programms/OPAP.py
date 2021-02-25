import requests
import json
import datetime
from collections import Counter

d = datetime.datetime.now()
M = d.strftime("%m")

if d.hour < 9:
    D = d.day-1
else:
    D = d.day

Numbers = []
for i in range(1, D+1):
    number_str = str(i)
    A = number_str.zfill(2)
    x = requests.get('https://api.opap.gr/draws/v3.0/1100/draw-date/2021-{M}-{D}/2021-{M}-{D}/draw-id'.format(D=A, M=M))
    z = x.json()
    Z = z[0]
    X = requests.get("https://api.opap.gr/draws/v3.0/1100/{Z}".format(Z=Z))
    a = json.loads(X.text)
    winning = a["winningNumbers"]['list']
    Numbers.extend(winning)

print("Τα νουμερα απο την πρωτη κληρωση για καθε μερα του συγκεκριμενου μηνα ειναι:", Numbers)
print("Στο συνολο ειναι:", len(Numbers))
g = Counter(Numbers)
print(g)
print(type(g))

y = len(Numbers) / D
G = [(i, g[i] / y * 100) for i, count in g.most_common()]
print(G)
for (x, y) in G:
    print("Ο αριθμος", x, "εχει", y, "% πιθανοτητες να εμφανιστει")
