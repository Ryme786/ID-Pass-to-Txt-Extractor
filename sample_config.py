import os

api_id = 19259149
api_hash = os.environ.get("API_HASH", "67e9ed15eb0adf9d3b391311933fa594")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "5591734243,1369808729")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "6705657501")
owner_users = [int(num) for num in osowner_users.split("6705657501")]
