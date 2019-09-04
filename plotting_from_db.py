#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:53:11 2019

@author: mig
"""

#from flask_script import Manager
from flask import Flask
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#manager = Manager(app)

app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
#db = SQLAlchemy()


class Cent(db.Model):
    __tablename__ = 'cents'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, default=1)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
#class Role(db.Model):
#    __tablename__ = 'roles'
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(64), unique=True)
#    
#    def __repr__(self):
#        return '<Role %r>' % self.name
#
#class User(db.Model):
#    __tablename__ = 'users'
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(64), unique=True, index=True)
#    
#    def __repr__(self):
#        return '<User %r>' % self.username

dates = []

cents = Cent.query.all()
for c in cents:
    dates.append(c.timestamp)

print(len(dates))
#dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]


# ---------------- plotting ------------------------------------


# Choose some nice levels
levels = np.tile(np.zeros(len(dates)),
                 int(np.ceil(len(dates)/7)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
ax.set(title="sample time series for nearest number")

markerline, stemline, baseline = ax.stem(dates, levels,
                                         linefmt="C3-", basefmt="k-",
                                         use_line_collection=True)

plt.setp(markerline, mec="k", mfc="w", zorder=3)

# Shift the markers to the baseline by replacing the y-data by zeros.
markerline.set_ydata(np.zeros(len(dates)))

# annotate lines
vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
#for d, l, r, va in zip(dates, levels, names, vert):
#    ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3),
#                textcoords="offset points", va=va, ha="right")

# format xaxis with 4 month intervals
ax.get_xaxis().set_major_locator(mdates.SecondLocator(bysecond=[0,10,20,30,40,50]))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%M:%S"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y axis and spines
ax.get_yaxis().set_visible(False)
for spine in ["left", "top", "right"]:
    ax.spines[spine].set_visible(False)

ax.margins(y=0.1)
plt.show()

 












#if __name__ == '__main__':
#    manager.run()
    