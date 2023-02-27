from flask import Flask, render_template, request,redirect
from datetime import datetime
from DB_CONN import *



def get_data():
    data = conn.returnQuery('SELECT * FROM tasks where is_completed=0')
    return data


def get_data_done():
    data = conn.returnQuery('SELECT * FROM tasks where is_completed=1')
    return data

app = Flask(__name__)

tasks = []
done_tasks = []

@app.route('/', methods=['POST','GET'])
def homepage():
    if request.method == 'POST':
        task_content = request.form['content']
        mydata = [conn.get_nextID('tasks','id'), task_content, datetime.now()]
        conn.NonReturnQuery(f"INSERT INTO tasks(id,task,add_date) VALUES ({mydata[0]},'{mydata[1]}','{mydata[2]}')")
        #tasks.append(task_content)
        return redirect('/')
    else:
        tasks = get_data()
        done_tasks = get_data_done()
        return render_template('index.html', title='Task Manager', Task=tasks, done_tasks=done_tasks)


@app.route('/delete/<int:x>')
def delete_item(x):
    conn.NonReturnQuery(f'DELETE FROM tasks WHERE id={x}')
    return redirect('/')

@app.route('/done/<int:x>')
def item_completed(x):
    conn.NonReturnQuery(f'UPDATE tasks SET is_completed=1 WHERE id={x}')
    return redirect('/')

@app.route('/undone/<int:x>')
def item_notcompleted(x):
    conn.NonReturnQuery(f'UPDATE tasks SET is_completed=0 WHERE id={x}')
    return redirect('/')


@app.route('/update/<int:x>', methods=['POST', 'GET'])
def update_item(x):
    if request.method == 'POST':
        conn.NonReturnQuery(f"UPDATE tasks SET task='{request.form['content']}' WHERE id={x}")
        return redirect('/')
    else:
        currItem = conn.returnQuery(f'SELECT task from tasks where id={x}')
        return render_template('update.html', Task=currItem, index=x)


if __name__ == '__main__':
   # print(tasks[0][1])
    conn.init_db()
    cr = conn.connect()
    conn.get_nextID('tasks','id')
    app.run(debug=False, host='192.168.1.7', port=5000)

