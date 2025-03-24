from typing import List, Tuple
from dataclasses import dataclass
class Graph:
    
    def __init__(self) -> None:
        self.cities : set[str] = set()
    
    def new_edge(self, from_city: str, to_city: str, distance: int) -> None:
        ...