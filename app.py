from flask import Flask,jsonify,request
from flask_restful import Api, Resource

app= Flask(__name__)
api=Api(app)

def checkPostedData(postedData, functionName):
    if (functionName == "add" or functionName=="sub" or functionName=="mul"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    else:
        if (functionName == "div"):
            if "x" not in postedData or "y" not in postedData:
                return 301
            elif int(postedData["y"]==0):
                return 302
            else:
                return 200

class Add(Resource):
    def post(self):
        postedData=request.get_json()

        status_code = checkPostedData(postedData,'add')
        if(status_code!=200):
            retJson = {
                'Message':'An error occured',
                'Status Code': status_code
            }
            return retJson

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x+y
        retMap = {
            'Sum': ret,
            'Status Code': 200
        }
        return retMap

class Subtract(Resource):
    def post(self):
        postedData=request.get_json()

        status_code = checkPostedData(postedData,'sub')
        if(status_code!=200):
            retJson = {
                'Message':'An error occured',
                'Status Code': status_code
            }
            return retJson

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        if x>y:
            ret = x-y
        else:
            ret= y-x
        retMap = {
            'Sub': ret,
            'Status Code': 200
        }
        return retMap

class Multiply(Resource):
    def post(self):
        postedData=request.get_json()

        status_code = checkPostedData(postedData,'mul')
        if(status_code!=200):
            retJson = {
                'Message':'An error occured',
                'Status Code': status_code
            }
            return retJson

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x*y
        retMap = {
            'Result': ret,
            'Status Code': 200
        }
        return retMap

class Divide(Resource):
    def post(self):
        postedData=request.get_json()

        status_code = checkPostedData(postedData,'div')
        if(status_code!=200):
            retJson = {
                'Message':'An error occured',
                'Status Code': status_code
            }
            return retJson

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        if x>y:
            ret = x/y
        else:
            ret= y/x
        retMap = {
            'Result': ret,
            'Status Code': 200
        }
        return retMap

api.add_resource(Add,'/add')
api.add_resource(Subtract,'/sub')
api.add_resource(Multiply,'/mul')
api.add_resource(Divide,'/div')

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__=="__main__":
#    app.run(host="127.0.0.1",port=80)
    app.run(debug=True)
