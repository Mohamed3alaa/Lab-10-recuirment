from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#to store the tasks
tasks = []

def add_task(task):
    tasks.append(task)


def get_tasks():
    return tasks

@app.route('/')
def index():
    return render_template('home.html', tasks=get_tasks())

@app.route('/add-task', methods=['POST'])
def add_task_route():
    task = request.form['task']
    add_task(task)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
