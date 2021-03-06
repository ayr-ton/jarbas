import os

from django.conf import settings
from django_assets import Bundle, register
from webassets.filter import register_filter
from webassets_elm import Elm

register_filter(Elm)

frontend_path = os.path.dirname(settings.ASSETS_ROOT)

elm = Bundle(
    os.path.join(frontend_path, 'elm', 'Main.elm'),
    filters=('elm', 'rjsmin'),
    depends=('**/*.elm'),
    output='app.js'
)


sass = Bundle(
    os.path.join(frontend_path, 'sass', 'app.sass'),
    filters=('libsass'),
    depends=('**/*.sass'),
    output='app.css'
)

register('elm', elm)
register('sass', sass)
