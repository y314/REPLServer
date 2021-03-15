from flask import Flask,request,json
import os
import time

#init server
app=Flask(__name__)
basic={'yaniv':'hi'}
#run server
if __name__ == '__main__':
    app.run(debug=True)


@app.route ("/", methods=['GET'])
def index():
    return json.dumps(basic)



    