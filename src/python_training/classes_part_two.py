from cat_class import Cat

# Second Class which Extends the First Class
class Persian(Cat):
    # Roar
    def roar(self):
        print(f"{self.cat_name} roars!")

# Persian Cat Object
persian_cat = Persian('victor')

# Meow
persian_cat.meow()

# Roar
persian_cat.roar()
    