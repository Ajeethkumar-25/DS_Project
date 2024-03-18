class country:
    def region(self):
        print("Country is a region")

class india(country):
    def language(self):
        print("Hindi")

    def game(self):
        print("hockey")

class USA(country):
    def language(self):
        print("English")
        
    def game(self):
        print("Football")


india = india()
india.region()
india.game()
india.language()


usa = USA()
usa.language()
usa.game()
usa.region()
