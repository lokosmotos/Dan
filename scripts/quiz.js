function startQuiz(topic) {
    let questions = [];
    let subjectName = "";
    
    // Islamic Studies Quizzes
    if (topic === 'islamic1') {
        subjectName = "Surah An-Nas";
        questions = [
            {
                question: "Surah An-Nas is the ___ surah in the Quran?",
                options: ["First", "Middle", "Last"],
                answer: 2
            },
            {
                question: "What do we seek in Surah An-Nas?",
                options: ["Money", "Protection from evil", "Good grades"],
                answer: 1
            }
        ];
    }
    else if (topic === 'islamic2') {
        subjectName = "20 Sifat Allah";
        questions = [
            {
                question: "What does 'Wujud' mean?",
                options: ["Allah knows everything", "Allah exists", "Allah is powerful"],
                answer: 1
            }
        ];
    }
    
    // Other subjects can be added similarly...
    
    let score = 0;
    alert(`Starting ${subjectName} quiz!`);
    
    questions.forEach((q, i) => {
        const userAnswer = prompt(
            `Question ${i+1}: ${q.question}\n\n${
                q.options.map((opt, idx) => `${idx+1}. ${opt}`).join('\n')
            }`
        );
        
        if (parseInt(userAnswer) - 1 === q.answer) {
            score++;
            alert("Correct! 🎉");
        } else {
            alert(`Good try! The answer is: ${q.options[q.answer]}`);
        }
    });
    
    const percentage = Math.round((score / questions.length) * 100);
    alert(`Quiz complete!\nYou scored ${score}/${questions.length} (${percentage}%)`);
    
    if (percentage >= 80) {
        alert("Excellent work! 🌟");
    } else if (percentage >= 50) {
        alert("Good job! Keep practicing!");
    } else {
        alert("Let's review this topic again!");
    }
}
