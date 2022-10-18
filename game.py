import pygame
import engine

class Opponent:
    def __init__(self, id, name, hp) -> None:
        pass

class Game:
    def __init__(self, id, opponent) -> None:
        self.id    = id
        self.opponent = opponent

    def run(self):
        running = True
        
