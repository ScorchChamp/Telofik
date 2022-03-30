from Log.Logger import *
from EventHandlers import *
from scorch_api.bot import *
from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values(".env")

# Setup environment config
setupLogger()


if __name__=="__main__":
    startBot(config['DISCORD_TOKEN'])