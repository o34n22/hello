#import os
#basedir = os.path.dirname(__file__)
#a = os.path.join(os.sep,basedir,'mathplay')
#os.sys.path.append(a)

from flask import Flask, request, make_response, session, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import Required

import mathplay.arithmetic.nearest_number_2 as nn
#print(nn.make_n())


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to dguess string'
bootstrap = Bootstrap(app)

class IntForm(Form):
    answer = IntegerField('Answer:', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    response = make_response('<h1>Your prowser is %s </h1>' % user_agent)
    response.set_cookie('answer','42')
    return response

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return '<h1>%s</h1>' % __file__

@app.route('/page3')
def page3():
    number = nn.make_n()
    return '<h1>%s</h1>' % str(number)

@app.route('/page4',methods=['GET','POST'])
def page4():
    answer = None
    number = nn.make_n()
    form = IntForm()
    if form.validate_on_submit():
        answer = form.answer.data
        form.answer.data = ''
    return render_template('page4.html', form=form, number=number, answer=answer)





@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
if __name__ == '__main__':
    app.run(debug=True)