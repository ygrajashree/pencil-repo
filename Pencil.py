class Pencil:

    def __init__(self, init_point_durability, length, eraser_durability):
        self.init_point_durability = init_point_durability
        self.point_durability = init_point_durability
        self.pencil_length = length
        self.eraser_durability = eraser_durability

    def write(self, paper, input_text):
        """Appends the input text to the end of a paper based on point durability."""

        for character in input_text:
            idx = len(paper.text)
            durability_reduction = self.eval_point_durability(character)
            if self.point_durability - durability_reduction >= 0:
                self.insert_character(paper, character, idx)
                self.point_durability -= durability_reduction
            else:
                self.insert_character(paper, " ", idx)

    def sharpen(self):
        """When a pencil is sharpened, it regains its initial point durability
        and length of the pencil will be reduced by one unit."""

        if self.pencil_length > 0:
            self.point_durability = self.init_point_durability
            self.pencil_length -= 1

    def erase(self, paper, text_to_erase):
        """Removes text from a paper by finding the text from backwards."""

        try:
            text_index = paper.text.rfind(text_to_erase)
        except ValueError:
            return

        if self.eraser_durability == 0:
            pass
        elif self.eraser_durability < len(text_to_erase):
            paper.text = paper.text[0:text_index] \
                         + paper.text[text_index:].replace(text_to_erase[-self.eraser_durability:], " " * self.eraser_durability, 1)
            self.eraser_durability = 0
        else:
            paper.text = paper.text[0:text_index] \
                         + paper.text[text_index:].replace(text_to_erase, " " * len(text_to_erase), 1)
            self.eraser_durability -= len(text_to_erase)

    def edit(self, paper, new_text, index):
        """Edits existing text on a paper."""
        for character in new_text:
            self.edit_character(paper, character, index)
            index += 1

    def edit_character(self, paper, character, index):
        """Edits a single `character` at specifed `index` in the `paper` text."""

        durability_reduction = self.eval_point_durability(character)
        if self.point_durability - durability_reduction >= 0:
            if paper.text[index] == ' ':
                self.insert_character(paper, character, index)
            else:
                self.insert_character(paper, '@', index)

            self.point_durability -= durability_reduction

    def eval_point_durability(self, character):
        """Funtion to evaluate the point durability reduction for upper case and lower case characters"""

        if character.islower(): # For lower case, reduce the durability by 1
            return 1
        else: # For upper case, reduce the durability by 2
            return 2

    def insert_character(self, paper, character, idx):
        """Function to insert a single character at a specified index of the text in paper."""

        paper.text = (paper.text[:idx] + character + paper.text[idx+1:])
