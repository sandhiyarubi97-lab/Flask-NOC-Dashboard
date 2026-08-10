from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def dashboard():
    servers = [
        {"name": "Web Server 1", "status": "UP", "CPU": "45%"},
        {"name": "Database Server", "status": "UP", "CPU": "70%"},
        {"name": "Backup Server", "status": "DOWN", "CPU": "0%"},
        {"name": "Mail Server", "status": "UP", "CPU": "30%"}
    ]
    return render_template('dashboard.html', servers=servers)

if __name__ == "__main__":
    app.run(debug=True)




