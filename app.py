from flask import Flask, render_template, request, redirect, url_for, abort
import os
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('Flask_Key')
import random
global index_left
global index_right
global score
index_left=random.randint(0, 250)
index_right=random.randint(0, 250)
score=0
movies=pd.read_csv('movies.csv')
def rand():
    global index_left
    global index_right

    index_left = random.randint(0, 250)
    index_right = random.randint(0, 250)

    begin_left = movies["Movie"][index_left]
    begin_right = movies["Movie"][index_right]
    begin = [begin_left, begin_right]
    return begin
def next_left():
    global index_right
    global index_left
    global score



    if movies["Rating"][index_left] > movies["Rating"][index_right]:
       print("Better Left")
       index_right = random.randint(0, 250)
       right=movies["Movie"][index_right]
       score+=1
    elif movies["Rating"][index_left] < movies["Rating"][index_right]:
        print("Better Right")
        index_left = random.randint(0, 250)
        left = movies["Movie"][index_left]

        return False
    else:
        print("Both")
        index_right = random.randint(0, 250)
        right = movies["Movie"][index_right]

        score+=1
    return True

def next_right():
    global index_right
    global index_left
    global score
    global photo_right
    global photo_left
    if movies["Rating"][index_left] > movies["Rating"][index_right]:
        print("Better Left")
        index_right = random.randint(0, 250)
        right = movies["Movie"][index_right]
        return False
    elif movies["Rating"][index_left] < movies["Rating"][index_right]:
        print("Better Right")
        index_left = random.randint(0, 250)
        left = movies["Movie"][index_left]

        score+=1


    else:
        print("Both")
        index_left = random.randint(0, 250)
        left = movies["Movie"][index_left]
        score += 1
    return True

def end():
    print("end")

@app.route('/', methods=["GET"])
def home():
    global index_left
    global index_right
    global score
    score =0
    index_left = random.randint(0, 250)
    index_right = random.randint(0, 250)
    return render_template("index.html")
@app.route('/directions', methods=["GET"])
def directions():
    print(score)
    return render_template("directions.html")

@app.route('/game', methods=["GET", "POST"])
def game():
    global index_right
    global index_left

    data=pd.read_csv("images.csv")
    if request.method=="POST":
        if (request.form['choice']=='left'):
            result=next_left()
        elif (request.form['choice']=='right'):
            result=next_right()
        if result==False:
            return redirect("/end")
    return render_template("start.html", data=data, index_left=index_left, index_right=index_right)
@app.route('/end', methods=["GET"])
def end():
    print(score)
    return render_template("end.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)

