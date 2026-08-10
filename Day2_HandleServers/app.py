from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#This is the database for now - just a a list

servers = [
    {"name": "Web Server", "status": "UP", "CPU": "45%"},
    {"name": "Database Server", "server": "Up", "CPU": "70%"},
    {"name": "Backup Server", "server": "DOWN", "CPU": "0%"}
]


@app.route("/", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        new_name = request.form["server_name"]    #Get data from the form
        new_status = request.form["server_status"]
        servers.append({"name": new_name, "status": new_status, "CPU": "0%"})
        return redirect("/")

    return render_template('dashboard.html', servers=servers)

if __name__ == "__main__":
    app.run(debug=True)
