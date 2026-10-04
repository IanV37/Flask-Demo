from flask import Blueprint, render_template, redirect

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "Hello, Flask!"

@main.route('/todoList', methods=['GET'])
def get_todoList():
    return render_template('todolist.html')

@main.route('/todoList/update', methods=["POST"])
def update_todo():
    return redirect('get_todoList')

