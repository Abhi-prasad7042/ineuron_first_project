from flask import Flask,redirect,url_for,render_template,request


app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():

    return "Starting machine learning project"

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)