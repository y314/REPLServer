from flask import Flask,request,jsonify
import os
def initserver():
    #init server
    app=Flask(__name__)
    basic={'yaniv':'hi'}
    #run server
    #if __name__ == '__main__':
    app.run(debug=True)
    msg('Application initiate OK')

    @app.route ("/", methods=['GET'])
    def index():
        return jsonify(basic)

def msg(content):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    #message = 'Yaniv - Pass wsgi answerd!\n Now you shoud get the app.py\n'
    message='Got MSG\n' + content
    #version = 'Python %s\n' % sys.version.split()[0]
    version='3'
    response = '\n'.join([message, version])
    return [response.encode()]





    