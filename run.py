from app import createApp
from dotenv import load_dotenv 
import os
load_dotenv()

app=createApp()
if __name__=='__main__':
   app.run(port=os.getenv('PORT'),debug=True)
