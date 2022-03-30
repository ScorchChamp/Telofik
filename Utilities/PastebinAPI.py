import requests
from dotenv import load_dotenv, dotenv_values
load_dotenv()

async def pasteData(values):
    login_data = {
        'api_dev_key': dotenv_values('.env')["PASTEBIN_API_KEY"],
        'api_user_name': dotenv_values('.env')["PASTEBIN_USERNAME"],
        'api_user_password': dotenv_values('.env')["PASTEBIN_PASSWORD"]
    }

    login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
    data = {
        'api_option': 'paste',
        'api_dev_key':dotenv_values('.env')["PASTEBIN_API_KEY"],
        'api_paste_code': values,
        'api_paste_name': "Weights",
        # 'api_paste_expire_date': 'see_https://pastebin.com/api',
        'api_user_key': login.text
        # 'api_paste_format': 'see_https://pastebin.com/api'
        }
    r = requests.post("https://pastebin.com/api/api_post.php", data=data)
    return r.text