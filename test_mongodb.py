from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
## Change to actual password
uri = "mongodb+srv://ayushkadam0907_db_user:<@yourpassword>@cluster0.biiuxql.mongodb.net/?appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)