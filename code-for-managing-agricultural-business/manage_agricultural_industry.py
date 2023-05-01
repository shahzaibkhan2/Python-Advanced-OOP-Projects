# Defining a class for crops
class Crop:
    def __init__(self, name, growth_period, yield_amount): # Constructor
        self.name = name
        self.growth_period = growth_period
        self.yield_amount = yield_amount

    # Defining a magic method to format string
    def __str__(self):
        return f'{self.name} - Growth Period: {self.growth_period}, Yield Amount: {self.yield_amount}'


# Defining a class for fields
class Field:
    def __init__(self, crop, area):
        self.crop = crop
        self.area = area
        self.current_yield = 0

    # Defining a function to add planted crops
    def plant_crop(self):
        self.current_yield = 0

    # Defining a function for harvesting crops
    def harvest_crop(self):
        self.current_yield = self.crop.yield_amount * self.area

    # Magic/Dunder method
    def __str__(self):
        return f'{self.crop.name} - Area: {self.area}, Current Yield: {self.current_yield}'


# Defining a class for farm
class Farm:
    def __init__(self, name):
        self.name = name
        self.crops = []
        self.fields = []

    # Defining a function to add crops
    def add_crop(self, crop):
        self.crops.append(crop)

    # Defining a function to add fields
    def add_field(self, field):
        self.fields.append(field)

    # Defining a function to display crops
    def display_crops(self):
        for crop in self.crops:
            print(crop)

    # Defining a function to display fields
    def display_fields(self):
        for field in self.fields:
            print(field)
