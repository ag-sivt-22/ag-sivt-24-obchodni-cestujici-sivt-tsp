from __future__ import annotations
from typing import List
from dataclasses import dataclass

@dataclass
class Mesto:
    nazev:str
    sousede: list[tuple[str,int]]

class Graph:
    
    def __init__(self) -> None:
        self.cities : dict[str,Mesto] = {}


    def kolik_mest(self):
        return len(self.cities)
        
    def _jednostrane_pridani_mesta(self, mesto_z: str, mesto_do: str, vzdalenost: int) -> None:
        if mesto_z not in self.cities:
            self.cities[mesto_z] = Mesto(mesto_z,[])

        self.cities[mesto_z].sousede.append((mesto_do,vzdalenost))
        
    def new_edge(self, from_city: str, to_city: str, distance: int) -> None:
        self._jednostrane_pridani_mesta(from_city, to_city, distance)
        self._jednostrane_pridani_mesta(to_city, from_city, distance)

    def najdi_sousedy(self,z_mesta):
        return self.cities[z_mesta].sousede

    def existuje_cesta(self, z_mesta, do_mesta) -> bool:
        return do_mesta in [soused[0] for soused in self.cities[z_mesta].sousede]



@dataclass
class Cesta:
    mesta: List[str]
    delka: int
    
    def pridej_mesto(self, dalsi_mesto, vzdalenost) -> Cesta:
        return Cesta(self.mesta+[dalsi_mesto],self.delka+vzdalenost)


reseni: list[Cesta] = []


def vyzkousej_cesty(graph, dosud_projita_cesta):
    global reseni
    sousedi=graph.najdi_sousedy(dosud_projita_cesta.mesta[-1])    
    for soused,vzdalenost in sousedi:
        if soused in dosud_projita_cesta.mesta:
            continue
        cesta_do_souseda=dosud_projita_cesta.pridej_mesto(soused, vzdalenost)
        if len(cesta_do_souseda.mesta)==graph.kolik_mest():
            if graph.existuje_cesta(soused,cesta_do_souseda.mesta[0]):
                print(f"nasel jsem reseni!: {cesta_do_souseda}")
                reseni.append(cesta_do_souseda)
        else:
            vyzkousej_cesty(graph, cesta_do_souseda)
