from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("calc.html")
@app.route("/data",methods=["Get","Post"])
def form():
    num1 = request.form["num1"]
    num2 = request.form["num2"]
    op = request.form["op"]
    num1 = int(num1)
    num2 = int(num2)
    op = str(op)
    print(op)
    print(num1)
    print(num2)
    if(op == 'Addition'):
        result = num1 + num2
    elif(op == 'Subtraction'):
        result = num1 - num2
    elif(op == 'Multiplication'):
        result = num1 * num2
    elif(op == 'Division'):
        result = num1 / num2
    else:
        print("invalid")
    result = str(result)
    return result
    return "the result is: ", result



if __name__  == '__main__':
    app.run()
