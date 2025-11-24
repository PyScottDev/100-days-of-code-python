class Country:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

    def details(self):
        print(f"The capital of {self.name} is {self.capital}.")



c1 = Country("Scotland", "Edinburgh")
c2 = Country("Ireland", "Dublin")
c3 = Country("Italy", "Rome")
c4 = Country("Wales", "Cardiff")

country_list = [c1,c2,c3,c4]

for country in country_list:
    country.details()

# print(country_list)
# c1.details()
# c2.details()
# c3.details()