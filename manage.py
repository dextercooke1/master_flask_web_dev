from main import app, db, User, Post, Comment

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Comment=Comment)
