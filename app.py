from flask import Flask,request,jsonify
import os

def initserver():
    #init server
    app=Flask(__name__)
    basic={'yaniv':'hi'}
    #run server
    if __name__ == '__main__':
        app.run(debug=True)
    #msg('Application initiate OK')

    @app.route ("/", methods=['GET'])
    def index():
        return {'hello':'Yaniv'}


initserver()
