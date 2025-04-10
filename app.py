from flask import Flask
import os
from datetime import datetime, timedelta
import subprocess
import getpass

app = Flask(__name__)

@app.route("/htop")
def htop():
    name= "Ankith K"  # Your name
    username = getpass.getuser()

    # Get IST time
    utc_time = datetime.utcnow()
    ist_time = utc_time + timedelta(hours=5, minutes=30)

    try:
        # Use ps instead of top
        process_output = subprocess.getoutput("ps aux")
    except OSError as e:
        process_output = f"Error occurred while fetching process data: {e}"

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h2>
    <pre>{process_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
