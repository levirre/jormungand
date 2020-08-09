from flaskr import create_app

if __name__ == "__main__":
    app=create_app()
    app.run(debug=True)
from database.makedb import db_session
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()