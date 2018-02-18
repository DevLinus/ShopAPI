from flask_jwt import jwt_required
from flask_restful import Resource,Api,reqparse
from models.item import ItemModel

class Items(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}





class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field can not be left blank")
    parser.add_argument('store_id', type=int, required=True, help="Every Item needs a store id")

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_item_byname(name)
        if item:
            return item.json(), 201
        return {'message': 'item not found'},404




    def post(self,name):
        item = ItemModel.find_item_byname(name)

        data = Item.parser.parse_args()


        if item:
            return {'message': 'item allready exist'}, 404

        item = ItemModel(name, data['price'],data['store_id'])
        if item:
            item.save_to_db()

        return item.json(),201


    def delete(self,name):
        item = ItemModel.find_item_byname(name)
        if item:
            item.delete_from_db()

        return {'message':'Item deleted'}


    def put(self,name):

        data = Item.parser.parse_args()
        item = ItemModel.find_item_byname(name)

        if item is None:
            item = ItemModel(name, data['price'],data['store_id'])
        else:
            item.price = data['price']

        item.save_to_db()
        return item.json(), 200