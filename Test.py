from Paper import Paper
from Pencil import Pencil

pencil = Pencil(init_point_durability = 100,
                length = 10,
                eraser_durability = 100)
paper = Paper()

pencil.write(paper, "Hi there, hello world")
pencil.erase(paper, "hello")
pencil.edit(paper, "howdy", 10)
print(paper.text)