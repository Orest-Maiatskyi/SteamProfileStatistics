import math
import os.path

from flask import Flask

from app.config import current_config

app = Flask(__name__,
            template_folder=os.path.abspath('./app/front/templates/'),
            static_folder=os.path.abspath('./app/front/static/'))

app.config.from_object(current_config)


@app.context_processor
def utility_processor():

    def smart_round(float_num):
        return math.ceil(float_num)

    return dict(smart_round=smart_round)


from app.routes import *
