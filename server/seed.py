from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    with app.app_context():
        print("Clearing existing data...")
        RestaurantPizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()
        
        print("Creating restaurants...")
        restaurant1 = Restaurant(name="Dominic's Pizza", address="123 Main St, New York, NY")
        restaurant2 = Restaurant(name="Kiki's Pizza", address="456 Oak Ave, Brooklyn, NY")
        restaurant3 = Restaurant(name="Tony's Italian", address="789 Pine St, Queens, NY")
        
        print("Creating pizzas...")
        pizza1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
        pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
        pizza3 = Pizza(name="Supreme", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni, Sausage, Bell Peppers, Onions")
        pizza4 = Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Cheese, Ham, Pineapple")
        pizza5 = Pizza(name="Vegetarian", ingredients="Dough, Tomato Sauce, Cheese, Bell Peppers, Mushrooms, Onions, Olives")
        
        db.session.add_all([restaurant1, restaurant2, restaurant3])
        db.session.add_all([pizza1, pizza2, pizza3, pizza4, pizza5])
        db.session.commit()
        
        print("Creating restaurant-pizza associations...")
        associations = [
            RestaurantPizza(price=12, restaurant=restaurant1, pizza=pizza1),
            RestaurantPizza(price=15, restaurant=restaurant1, pizza=pizza2),
            RestaurantPizza(price=18, restaurant=restaurant1, pizza=pizza3),
            
            RestaurantPizza(price=14, restaurant=restaurant2, pizza=pizza1),
            RestaurantPizza(price=16, restaurant=restaurant2, pizza=pizza4),
            RestaurantPizza(price=17, restaurant=restaurant2, pizza=pizza5),
            
            RestaurantPizza(price=13, restaurant=restaurant3, pizza=pizza2),
            RestaurantPizza(price=19, restaurant=restaurant3, pizza=pizza3),
            RestaurantPizza(price=15, restaurant=restaurant3, pizza=pizza5),
        ]
        
        db.session.add_all(associations)
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()