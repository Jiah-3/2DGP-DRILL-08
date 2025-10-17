class Sleep:

    def __init__(self, boy):
        self.boy = boy

    def enter(self):
        self.boy.dir = 0

    def exit(self):
        pass

    def do(self):
        self.boy.frame = (self.boy.frame + 1) % 8
        pass

    def draw(self):
        if self.boy.face_dir == 1:
            self.boy.image.clip_composite_draw(self.boy.frame * 100, 300, 100, 100, 3.14159/2, '', self.boy.x - 25, self.boy.y - 25, 100, 100)
        else:
            self.boy.image.clip_composite_draw(self.boy.frame * 100, 200, 100, 100, -3.14159 / 2, '', self.boy.x + 25, self.boy.y - 25, 100, 100)
