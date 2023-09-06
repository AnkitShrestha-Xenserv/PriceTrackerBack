from flask import Flask,jsonify,request
from models.product import Product
from models.user_data import UserData
import requests
import json
from process import Process

app = Flask(__name__)

"""
dict = [{"productName": "Computer",
        "productId":"2",
        "previousDate":"2020/05/05",
        "previousPrice":"1000",
        "currentPrice":"2000",
        "currentDate":"2020/05/05",
        "thresholdPrice":"1500",
        "rating":"2",
        "url":"hello"
        },{"productName": "Desktop",
        "productId":"2",
        "previousDate":"2020/05/05",
        "previousPrice":"1000",
        "currentPrice":"2000",
        "currentDate":"2020/05/05",
        "thresholdPrice":"1500",
        "rating":"2",
        "url":"hello"}]
"""
userDict = [{"userId":"-1","username":"","password":"","firstName": "","lastName":"","phoneNumber":""}]
process = Process()

def getProductJson(product : Product):
    data = []
    for item in product:
        name = item.productName.split(" ")[0:3];
        itemJson = {"productName": ''.join(name),
                    "productId": str(item.productId),
                    "previousDate": str(item.prevDate.strftime("%Y-%m-%d")),
                    "previousPrice":str(item.prevPrice),
                    "currentDate":str(item.currentDate.strftime("%Y-%m-%d")),
                    "currentPrice":str(item.currentPrice),
                    "thresholdPrice":str(item.thresholdPrice),
                    "rating":str(item.rating),
                    "url":item.url
                    }
        data.append(itemJson)
    return data

def getUserJson(user: UserData):
    userJson = {"userId": str(user.userId),
                "username": user.userName,
                "password": user.password,
                "firstName":user.firstName,
                "lastName":user.lastName,
                "phoneNumber":user.phoneNumber
                }
    return userJson
    
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method== "POST":
        data = json.loads(request.data)
        thing = process.login(data['username'], data['password'])
        if(thing == None):
            return json.dumps(getUserJson(thing))
    return json.dumps(userDict)

@app.route('/fetchProduct',methods=["POST","GET"])
def fetchProduct():
    if request.method == 'POST':
        data = json.loads(request.data)
        print(int(data['userId']))
        thing = process.getTrackedProducts(int(data['userId']))
        return json.dumps(getProductJson(thing))
    return json.dumps(dict)

@app.route('/',methods=["POST"])
def start():
    return 'Hello'

@app.route('/addProduct',methods=["POST","GET"])
def addProduct():
    print('here to add product')
    if request.method == 'POST':
        print('inside')
        data = json.loads(request.data)
        print(data['url'])
        print(data['userId'])
        print(data['thresholdPrice'])
        thing = process.addTrackedProducts(data['url'], int(data['userId']), int(data['thresholdPrice']))
        return json.dumps(getProductJson(thing))
    print("here")
    return json.dumps(dict)

app.run();