# -*- coding: utf-8 -*-

from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    #form = NameForm()
    #if form.validate_on_submit():
    #    return redirect(url_for('.index'))
    return render_template('index.html',
                           name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())


@main.route('/stuff', methods=['GET'])
def stuff():
    return render_template('stuff.html')


@main.route('/events', methods=['GET'])
def events():
    return render_template('events.html')


@main.route('/publications', methods=['GET'])
def publications():
    return render_template('publications.html')


@main.route('/post', methods=['GET'])
def post():
    return render_template('post.html')


@main.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')