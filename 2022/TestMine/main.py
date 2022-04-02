import random
from time import sleep
from datetime import datetime
import pygame


class Minesweeper:

    def __init__(self, x=10, y=10, mines=25):
        self.x = x
        self.y = y
        self.mines = mines
        self.mine = 'x'
        self.wall = '_'
        self.map = self._filling()
        self.map_with_numbers = self._filling_numbers()
        self.map_for_game = self._filling_map_for_game()

    def _filling(self):
        maps = []
        i = 0
        j = 0
        square = self.x * self.y
        for x in range(self.x):
            line = []
            for y in range(self.y):
                probability = ((self.mines - j) / (square - i)) * 100
                rand = random.randint(1, 100)
                #  sleep(datetime.now().microsecond % 10 / 1000000)
                if rand <= probability:
                    line.append(self.mine)
                    j += 1
                else:
                    line.append(self.wall)
                i += 1
            maps.append(line)
        return maps

    def _filling_numbers(self):
        maps = []
        i, j = len(self.map), len(self.map[0])
        for x in range(i):
            tmp_maps = []
            for y in range(j):
                if self.map[x][y] == self.wall:
                    p = 0
                    if x == 0:
                        if y == 0:
                            if self.map[x][y + 1] == self.mine:
                                p += 1
                            if self.map[x + 1][y] == self.mine:
                                p += 1
                            if self.map[x + 1][y + 1] == self.mine:
                                p += 1
                        elif y == j - 1:
                            if self.map[x][y - 1] == self.mine:
                                p += 1
                            if self.map[x + 1][y] == self.mine:
                                p += 1
                            if self.map[x + 1][y - 1] == self.mine:
                                p += 1
                        else:
                            if self.map[x][y - 1] == self.mine:
                                p += 1
                            if self.map[x][y + 1] == self.mine:
                                p += 1
                            if self.map[x + 1][y - 1] == self.mine:
                                p += 1
                            if self.map[x + 1][y] == self.mine:
                                p += 1
                            if self.map[x + 1][y + 1] == self.mine:
                                p += 1
                    elif x == i - 1:
                        if y == 0:
                            if self.map[x][y + 1] == self.mine:
                                p += 1
                            if self.map[x - 1][y] == self.mine:
                                p += 1
                            if self.map[x - 1][y + 1] == self.mine:
                                p += 1
                        elif y == j - 1:
                            if self.map[x][y - 1] == self.mine:
                                p += 1
                            if self.map[x - 1][y] == self.mine:
                                p += 1
                            if self.map[x - 1][y - 1] == self.mine:
                                p += 1
                        else:
                            if self.map[x][y - 1] == self.mine:
                                p += 1
                            if self.map[x][y + 1] == self.mine:
                                p += 1
                            if self.map[x - 1][y - 1] == self.mine:
                                p += 1
                            if self.map[x - 1][y] == self.mine:
                                p += 1
                            if self.map[x - 1][y + 1] == self.mine:
                                p += 1
                    elif y == 0:
                            if self.map[x][y + 1] == self.mine:
                                p += 1
                            if self.map[x - 1][y] == self.mine:
                                p += 1
                            if self.map[x - 1][y + 1] == self.mine:
                                p += 1
                            if self.map[x + 1][y] == self.mine:
                                p += 1
                            if self.map[x + 1][y + 1] == self.mine:
                                p += 1
                    elif y == j - 1:
                            if self.map[x][y - 1] == self.mine:
                                p += 1
                            if self.map[x - 1][y] == self.mine:
                                p += 1
                            if self.map[x - 1][y - 1] == self.mine:
                                p += 1
                            if self.map[x + 1][y] == self.mine:
                                p += 1
                            if self.map[x + 1][y - 1] == self.mine:
                                p += 1
                    if x != 0 and x != i - 1 and y != 0 and y != j - 1:
                        if self.map[x - 1][y - 1] == self.mine:
                            p += 1
                        if self.map[x - 1][y] == self.mine:
                            p += 1
                        if self.map[x - 1][y + 1] == self.mine:
                            p += 1
                        if self.map[x][y - 1] == self.mine:
                            p += 1
                        if self.map[x][y + 1] == self.mine:
                            p += 1
                        if self.map[x + 1][y - 1] == self.mine:
                            p += 1
                        if self.map[x + 1][y] == self.mine:
                            p += 1
                        if self.map[x + 1][y + 1] == self.mine:
                            p += 1
                    tmp_maps.append(p)
                else:
                    tmp_maps.append(self.mine)
            maps.append(tmp_maps)
        return maps

    def _filling_map_for_game(self):
        map_for_game = []
        i, j = len(self.map), len(self.map[0])
        k = 0
        for x in range(i):
            tmp_map = []
            for y in range(j):
                if k / 10 < 1:
                    tmp_map.append('0' + str(k))
                else:
                    tmp_map.append(str(k))
                k += 1
            map_for_game.append(tmp_map)
        return map_for_game


m = Minesweeper()
#  for x in m.map:
#    print(*x)

for x in m.map_for_game:
    print(*x)
