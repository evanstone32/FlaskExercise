from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

orgList = []
dict= {}
@app.route('/result', methods=['GET'])
def result():
    name = request.args.get('name')
    org = request.args.get('org')
    dict[name] = org
    orgList.append(dict)
    return render_template('result.html',name=name,org=org,orgList=orgList,dict=dict)



if __name__ == '__main__':
    app.run(debug=True)