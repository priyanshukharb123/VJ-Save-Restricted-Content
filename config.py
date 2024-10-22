import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "15269032"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "502a412c9dd31ae07c30c315e0ad36de")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://hardwork2990:hjFCo0jjiXsveJOa@cluster0.zkbki.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
