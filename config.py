import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21220145"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f7cab9f80f77952272c641af39139562")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://chauhankishansinh174:t6qXWE5P7tTGmcMH@cluster0.wgmunsq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
