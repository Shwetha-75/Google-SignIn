import requests 
from dotenv import load_dotenv
import os
from flask import jsonify
load_dotenv()

class ReadData:
      def check_if_user_exists(self,email:str):
          try:
              
             result=requests.get(f"{os.getenv("REPOSITORY_URL")}/check/{email}").json()
             return result
          except Exception as exception:
                 print(exception)
                 return jsonify({
                     "status":'no',
                     "message":"something went wrong !!",
                     "user_model":None
                 })