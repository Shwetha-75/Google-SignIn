import os
from flask import Flask, request, jsonify,Blueprint
from flask_cors import CORS
from app.GoogleAuthRequired import googleAuthRequired
from app.Repository.InsertData import InsertData
from app.Repository.ReadData import ReadData

app = Flask(__name__)

blue_print=Blueprint('Google_SignIn',__name__)

CORS(app,supports_credentials=True, origins={r'/*':{"origins":
    [os.getenv("FRONTEND_URL"),
      os.getenv("API_GATEWAY_URL")]
    }})


@blue_print.route('/')
def index():
    return "Flask backend for Google Sign-In"

@blue_print.route('/signin/auth/google', methods=['POST','GET'])
@googleAuthRequired.google_auth_required
def google_signin():
    try:
        user_data = request.user_data
        # return SetToken.SetToken().setHttpHeaderToken(user_data)
        print(user_data)
        if user_data:
            # print(user_data)
            result=ReadData().check_if_user_exists(user_data['email'])
            # if the user exist no need to to store persistently 
            print("User data :  ",result)
            if result['status']=='yes':
                return result 
            else:
                # insert it
                print("Trying to insert User data: ",user_data)
                result=InsertData().insert_user_by_email(user_data)
                return result  
        else:
            return jsonify({
                    "status":"no",
                    "message":"not inserted!!",
                    "user_model":None
                })
    except Exception as exception:
           print("There is some problem in authentication: ",exception)
           return jsonify({
                    "status":"no",
                    "message":"not inserted!!",
                    "user_model":None
                })
        


        
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=os.getenv('PORT'))