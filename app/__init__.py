from flask import Flask
# from dbconfig import Config

def create_app():
    app = Flask(__name__)
    # app.dbconfig.from_object(Config)

    from app.api.v1.mikrotik.routes import mikrotik_bp
    from app.api.v1.mikrotik.pppProfile.routes import pppProfile_bp

    app.register_blueprint(mikrotik_bp, url_prefix='/api/v1/mikrotik')
    app.register_blueprint(pppProfile_bp, url_prefix='/api/v1/mikrotik/pppProfile')

    return app
