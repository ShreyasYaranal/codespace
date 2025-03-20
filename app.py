from flask import Flask, render_template_string
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the Flask Application!</h1><p>Visit <a href='/htop'>/htop</a> to see system info.</p>"

@app.route('/htop', methods=['GET'])
def htop():
    # Set the name and username as specified
    full_name = "Shreyas"
    username = "shreyasyaranal"

    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Simulating top output using ps command
    try:
        top_output = subprocess.check_output(['ps', '-eo', 'pid,comm,%cpu,%mem'])
        top_output = top_output.decode('utf-8').splitlines()
    except Exception as e:
        top_output = [f"Error: {str(e)}"]

    # Rendering the output in HTML format
    html_output = f"""
    <html>
        <head>
            <title>System Info</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #f0f0f0; padding: 20px; }}
                h1 {{ color: #333; }}
                h2 {{ color: #555; }}
                pre {{ background: #eee; padding: 10px; border-radius: 5px; }}
                strong {{ color: #000; }}
            </style>
        </head>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {full_name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h2>Top Output</h2>
            <pre>{'\n'.join(top_output)}</pre>
        </body>
    </html>
    """

    return render_template_string(html_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)