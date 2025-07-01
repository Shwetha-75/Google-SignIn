import requests
class Authorization:
      def setAccessToken(self,email:str):
          return requests.get(f"http://localhost:5022/generate-token/{email}").json()
      def getAccessToken(self,access_token:str):
          data={
              'ACCESS_TOKEN_KEY':access_token
          }
          result=requests.post(f"http://localhost:5022/decode-token",json=data).json()
          return result['status']=='ok'         