from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.create_db import Tasks


@app.route("/", methods=['POST','GET'])
def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Tasks(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
            
        except:
            return "Algo deu errado ao tentar adicionar a tarefa \(ºbº)/"
            
    else:
        all_tasks = Tasks.query.order_by(Tasks.date_create).all()
        return render_template("index.html", all_tasks = all_tasks)

@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Tasks.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")

    except:
        return "Algo deu errado ao tentar deletar a tarefa \(ºbº)/"

@app.route("/alter_task/<int:id>", methods=['GET','POST'])
def alter_task(id):
    task = Tasks.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect("/")
        except:
            return "Algo deu errado ao tentar alterar a tarefa \(ºbº)/"

    else:
        return render_template("alter_task.html", task=task)
    #try:
        #db.session.