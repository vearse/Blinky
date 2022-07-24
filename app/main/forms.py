from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields import (
    BooleanField,
    StringField,
    SubmitField,
    SelectField,
    SelectFieldBase
)
from wtforms.validators import Regexp, EqualTo, InputRequired, Length


VOICE_CHOICES = [('zara', 'Zara'), ('daniel', 'Daniel'), ('mia', 'Mia'), ('tessa', 'Tessa'), ('sophia', 'Sophia'), ('alex', 'Alex')]
Language_CHOICES = [('', 'Default'), ('en', 'English'), ('fr', 'French'), ('sh', 'Spanish'), ('ar', 'Arabic'), ('sh', '') ]

class GeneratePodcastForm(FlaskForm):
    # print('Form', FlaskForm)
    link = StringField('Input a Twitter Link', validators=[InputRequired(),
                                        Regexp('/^https?:\/\/twitter\.com\/(?:#!\/)?(\w+)\/status(es)?\/(\d+)$/')])

    language = SelectField('Select Language',choices=Language_CHOICES )

    voice = SelectField('Select Voice', choices=VOICE_CHOICES)

    generate = SubmitField('Generate') 