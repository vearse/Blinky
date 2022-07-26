from flask import Blueprint, render_template, flash, request, url_for, redirect

from app.models import EditableHTML, Podcaster
from app.main.forms import GeneratePodcastForm
from app.podcast.generate import podcast_generator
from flask_login import  login_required


main = Blueprint('main', __name__)


@main.route('/')
def index():
    form = GeneratePodcastForm()
    return render_template('main/index.html', form=form)
  

@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template(
        'main/about.html', editable_html_obj=editable_html_obj)
 

@main.route('/generate/podcast', methods=['POST'])
@login_required
def generate_podcast():

    form = GeneratePodcastForm()
    
    print('====================',form.validate_on_submit(), form.link)

    if (form.link):
        link = form.link.data
        language =form.language.data
        voice = form.voice.data

        player = podcast_generator(link, language, voice)

        # return render_template('main/playpodcast.html', form=form)
        return redirect(url_for('account.edit_podcast',code=player.code))
    return render_template('main/index.html', form=form)
