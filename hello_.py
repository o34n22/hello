import os
from flask import Flask, request, make_response, session, redirect,\
                    render_template, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import IntegerField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
import logging
import mathplay.arithmetic.nearest_number_2 as nn

# --------------- logging -----------------------------------------------
#logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log',\
                    format='%(levelname)s: %(asctime)s %(message)s'\
                    ,level=logging.INFO)
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')

# -----------------------------------------------------------------------
basedir = os.path.abspath(os.path.dirname(__file__))

# --------------- configuration -----------------------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to dguess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
bootstrap = Bootstrap(app)

# -------------- instantiate --------------------------------------------
db = SQLAlchemy(app) # this thing represents the database


# -------------- models -------------------------------------------------

class Cent(db.Model):
    __tablename__ = 'cents'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, default=1)
#    timedelta = db.Column(db.Interval)
#    user_id = db.Column(db.Integer, default=1)

#    def __repr__(self):
#        return '<Role %r>' % self.name

db.create_all()
db.session.commit()
# -------------- forms --------------------------------------------------

class IntForm(Form):
    answer = IntegerField('Answer:', validators=[Required()], \
                        render_kw={'autofocus':True})
    submit = SubmitField('Submit')
    
# -------------- view functions ----------------------------------------
    
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    response = make_response('<h1>Your prowser is %s </h1>' % user_agent)
    response.set_cookie('answer','42')
    return response


@app.route('/page4',methods=['GET','POST'])
def page4():
#    answer = None
    num = session.get('number')
    if num is None:
        session['number'] = nn.make_n1()
    form = IntForm()
    if form.validate_on_submit():
        session['answer'] = form.answer.data # overwrite any existing answer
        if form.answer.data == int(nn.find_nearest(num)):
            cent = Cent()
            db.session.add(cent)
            db.session.commit()
            session['number'] = None
        elif str(form.answer.data) in nn.permutations(session.get('number')):
            flash('It seems there is a number yet nearer to 500.')
        else:
            flash('Digits aren\'t matching. You must use the digits from \
                  the number given.')
        return redirect(url_for('page4'))
    return render_template('page4.html', form=form,\
                           number=session.get('number'), answer=session.get('answer'))

#@app.route('/page5',methods=['GET','POST'])
#def page5():
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
if __name__ == '__main__':
    app.run(debug=True)