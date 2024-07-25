from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class ReviewForm(FlaskForm):
    rating = IntegerField('Рейтинг', validators=[
        DataRequired(), NumberRange(min=1, max=5)])
    review = TextAreaField('Текст отзыва', validators=[DataRequired()])
    submit = SubmitField('Отправить')