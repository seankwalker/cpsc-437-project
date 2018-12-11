from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import QueryForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/movies'
app.config['SECRET_KEY'] = '7d4e41f27d441f27567d441f2b6176a'
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)


@app.route("/")
def index():
	form = QueryForm(request.form)
	if request.method=='POST':
		year = request.form['year']
		genre=request.form['genre']

		if form.validate():    
			return redirect(url_for('/'))
		else:
			flash(MSG[0])
	return render_template('index.html', form=form)

@app.route("/name/<name>")
def get_movie_name(name):
    return "name : {}".format(name)

if __name__ == '__main__':
    app.debug = True
    app.run()

