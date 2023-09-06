import datetime

class Product():
    def __init__(self, productName, currentPrice,url="",rating=0):
        self.productId = -1
        self.userId = -1
        self.productName = productName
        
        self.currentDate = datetime.datetime.now()
        self.prevDate = datetime.datetime.now()
        
        self.currentPrice = currentPrice
        self.prevPrice = currentPrice
        self.thresholdPrice = 0
        
        self.rating = rating
        self.url = url
        
    # Default object to string conversion
    def __str__(self):
        return f"""
                ProductID = {self.productId} 
                UserId = {self.userId} 
                ProductName = {self.productName} 
                CurrentPrice = {self.currentPrice} 
                PreviousPrice = {self.prevPrice} 
                CurrentDate = {self.currentDate} 
                ThresholdPrice = {self.thresholdPrice}
                PreviousDate = {self.prevDate}
                Url = {self.url}
                Rating = {self.rating}
            """
        