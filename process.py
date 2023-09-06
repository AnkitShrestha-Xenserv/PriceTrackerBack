from models.product import Product
from models.user_data import UserData
from backend.database import Database

class Process():
    def __init__(self):
        # Initialize the Database instance
        self.db = Database()
    
    # Add the deatils of the product from the given URL to the database
    def addTrackedProducts(self,url,userId,thresholdPrice):
        product = self.db.getProductDetails(url)
        product.userId = userId
        product.thresholdPrice = thresholdPrice
        return self.db.addProduct(product)
    
    # Get a lit of all the tracked products for the specified user
    def getTrackedProducts(self,userId):
        return self.db.getUserProducts(userId)
    
    # Update the details of the tracked product with new information fetched from the URL
    def updatePrices(self,userId):
        return self.db.updatePrices(userId)

    # Remove the specified product from the product table
    def removeProduct(self,productId,userId):
        return self.db.removeProduct(productId,userId)
    
    # Add the UserData object to the user table if the username is unique
    def registerUser(self, userName,password,firstName,lastName,phoneNumber="98542000"):
        newUser = UserData(userName,password,firstName,lastName,phoneNumber)
        return self.db.registerUser(newUser)
    
    # Validates the user credentials and returns the UserData object if successful else returns None
    def login(self,username,password):
        return self.db.login(username, password)
    
    # Delete a UserData object from the user table
    def deleteUser(self, userId):
        return self.db.deleteUser(userId)