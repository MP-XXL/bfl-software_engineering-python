class Forces:


    def __init__(self, force_name, rank, name):
        self.force_name = force_name
        self.rank = rank
        self.name = name


class Personnel(Forces):

    def __init__(self, force_name, rank, name, rifle = False):
        Forces.__init__(self, force_name, rank, name)
        self.rifle = rifle

road_safety = Personnel("Road safety", "Admiral", "Tosin", False)
police = Personnel("Police", "Sergent", "Victor", True)
army = Personnel("Army", "General", "MP", True)

print(army.__dict__)
