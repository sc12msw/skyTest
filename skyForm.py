from flask import Flask, render_template, request
import json
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/form",methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        ##If form posted get the dictionary and remove array number
        ##This is not effcient and could be improved by reciveving json directly from request with .get_json.
        if request.json:
            data = request.json
            print(data)
            writeToFile(data)
            return render_template('form.html', data=readFromFile())
        else:
            print('failed')
            return render_template('form.html',data=readFromFile())
    else:
        with open('formData.json') as jsonF:
            return render_template('form.html', data=readFromFile())


def readFromFile():
    with open('formData.json') as jsonF:
        return json.load(jsonF)

def writeToFile(data):
    with open('formData.json', 'w') as jsonF:
        json.dump(data,jsonF)
