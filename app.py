from flask import Flask,request,jsonify,redirect,url_for
from database import user
from flask_cors import CORS
from flask_httpauth  import HTTPBasicAuth
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
CORS(app)

auth = HTTPBasicAuth()
cred = {'tharani':generate_password_hash('1998')}

@auth.verify_password
def verify_password(username,password):
    print(username,password)
    if username in cred and check_password_hash(cred.get(username), password):
          return username
    else:
         print('fail')
         return None
    
@app.route('/secret',methods=['POST'])
@auth.login_required
def secret():  
     return user,200
# jsonify({"message": f"Hello, {auth.current_user()}!"}),200

@app.route('/users',methods=['GET'])
def table():
     usertype = request.args.get('usertype')
     res = []
     for i in user:
          if i['usertype'] == usertype  :
               res.append(i)
     return res 

if __name__ == '__main__':
    app.run(port=3000)