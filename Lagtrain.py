from PIL import Image
import numpy as np
import time
from PIL import GifImagePlugin
import sys

PIXEL_SIZE = 10
BLACK_WHITE = ([30 , 55 , 80 , 105, 130, 155, 180, 205, 230, 255, 999999999],
               ['M', 'Z', '8', '$', '?', '=', ':', '-', ',', ' ', ' '])
LAGTRAIN = ([30 , 50 , 85 , 92 , 100, 115, 130, 145, 160, 180, 190, 204, 224, 239, 255, 999999999],
            ['M', '+', '$', '?', '=', ':', '-', ',', '.', ' ', '.', ',', 'o', 'O', '+', "X"])
TEMPLATE = LAGTRAIN

class Frame:
    def __init__(self):
        try:
            self.gif = Image.open(f"gifs/{sys.argv[1]}")
        except IndexError:
            print("Wrong command use")
            sys.exit(1)

    def prepare_next_frame(self):
        self.im = self.gif
        self.data1 = np.asarray(self.im)
        self.imsizex = len(self.data1[0])
        self.imsizey = len(self.data1)
        self.data = self.transform_to_squares(self.data1, PIXEL_SIZE)
        self.res = ""
        self.hashmap = []
        self.n = -1
        self.darknessIndex = TEMPLATE[0]
        self.artDarkness = TEMPLATE[1]

    def transform_to_squares(self, imageData, sqsize):
        array_split_1 = np.array_split(imageData, len(self.data1)/sqsize)
        np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
        array_split_2 = np.array([np.array_split(i, len(self.data1[0])/sqsize, 1) for i in array_split_1])
        return array_split_2

    def create_ascii(self):
        for i in self.data:
            self.hashmap.append([])
            self.n += 1
            for j in i:
                self.hashmap[self.n].append(int(j.sum()/len(j)/len(j[0])/3))
        for i in range(len(self.hashmap)):
            for j in range(len(self.hashmap[0])):
                 self.res += self.index_hashmap(i, j)*3
            self.res += "\n"

    def print_ascii(self):
        print(self.res)

    def do_frame(self, frame):
        self.gif.seek(frame)
        self.prepare_next_frame()
        self.create_ascii()
        self.print_ascii()

    def index_hashmap(self, i, j):
        color = self.hashmap[i][j]
        for n in range(len(self.darknessIndex)):
            if color <= self.darknessIndex[n]:
                return self.artDarkness[n]


f = Frame()
for i in range(1, 99999999999):
    try:
        f.do_frame(i)
        print(i)
    except EOFError:
        print("Finished")
        break