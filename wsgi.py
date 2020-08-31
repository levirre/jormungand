from flaskr import create_app
from livereload import Server

if __name__ == "__main__":
    app=create_app()
    server = Server(app)
    server.serve(debug=True,port=5000)
from database.makedb import db_session
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()