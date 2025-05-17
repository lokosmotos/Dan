from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import logging
from data.questions import practice_questions
from data.planner import planner_data

# Initialize Flask app
app = Flask(__name__, static_folder='../frontend/public')
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Verify static folder and index.html exist
static_folder_path = os.path.abspath(app.static_folder)
index_path = os.path.join(static_folder_path, 'index.html')

if not os.path.exists(static_folder_path):
    logger.error(f"Static folder not found at: {static_folder_path}")
    raise FileNotFoundError(f"Static folder missing: {static_folder_path}")
    
if not os.path.exists(index_path):
    logger.error(f"index.html not found at: {index_path}")
    raise FileNotFoundError(f"index.html missing: {index_path}")

logger.info(f"Static files served from: {static_folder_path}")
logger.info(f"Found index.html at: {index_path}")

# In-memory storage for completed tasks
completed_tasks = {}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    try:
        file_path = os.path.join(app.static_folder, path)
        if path and os.path.exists(file_path) and not os.path.isdir(file_path):
            logger.info(f"Serving static file: {file_path}")
            return send_from_directory(app.static_folder, path)
        logger.info(f"Serving index.html for path: {path}")
        return send_from_directory(app.static_folder, 'index.html')
    except Exception as e:
        logger.error(f"Error serving {path}: {str(e)}")
        return jsonify({
            "error": "Failed to serve file",
            "path": path,
            "details": str(e)
        }), 500

@app.route('/api/questions')
def get_questions():
    logger.info("Serving practice questions")
    return jsonify(practice_questions)

@app.route('/api/planner')
def get_planner():
    logger.info("Serving planner data")
    return jsonify(planner_data)

@app.route('/api/complete-task', methods=['POST'])
def complete_task():
    try:
        data = request.get_json()
        task_index = data.get('index')
        
        if task_index is None:
            logger.warning("Complete task request missing index")
            return jsonify({"error": "Index is required"}), 400
            
        logger.info(f"Marking task {task_index} as complete")
        completed_tasks[task_index] = True
        return jsonify({"status": "success", "index": task_index})
    except Exception as e:
        logger.error(f"Error completing task: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/completed-tasks')
def get_completed_tasks():
    logger.info("Serving completed tasks")
    return jsonify(completed_tasks)

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(host='0.0.0.0', port=5000, debug=True)