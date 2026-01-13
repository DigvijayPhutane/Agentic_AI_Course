# lets create class
class Biryani:
    def __init__(self,rice,chicken):
        self.rice = rice 
        self.chicken = chicken
    def prepare(self):
        print("preparation on")
    def add_Masala(self,massala_level):
        print('massala added')
    def make_biryani(self):
        print("Birayni is done")
my_biryani = Biryani(rice=3,chicken=1)
my_biryani.add_Masala(3)
my_biryani.make_biryani()