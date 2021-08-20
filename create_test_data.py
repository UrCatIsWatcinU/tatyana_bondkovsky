from app import db, models

# u = models.User(login='owner')
# u.set_password('site08.2021')

# db.session.add(u)

db.session.add_all([
    models.PriceAge(name='Старшие (8-11 кл)'),
    models.PriceAge(name='Средние (5-7 кл)'),
    models.PriceAge(name='Малыши (3-4 кл)'),
    models.PriceAge(name='Любой'),
])

db.session.add_all([
    models.PriceType(name='Индивидуальные занятия'),
    models.PriceType(name='Груповые занятия (до 6 человек)'),
    models.PriceType(name='Вебинары'),
])

db.session.add_all([
    models.PricePeriod(name='Абонемент на год', min=36),
    models.PricePeriod(name='Пол учебного года', min=12),
    models.PricePeriod(name='Месяц обучения', min=4),
    models.PricePeriod(name='Каждое занятие'),
    models.PricePeriod(name='Льготники, за любой период', is_for_beneficiary=True),
    models.PricePeriod(name='Весь курс', min=1000),
])

db.session.add_all([
# индивидуально
    # старшие
    models.Price(value=2000, type_id=1, age_id=1, period_id=4),
    models.Price(value=1800, type_id=1, age_id=1, period_id=3),
    models.Price(value=1500, type_id=1, age_id=1, period_id=2),
    models.Price(value=1300, type_id=1, age_id=1, period_id=5),
    
    # средние
    models.Price(value=1800, type_id=1, age_id=2, period_id=4),
    models.Price(value=1600, type_id=1, age_id=2, period_id=3),
    models.Price(value=1500, type_id=1, age_id=2, period_id=2),
    models.Price(value=1300, type_id=1, age_id=2, period_id=5),
    
    # младшие
    models.Price(value=1600, type_id=1, age_id=3, period_id=4),
    models.Price(value=1400, type_id=1, age_id=3, period_id=3),
    models.Price(value=1300, type_id=1, age_id=3, period_id=2),
    models.Price(value=1300, type_id=1, age_id=3, period_id=5),

# группы
    # старшие
    models.Price(value=1200, type_id=2, age_id=1, period_id=4),
    models.Price(value=1100, type_id=2, age_id=1, period_id=3),
    models.Price(value=1000, type_id=2, age_id=1, period_id=2),
    models.Price(value=900, type_id=2, age_id=1, period_id=1),

    # средние
    models.Price(value=1200, type_id=2, age_id=2, period_id=4),
    models.Price(value=1000, type_id=2, age_id=2, period_id=3),
    models.Price(value=900, type_id=2, age_id=2, period_id=2),
    models.Price(value=900, type_id=2, age_id=2, period_id=1),

    # младшие
    models.Price(value=1100, type_id=2, age_id=3, period_id=4),
    models.Price(value=950, type_id=2, age_id=3, period_id=3),
    models.Price(value=900, type_id=2, age_id=3, period_id=2),
    models.Price(value=900, type_id=2, age_id=3, period_id=1),

# вебинары
    models.Price(value=400, type_id=3, age_id=4, period_id=3),
    models.Price(value=750, type_id=3, age_id=4, period_id=4),
])

db.session.commit()