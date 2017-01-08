class House(object):

    def __init__(self, color, doors, windows, height, length):
        self.color = color
        self.doors = doors
        self.windows = windows
        self.length = length

    def paint(self, color):
        self.color = color
        return 'Húsið hefur fengið nýjan lit: {}'.format(self.color)


    def add_window(self, num):
        self.windows += num
        return 'Við bættum við glugga, nú eru þeir {}'.format(self.windows)            

