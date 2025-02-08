# wordgames/web/__init__.py
"""Web interface for word game tools."""
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)
    
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
