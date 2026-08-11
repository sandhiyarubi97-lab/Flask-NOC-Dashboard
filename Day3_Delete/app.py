from flask import Flask, render_template, request, redirect

app = Flask(__name__)

servers = [
    {"id": 1, "name": "Web Server", "status": "UP", "CPU": "45%"},
    {"id": 2, "name": "Database Server", "status": "UP", "CPU": "70%"},
    {"id": 3, "name": "Backup Server", "status": "DOWN", "CPU": "0%"}
]
next_id = 4


@app.route("/", methods=["GET", "POST"])
def dashboard():
    global next_id
    if request.method == "POST":
        new_name = request.form["server_name"]
        new_status = request.form["server_status"]
        servers.append({"id": next_id, "name": new_name, "status": new_status, "CPU": "0%"})
        next_id += 1
        return redirect("/")
    return render_template('dashboard.html', servers=servers)


@app.route("/delete/<int:server_id>")
def delete_server(server_id):
    global servers
    servers = [s for s in servers if s["id"] != server_id]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

