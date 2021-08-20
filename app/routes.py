from flask_login.utils import login_required
from app import app, db

from flask import render_template, redirect, request, url_for
from werkzeug.urls import url_parse
from flask_login import current_user, logout_user, login_user

from app.models import CallRequest, Price, PriceAge, PricePeriod, PriceType, User
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user is None:
            return render_template('login.html', title='Авторизация', form=form, errors=['username'], user=current_user) 
        if not user.check_password(form.password.data):
            return render_template('login.html', title='Авторизация', form=form, errors=['pwd'], user=current_user) 
        
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
    return render_template('login.html', title='Авторизация', form=form, errors=[], user=current_user)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
@app.route('/index')
def index():
    table = {
        'ages': PriceAge.query.all(),
        'price_types': PriceType.query.all(),
        'periods': PricePeriod.query.all(),
        'prices': Price.query,
    }
    return render_template('index.html', **table) 

@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/call-requests', methods=['GET', 'POST'])
@login_required
def call_requests():
    if request.method == 'POST':
        try:
            db.session.add(CallRequest(**request.values))
            db.session.commit()
        except:
            db.session.rollback()
            return redirect(url_for('index', messages=[{ 'type': 'error', 'message': 'Не удалось записать заявку. Проверьте данные и попробуйте ещё раз' }]))

        return redirect(url_for('success'))

    return render_template('call-requests.html', requests=CallRequest.query.all(), title='Заявки', user=current_user)