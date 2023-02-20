from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route("/",methods=['GET']) 
def home():
    return render_template('home.html')



@app.route('/result', methods=['GET'])
def result():
    number = request.args.get('number')
    if number is None:
        return render_template('error.html')
    try:
        number = int(number)
        if number % 2 == 0:
            result = "even"
        else:
            result = "odd"
        return render_template('calc.html', number=number, result=result)
    except ValueError:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)