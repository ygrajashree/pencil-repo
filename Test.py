from Paper import Paper
from Pencil import Pencil

paper = Paper()
pencil = Pencil(init_point_durability = 20,
                length = 10,
                eraser_durability = 10)

pencil.write(paper, "Hi there hello world.")
print("After first write: ", paper.text)

pencil.sharpen()
pencil.write(paper, " Welcome to my activity!!")
print("After second write: ", paper.text)

pencil.erase(paper, "hello")
print("After erasing: ", paper.text)

pencil.sharpen()
pencil.edit(paper, "howdy", 9)
print("After editing: ", paper.text)