from app import app
import os

if __name__ == "__main__":
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"),
            debug=True, ssl_context=('cert.pem', 'key.pem'))
