from flask_login.utils import login_required
from app import app, db
from app.models import *

from flask import redirect
from flask.helpers import url_for
from flask_admin.base import expose
from flask_admin import AdminIndexView, Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

class SecureView():
    def is_accessible(self):
        return current_user.is_authenticated
        

class IndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        if current_user.is_authenticated:
            return super().index()

admin = Admin(app, name='Татьяна Бондковская', index_view=IndexView(), template_mode='bootstrap3')


for model in [Price, PriceAge, PricePeriod, PriceType]:
    class WOLists(SecureView, ModelView):
        column_exclude_list = ['password_hash', 'id']
        column_select_related_list = []
        form_columns = []
        form_extra_fields = {}

        for c in [c.name for c in model.__table__.columns] + column_select_related_list + list(form_extra_fields):
            if('_id' in c):
                c = c.replace('_id', '')
                column_select_related_list.append(c)
            
            if not c in column_exclude_list:
                form_columns.append(c)


    admin.add_view(WOLists(model, db.session, name=model.__admin_name__))