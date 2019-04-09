from flask import Flask
from flask_cors import CORS

def create_app(config_filename):
    app = Flask(__name__)
    app.config['JSONIFY_MIMETYPE'] = 'application/ld+json'
    CORS(app)
    app.config.from_object(config_filename)

    @app.route('/', methods=['GET'])
    def index():
        return 'Ok'

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run()
