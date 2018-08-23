from flask_restful import Resource


class GoodsAPI(Resource):
    def get(self):
        return {'name': 'apple'}

    def post(self):
        pass
