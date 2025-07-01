import requests
from flask import jsonify
from dotenv import load_dotenv 
import os 
load_dotenv()

class InsertData:
     
      def insert_user_by_email(self,data):
          try:
             return requests.post(f"{os.getenv("REPOSITORY_URL")}/signin",json=data).json()
          except Exception as exception:
                print(exception)
                return jsonify({
                    "status":"no",
                    "message":"not inserted!!",
                    "user_model":None
                })
          