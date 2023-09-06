from backend.scrap import Scrap
from backend.database import Database
from models.user_data import UserData
from process import Process
import json

process = Process()

db = Database()
url = "https://www.daraz.com.np/products/t500-smart-watch-with-bluetooth-call-heart-rate-monitor-for-men-and-women-i119504763-s1032714012.html?spm=a2a0e.11779170.just4u.1.287d2d2bmK3DRQ&scm=1007.28811.312168.0&pvid=afe9a65b-9ca1-433b-b4c8-60c9fca385d0&clickTrackInfo=pvid%3Aafe9a65b-9ca1-433b-b4c8-60c9fca385d0%3Bchannel_id%3A0000%3Bmt%3Ahot%3Bitem_id%3A119504763%3B"
url1 = "https://www.daraz.com.np/products/s1-extra-bass-earphone-with-hd-microphone-i123232444-s1033482127.html?spm=a2a0e.11779170.flashSale.2.287d2d2bDhUQIZ"
url2 = "https://www.daraz.com.np/products/tg113-super-bass-splashproof-portable-bluetooth-speaker-i123179288-s1033468294.html?&search=pdp_same_topselling?spm=a2a0e.pdp.recommend_2.3.2479JJsNJJsN0M&mp=1&scm=1007.38553.252219.0&clickTrackInfo=2718fc99-4358-4ad2-9e56-5ba817d62f28__123179288__7496__trigger2i__309933__0.31__0.31__0.0__0.0__0.0__0.31__2__null__null__null__null__null__null____1200.0__0.43333333333333335__0.0__0__680.0__12005__null__null__null__3650.16544_955.3632__null__28557__null__0.0__0.0________null__null"
#p1 = process.getProductDetails(url1)
#p2 = process.getProductDetails(url2)

# Register a new user
print(process.registerUser("B","Hello","John","Smith"))
#print(db.deleteUser(3))

# Login to the server
loggedInUser = process.login("B","Hello")
if loggedInUser != None:
    #process.addTrackedProducts(url1, loggedInUser.userId,500)
    #process.addTrackedProducts(url, loggedInUser.userId,500)
    #process.addTrackedProducts(url2, loggedInUser.userId,500)
    
    #print(process.updatePrices(loggedInUser.userId))
    #print(process.addTrackedProducts(url, loggedInUser.userId))
    
    result = process.getTrackedProducts(loggedInUser.userId)
    
    for product in result:
        print(product)
#   print("Successfully logged in")
#   print(loggedInUser)

#result = process.getProductDetails("https://www.daraz.com.np/products/premium-luxury-velvet-king-size-bed-sheet-with-pillow-covers-i112412964-s1030412185.html?spm=a2a0e.11779170.flashSale.2.287d2d2blai8fQ")
#print("Name = ",result.name)
#print("Price = ",result.price)
#print("Url = ",result.url)
# Url to Scrap
#url = "https://www.daraz.com.np"

#with Scrap(teardown=True) as bot:

    # Load the required website
    #bot.loadWebsite(url)
    
    # Search for any product
    #bot.search("Apple MacBook")
    
    # Get the searched products as a list of Product objects
    #results = bot.getTopSearchResults()
    
    # Track a certain product
    #result = bot.trackProduct()
    #print("Name = ",result.name, "Price = ",result.price)
    