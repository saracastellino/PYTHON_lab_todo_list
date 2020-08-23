from flask import render_template
from app import app, db
from app.models import User, Task # ADDED

# @app.route('/tasks')
# def index():
#     user = User.query.get(1)
#     tasks = user.tasks
#     return render_template('index.html', title='Home', user=user, tasks=tasks)


@app.route('/')
def index():
    user = {'username': 'Sandy'}
    tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Java',
        'description': 'Learn an awesome new programming language',
        'done': True
    }
    ] # ADDED
    return render_template('index.html', title='Home', user=user, tasks=tasks) # MODIFIED
