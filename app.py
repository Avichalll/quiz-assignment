from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__) 
@app.route('/htop')
def htop():
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown_user"
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    try:
            htop_output = subprocess.check_output(
            ["top", "-b", "-n", "1"],
            universal_newlines=True
        )  
    except Exception as e:
        htop_output = f"Error fetching process information: {str(e)}"
    response = f"""
    <html>
        <head><title>HTOP Output</title></head>
        <body>
            <h2>Name: Avichal Kumar</h2>
            <h3>Username: {username}</h3>
            <h3>Server Time (IST): {server_time}</h3>
            <h3>Process List:</h3>
            <pre>{htop_output}</pre>
        </body>
    </html>
    """
    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)