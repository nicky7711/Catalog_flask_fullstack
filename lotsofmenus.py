"""
This is the class where create dummy restaurant and menu items!
All of items will be able to be accessed by anyone,
and will be able to edited or deleted by any authenticated users!
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy user
User1 = User(name="Nick", email="nicky7711@udacity.com",
             picture='')
session.add(User1)
session.commit()

# Menu for UrbanBurger
restaurant1 = Restaurant(user_id=1, name="Urban Burger")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Veggie Burger",
                     description="Juicy grilled veggie patty with tomato mayo and lettuce",  # noqa
                     price="$7.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="French Fries",
                     description="with garlic and parmesan",
                     price="$2.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chicken Burger",
                     description="Juicy grilled chicken patty with tomato mayo and lettuce",  # noqa
                     price="$5.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Chocolate Cake",
                     description="fresh baked and served with ice cream",
                     price="$3.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Sirloin Burger",
                     description="Made with grade A beef",
                     price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Root Beer",
                     description="16oz of refreshing goodness",
                     price="$1.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Iced Tea", description="with Lemon",
                     price="$.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Grilled Cheese Sandwich",
                     description="On texas toast with American Cheese",
                     price="$3.49", course="Entree", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Veggie Burger",
                     description="Made with freshest of ingredients and home grown spices",  # noqa
                     price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(user_id=1, name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Chicken Stir Fry",
                     description="With your choice of noodles vegetables and sauces",  # noqa
                     price="$7.99", course="Entree", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Peking Duck",
                     description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook",  # noqa
                     price="$25", course="Entree", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Spicy Tuna Roll",
                     description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",  # noqa
                     price="15", course="Entree", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Nepali Momo ",
                     description="Steamed dumplings made with vegetables, spices and meat. ",  # noqa
                     price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Beef Noodle Soup",
                     description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",  # noqa
                     price="14", course="Entree", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Ramen",
                     description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",  # noqa
                     price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem6)
session.commit()


# Menu for Panda Garden
restaurant1 = Restaurant(user_id=1, name="Panda Garden")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Pho",
                     description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",  # noqa
                     price="$8.99", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chinese Dumplings",
                     description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",  # noqa
                     price="$6.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Gyoza",
                     description="light seasoning of Japanese gyoza with salt and soy sauce, and in a thin gyoza wrapper",  # noqa
                     price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Stinky Tofu",
                     description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",  # noqa
                     price="$6.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Veggie Burger",
                     description="Juicy grilled veggie patty with tomato mayo and lettuce",  # noqa
                     price="$9.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Thyme for that
restaurant1 = Restaurant(user_id=1, name="Thyme for That Vegetarian Cuisine ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Tres Leches Cake",
                     description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",  # noqa
                     price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Mushroom risotto",
                     description="Portabello mushrooms in a creamy risotto",
                     price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Honey Boba Shaved Snow",
                     description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",  # noqa
                     price="$4.50", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Cauliflower Manchurian",
                     description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",  # noqa
                     price="$6.95", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Aloo Gobi Burrito",
                     description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",  # noqa
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Veggie Burger",
                     description="Juicy grilled veggie patty with tomato mayo and lettuce",  # noqa
                     price="$6.80", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Tony's Bistro
restaurant1 = Restaurant(user_id=1, name="Tony\'s Bistro ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Shellfish Tower",
                     description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",  # noqa
                     price="$13.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chicken and Rice",
                     description="Chicken... and rice",
                     price="$4.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Mom's Spaghetti",
                     description="Spaghetti with some incredible tomato sauce made by mom",  # noqa
                     price="$6.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",  # noqa
                     description="Milk, cream, salt, ..., Liquid nitrogen magic",  # noqa
                     price="$3.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Tonkatsu Ramen",
                     description="Noodles in a delicious pork-based broth with a soft-boiled egg",  # noqa
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()


# Menu for Andala's
restaurant1 = Restaurant(user_id=1, name="Andala\'s")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Lamb Curry",
                     description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",  # noqa
                     price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chicken Marsala",
                     description="Chicken cooked in Marsala wine sauce with mushrooms",  # noqa
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Potstickers",
                     description="Delicious chicken and veggies encapsulated in fried dough.",  # noqa
                     price="$6.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Nigiri Sampler",
                     description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="$6.75", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Veggie Burger",
                     description="Juicy grilled veggie patty with tomato mayo and lettuce",  # noqa
                     price="$7.00", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Auntie Ann's
restaurant1 = Restaurant(user_id=1, name="Auntie Ann\'s Diner' ")

session.add(restaurant1)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Chicken Fried Steak",
                     description="Fresh battered sirloin steak fried and smothered with cream gravy",  # noqa
                     price="$8.99", course="Entree", restaurant=restaurant1)

session.add(menuItem9)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Boysenberry Sorbet",
                     description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",  # noqa
                     price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Broiled salmon",
                     description="Salmon fillet marinated with fresh herbs and broiled hot & fast",  # noqa
                     price="$10.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Morels on toast (seasonal)",
                     description="Wild morel mushrooms fried in butter, served on herbed toast slices",  # noqa
                     price="$7.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Tandoori Chicken",
                     description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",  # noqa
                     price="$8.95", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Veggie Burger",
                     description="Juicy grilled veggie patty with tomato mayo and lettuce",  # noqa
                     price="$9.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem10 = MenuItem(user_id=1, name="Spinach Ice Cream",
                      description="vanilla ice cream made with organic spinach leaves",  # noqa
                      price="$1.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem10)
session.commit()


# Menu for Cocina Y Amor
restaurant1 = Restaurant(user_id=1, name="Cocina Y Amor ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Super Burrito Al Pastor",
                     description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",  # noqa
                     price="$5.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Cachapa",
                     description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",  # noqa
                     price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


restaurant1 = Restaurant(user_id=1, name="State Bird Provisions")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Chantrelle Toast",
                     description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",  # noqa
                     price="$5.95", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Guanciale Chawanmushi",
                     description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",  # noqa
                     price="$6.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Lemon Curd Ice Cream Sandwich",
                     description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",  # noqa
                     price="$4.25", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


print "added menu items!"
