from flask import Flask, jsonify, request, send_file
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='.')

# Verify index.html file
index_path = os.path.join(app.static_folder, 'index.html')
if not os.path.exists(index_path):
    logger.error(f"index.html not found at: {index_path}")
else:
    logger.info(f"index.html found at: {index_path}")

# Sample data
practice_questions = {
    "Bahasa Melayu": [
        {"question": "Write: buku, kucing, meja", "answer": "buku, kucing, meja"},
        {"question": "Describe your favorite animal in 3 sentences", "answer": "Example: Saya suka kucing. Kucing saya comel. Ia suka bermain bola."},
        {"question": "Name 3 Kata Nama Am", "answer": "pensil, rumah, pokok"},
        {"question": "Describe a ball (color, shape)", "answer": "Bola itu merah dan bulat."},
        {"question": "Penjodoh for buku", "answer": "buah"}
    ],
    "English": [
        {"question": "What day comes after Wednesday?", "answer": "Thursday"},
        {"question": "Correct: ali likes to play", "answer": "Ali likes to play."},
        {"question": "Name 3 free time activities", "answer": "Play football, read books, draw"},
        {"question": "Write a question about free time", "answer": "What do you do after school?"},
        {"question": "Is an apple healthy or unhealthy?", "answer": "Healthy"}
    ],
    "Pendidikan Islam": [
        {"question": "Recite first 2 verses of Surah An-Nas", "answer": "قُلْ أَعُوذُ بِرَبِّ النَّاسِ، مَلِكِ النَّاسِ"},
        {"question": "Find one mad asli in Surah An-Nas", "answer": "“nās”"},
        {"question": "Name 3 sifat wajib", "answer": "Wujud, Ilm, Qudrah"},
        {"question": "Du’a when entering toilet", "answer": "Bismillah, Allahumma inni a‘udhu..."},
        {"question": "Name one sign of Nabi Muhammad’s prophethood", "answer": "The Quran"}
    ]
}

planner_data = [
    {"date": "13/5", "subjects": ["Science: Sense Organs, Lab Rules", "Pendidikan Islam: Surah An-Nas, Istinjak"], "activities": ["Draw 5 sense organs", "Recite Surah An-Nas 5 times"]},
    {"date": "14/5", "subjects": ["Bahasa Melayu: Imlak, Kata Nama", "English: Days, Punctuation"], "activities": ["Write 10 dictated words", "Sing Days song"]},
    {"date": "15/5", "subjects": ["Matematik: Addition, Subtraction", "Pendidikan Islam: Sifat Allah, Jawi"], "activities": ["Solve 10 sums", "Write 5 Jawi suku kata"]},
    {"date": "16/5", "subjects": ["Science: Human", "Bahasa Melayu: Adjektif, Penjodoh"], "activities": ["Draw growth timeline", "Match 5 penjodoh"]},
    {"date": "17/5", "subjects": ["English: Activities, Questions", "Muzik: Singing, Tempo"], "activities": ["List 5 activities", "Sing Rasa Sayang"]},
    {"date": "18/5", "subjects": ["Pendidikan Islam: Sirah, Adab", "Seni Visual: Chosen Task"], "activities": ["Tell Nabi Muhammad story", "Practice drawing/craft"]},
    {"date": "19/5", "subjects": ["All Subjects: Revision"], "activities": ["Quiz 2 questions per subject"]}
]

completed_tasks = {}

@app.route('/')
def index():
    logger.info("Attempting to serve index.html")
    try:
        if not os.path.exists(index_path):
            logger.error(f"index.html not found at {index_path}")
            return jsonify({"error": "File missing", "path": index_path}), 500
        return send_file(index_path)
    except Exception as e:
        logger.error(f"Error serving index.html: {str(e)}")
        return jsonify({"error": "Failed to load page", "details": str(e)}), 500

@app.route('/api/questions', methods=['GET'])
def get_questions():
    logger.info("Fetching practice questions")
    return jsonify(practice_questions)

@app.route('/api/planner', methods=['GET'])
def get_planner():
    logger.info("Fetching planner data")
    return jsonify(planner_data)

@app.route('/api/complete-task', methods=['POST'])
def complete_task():
    logger.info("Processing task completion")
    try:
        data = request.json
        task_index = data.get('index')
        if task_index is None:
            logger.error("Invalid task index")
            return jsonify({"status": "error", "message": "Invalid index"}), 400
        completed_tasks[task_index] = True
        logger.info(f"Task {task_index} marked complete")
        return jsonify({"status": "success", "index": task_index})
    except Exception as e:
        logger.error(f"Error completing task: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/completed-tasks', methods=['GET'])
def get_completed_tasks():
    logger.info("Fetching completed tasks")
    return jsonify(completed_tasks)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)