from flask import Flask, render_template, request, flash, redirect, jsonify
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "kabum-case"


@app.route("/")
def home():
    return render_template("html/index.html")

@app.route("/register", methods=['POST'])
def register():
    fullname = request.form.get('fullname')
    cpf = request.form.get('cpf')
    rg = request.form.get('rg')
    email = request.form.get('email')
    birthday = request.form.get('birthday')
    phone1 = request.form.get('phone1')
    phone2 = request.form.get('phone2')
    adress = request.form.get('adress')

    new_user = {
        "fullname": fullname,
        "cpf": cpf,
        "rg": rg,
        "email": email,
        "birthday": birthday,
        "phone1": phone1,
        "phone2": phone2,
        "adress": adress,
        "active": True,
    }

    with open('file.json', 'r') as users_file:
        users_data = json.load(users_file)
    
    users_data.append(new_user)

    with open('file.json', 'w') as users_file:
        json.dump(users_data, users_file, indent=4)

    flash('Usuário cadastrado')
    return redirect("./list")

@app.route("/list")
def view_users():
    with open('file.json', 'r') as users_file:
        users_data = json.load(users_file)
    return render_template("html/list.html", users=users_data)

@app.route("/disable")
def view_disable():
    with open('file.json', 'r') as users_file:
        users_file = json.load(users_file)
    return render_template("html/disable.html", users=users_file)

@app.route("/disable-user", methods=['POST'])
def disable_user():
    fullname = request.json.get('fullname')  
    with open('file.json', 'r') as users_file:
        users_data = json.load(users_file)
    for user in users_data:
        if user["fullname"] == fullname:
            user["active"] = False
    with open('file.json', 'w') as users_file:
        json.dump(users_data, users_file, indent=4)
    return jsonify(success=True)

@app.route("/activate-user", methods=['POST'])
def activate_user():
    fullname = request.json.get('fullname')  
    with open('file.json', 'r') as users_file:
        users_data = json.load(users_file)
    for user in users_data:
        if user["fullname"] == fullname:
            user["active"] = True
    with open('file.json', 'w') as users_file:
        json.dump(users_data, users_file, indent=4)
    return jsonify(success=True)

# //rota de edição

@app.route("/edit", methods=['POST'])
def edit_users():
    return render_template("html/edit.html")

# @app.route("/edit/<string:fullname")
# def edit_user(fullname):
#     with open('file.json', 'r') as users_file:
#         users_data = json.load(users_file)   
#         return(render_template)("html/edit.html")


if __name__ == '__main__':
    app.run(debug=True)

