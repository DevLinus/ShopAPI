from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self,name):
        store = StoreModel.find_item_byname(name)
        if store:
            return store.json(), 200
        else:
            return {'Message' : 'Item not found in the Database'}, 404

    def delete(self,name):
        store = StoreModel.find_item_byname(name)
        if store:
            store.delete_from_db()
        return {'message': 'Store Deleted'}

    def post(self,name):
        if StoreModel.find_item_byname(name):
            return {'Message': 'A Store with the Name {} allready Exist'.format(name)}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'Message': 'An Error occured while creating the store'}, 500

        return store.json(), 201



class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
