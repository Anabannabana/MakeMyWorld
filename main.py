import flask
from flask import render_template, request


def sort2d(array):
    array.sort(key=lambda x: x[0])
    
app = flask.Flask(__name__)
recipes = []
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/newrecipe",methods=['GET', 'POST'])

def newrecipe():
    global recipes
    if request.method == 'GET':
        return render_template('newrecipe.html')
    if 'Dish' in request.form:
        dish = request.form['Dish']
        number = 1
        for i in recipes:
            if i[0].lower() == dish.lower():
                    number +=  1                    
        body = request.form['RecipeBody']
        recipes.append([dish, body, number])
        return flask.redirect('/')
    return 'No form data found!'  
@app.route("/search")
def search():
    return render_template("search.html")
@app.route("/getsearch")
def getsearch():
    if 'DishQuery' in request.args:
        for i in recipes:
            if i[0].lower() == request.args['DishQuery'].lower() or i[0].lower() + " " + str(i[2]) == request.args['DishQuery'].lower():
                formatted = i[1].replace("\n","<br>")
                return render_template("browse.html", recipedish = i[0], recipe = formatted)
        return render_template("searchnotfound.html")
    return "No Form Data Found!"

@app.route("/browse")
def browse():
    string = ""
    sort2d(recipes)
    for i in recipes:
        string += i[0] + " " + str(i[2]) + "<br>"
    return render_template("database.html",string = string)

if __name__ == '__main__':
    app.run()

