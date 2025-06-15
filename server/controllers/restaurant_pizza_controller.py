from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from sqlalchemy.exc import IntegrityError

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"errors": ["No data provided"]}), 400
        
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')
        
        if not all([price is not None, pizza_id, restaurant_id]):
            return jsonify({"errors": ["Price, pizza_id, and restaurant_id are required"]}), 400
        
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)
        
        if not pizza:
            return jsonify({"errors": ["Pizza not found"]}), 400
        
        if not restaurant:
            return jsonify({"errors": ["Restaurant not found"]}), 400
        
        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        return jsonify(restaurant_pizza.to_dict()), 201
        
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"errors": ["Database integrity error"]}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["An error occurred while creating the restaurant pizza"]}), 400