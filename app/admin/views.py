# -*- coding: utf-8 -*-

from flask import Flask
from flask_admin import Admin, BaseView, expose
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from . import admin
from ..auth import auth
from ..models import User, db


@admin.route('/')
@admin.route('/index.html')
@login_required
def admin_index():
    return render_template('admin/index.html')


@admin.route('/new-article')
@admin.route('/new-article.html')
@login_required
def admin_new_article():
    return render_template('admin/new-article.html')


