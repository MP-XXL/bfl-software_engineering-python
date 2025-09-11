class Mp:

    content = []


    def append(self, *element):
        Mp.content += list(element)
        print(Mp.content)


    def remove(self, element):
        i = 0
        for ele in Mp.content:
            if ele == element:
                del Mp.content[i]
            else:
                pass
            i += 1
        print(Mp.content)


    """def remove(self, element):
        if element in Mp.content:
            i = Mp.content.index(element)
            del Mp.content[i]"""


    def pop(self):
        del Mp.content[-1]
        print(Mp.content)

    """def pop(self, index):
        i = 0
        for ele in Mp.content:
            if i == index:
                del Mp.content[i]
            else:
                pass
            i +=1"""

    
    def insert(self, index, *element):
        first_half = Mp.content[:index]
        second_half = Mp.content[index:]
        first_half += list(element)
        Mp.content = first_half + second_half

    """ def __repr__(self):
        return f"{Mp.content}"""

    def __str__(self):
        return f"{Mp.content}"

