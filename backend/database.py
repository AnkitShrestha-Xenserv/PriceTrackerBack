import json
import pickle
import os
from models.product import Product
from models.user_data import UserData
from .scrap import Scrap

PRODUCT_FILE = "Project\database\product.bin"
USER_FILE = "Project\database\\user.bin"

class Database():
    def __init__(self):
        # Initialize the Scrapper instance
        self.bot = Scrap(teardown=True)
        
    # Helper function for getting and setting data to the database for both Product and User
        
    # Fetches data from the database referred to by the file name and returns it as a list of objects
    def getData(self,file):
        data = []
        try:
            with open(file,'rb') as f:
                while True:
                    try:
                        data.append(pickle.load(f))
                    except EOFError:
                        break
                f.close()
        except FileNotFoundError:
            pass
        return data
    
    # Stores data in the database referred to by the file name and returns True if the insertion was successful
    def storeData(self,file,data):
        try:
            with open(file,'ab') as f:
                for item in data:
                    pickle.dump(item,f,protocol=pickle.HIGHEST_PROTOCOL)
            return True
        except FileNotFoundError:
            return False
        
    # Functions related to Product        

    # Add the specified product to the product table
    def addProduct(self,newProduct : Product):
        data = self.getData(PRODUCT_FILE)
        if data == []:
            newProduct.productId = 0
        else:
            newProduct.productId = data[-1].productId +1
        self.storeData(PRODUCT_FILE,[newProduct])
        return newProduct
    
    # Get a list of all the tracked products for the specified user
    def getUserProducts(self,userId):
        data = self.getData(PRODUCT_FILE)
        result = []
        for product in data:
            if product.userId == userId:
                
                result.append(product)
                
        return result
    
    # Update the details of the tracked product with new information fetched from the URL
    def updatePrices(self,userId):
        data = self.getData(PRODUCT_FILE)
        for index,product in enumerate(data):
            if product.userId == userId:
                tempProduct = self.bot.getProductDetails(product.url)
                product.currentPrice = tempProduct.currentPrice
                product.currentDate = tempProduct.currentDate
                product.rating = tempProduct.rating
                del data[index]
                data.append(product)
                os.remove(PRODUCT_FILE)
                self.storeData(PRODUCT_FILE,data)
        return "Product Updated"
        
                
        
    
    # Remove the specified product from the product table
    def removeProduct(self,productId : Product,userId : UserData):
        data = self.getData(PRODUCT_FILE)
        for index,product in enumerate(data):
            if product.productId == productId and product.userId == userId:
                del data[index]
                os.remove(PRODUCT_FILE)
                self.storeData(PRODUCT_FILE,data)
                return "Product Deleted"
        return "Product not Found"
            
    # Get details of the product from the given URL
    def getProductDetails(self,url):
        return self.bot.getProductDetails(url)
    
    # Functions related to User
    
    # Validates the user credentials and returns the UserData object if successful else returns None
    def login(self,username,password):
        data = self.getData(USER_FILE)
        
        for user in data:
            if(user.userName == username and user.password == password):
                return user
        return None
    
        
    # Add the UserData object to the user table if the username is unique
    def registerUser(self, newUser : UserData):
        data = self.getData(USER_FILE)
    
        for user in data:
            if(newUser.userName == user.userName):
                return "User already exists"
            
        if data == []:
            newUser.userId = 0
        else:
            newUser.userId = data[-1].userId + 1
        return self.storeData(USER_FILE,[newUser])
    
    # Delete a UserData object from the user table
    def deleteUser(self, userId):
        data = self.getData(USER_FILE)
        for index,user in enumerate(data):
            if(user.userId == userId):
                del data[index]
                os.remove(USER_FILE)
                self.storeData(USER_FILE,data)
                return "User deleted"
        return "User not found"
            
        
        