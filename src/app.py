from flask import Flask, render_template, request, redirect, url_for
from database import tasks

app = Flask(__name__)

@app.route('/')
def index():
    all_tasks = tasks.get_all_tasks()
    return render_template('index.html', tasks=all_tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    description = request.form['description']
    tasks.add_task(title, description)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>')
def edit(task_id):
    task = tasks.get_task(task_id)
    return render_template('edit.html', task=task)

@app.route('/update/<int:task_id>', methods=['POST'])
def update(task_id):
    title = request.form['title']
    description = request.form['description']
    status = request.form['status']
    tasks.update_task(task_id, title, description, status)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks.delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    tasks.create_table()
    app.run(debug=True)
