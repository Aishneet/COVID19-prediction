from flask import Flask, render_template,request
import AMF_code

app = Flask(__name__)

@app.route('/')
def test_server():
    return "<html><body><h2>The model is ready to predict!</h2></body></html>"

@app.route('/input')
def form():
    return render_template("form.html")

@app.route('/input',methods = ['POST'])
def form_post():
    date = request.form['text']
    result = int(float(AMF_code.go(date)['Results']['output1'][0]['Scored Labels']))
    result = result * 8 + 1010
    return '<html><body><h1>The confirmed cases are : {0} </h1></body></html>'.format(str(result))

if __name__ == '__main__':
    app.run(debug= True)