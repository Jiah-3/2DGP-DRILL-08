class AutoRun:
    def __init__(self, boy):
        self.boy = boy

    def enter(self, e):
        self.boy.dir = self.boy.face_dir

    def exit(self, e):
        pass

    def do(self):
        self.boy.frame = (self.boy.frame + 1) % 8
        self.boy.x += self.boy.dir * 10
        if self.boy.x < 0:
            self.boy.x = 0
            self.boy.dir = self.boy.face_dir = 1
        elif self.boy.x > 800:
            self.boy.x = 800
            self.boy.dir = self.boy.face_dir = -1

    def draw(self):
        if self.boy.face_dir == 1:  # right
            self.boy.image.clip_draw(self.boy.frame * 100, 100, 100, 100, self.boy.x, self.boy.y + 10, 150, 150)
        else:  # face_dir == -1: # left
            self.boy.image.clip_draw(self.boy.frame * 100, 0, 100, 100, self.boy.x, self.boy.y + 10, 150, 150)
