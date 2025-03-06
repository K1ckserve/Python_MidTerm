class Movie:
    # Q1.1: Initializer method
    def __init__(self, year="2021", rating="PG-13"):
        self.__year = year  # Private attribute
        self.__rating = rating  # Private attribute

    # Q1.2: Mutator (set) methods
    def set_year(self, year):
        self.__year = year

    def set_rating(self, rating):
        self.__rating = rating

    # Q1.3: Accessor (get) methods
    def get_year(self):
        return self.__year

    def get_rating(self):
        return self.__rating

# Subclass ComedyMovie
class ComedyMovie(Movie):
    # Q1.4: Initializer method
    def __init__(self, year="2021", rating="PG-13", comedyType="RomCom"):
        super().__init__(year, rating)  # Call superclass initializer
        self.__comedyType = comedyType  # Private attribute

    # Q1.5: Mutator (set) method
    def set_comedyType(self, comedyType):
        self.__comedyType = comedyType

    # Q1.6: Accessor (get) method
    def get_comedyType(self):
        return self.__comedyType
