from flask import Flask, render_template

app = Flask(__name__)

# Sample data
devices = [
    {"group": "Prince 6th Floor", "hostname": "N-INEPRINCE-AP01", "ip": "10.192.160.10", "status": "Active"},
    {"group": "Prince 6th Floor", "hostname": "N-INEPRINCE-AP02", "ip": "10.192.160.11", "status": "Active"},
    {"group": "Prince 6th Floor", "hostname": "N-INEPRINCE-AP03", "ip": "10.192.160.12", "status": "Active"},
    {"group": "Prince 6th Floor", "hostname": "N-INEPRINCE-AP04", "ip": "10.192.160.13", "status": "Active"},
    {"group": "Prince 6th Floor", "hostname": "N-INEPRINCE-AP05", "ip": "10.192.160.14", "status": "Inactive"},
    {"group": "Prince 6th Floor", "hostname": "N-INEPRINCE-AP06", "ip": "10.192.160.15", "status": "Active"},
    {"group": "Prince 6th Floor", "hostname": "N-INEPRINCE-AP07", "ip": "10.192.160.16", "status": "Active"},
    {"group": "Prince 6th Floor", "hostname": "N-INEPRINCE-AP08", "ip": "10.192.160.17", "status": "Inactive"},
    {"group": "Prince 6th Floor", "hostname": "N-INEPRINCE-AP09", "ip": "10.192.160.19", "status": "Active"},
    {"group": "Prince 6th Floor", "hostname": "N-INEPRINCE-AP10", "ip": "10.192.160.18", "status": "Inactive"},
    {"group": "Prince 6th Floor", "hostname": "N-INEPRINCE-AP11", "ip": "10.192.160.20", "status": "Active"},
    {"group": "Prince 6th Floor", "hostname": "N-INEPRINCE-AP12", "ip": "10.192.160.21", "status": "Active"},
    # Add more devices as needed
]

@app.route('/')
def index():
    return render_template('index.html', devices=devices)

if __name__ == '__main__':
    app.run(debug=True)
