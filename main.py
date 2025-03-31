from graph import Cesta, vyzkousej_cesty
from europe import load_europe

evropa = load_europe()
print(evropa)

cesta = Cesta(["Madrid"], 0)
vyzkousej_cesty(evropa, cesta)
print("hotovo")