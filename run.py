from flask import Flask
from flask_cors import CORS
from app import api_bp

def create_app():
    app = Flask(__name__)
    app.config['JSONIFY_MIMETYPE'] = 'application/ld+json'
    CORS(app)
    app.register_blueprint(api_bp, url_prefix='/')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0')
