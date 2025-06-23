from flask import flask, render_template, request, jsonify
import time

app = flask(__name__)

# Log to store task names and their start and stop times
task_log = []   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_time', methods=['POST'])
def log_time():
    # Get the task start and stop times from the request
    start_time = request.json.get('start_time')
    end_time = request.json.get('end_time')
    
    # Calculate duration in seconds
    duration = end_time - start_time
    task_log.append({
        'start_time': start_time,
        'end_time': end_time,
        'duration': duration
    })
    
    return jsonify({"message": "Time logged successfully", "duration": duration})

@app.route('/get_log', methods=['GET'])
def get_log():
    return jsonify(task_log)

if __name__ == '__main__':
    app.run(debug=True)
