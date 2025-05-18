function startQuiz(topic) {
    let questions = [];
    
    if (topic === 'science1') {
        questions = [
            {
                question: "Which sense organ do we use to see?",
                options: ["Ears", "Eyes", "Nose", "Tongue"],
                answer: 1
            },
            {
                question: "Can a rock grow and reproduce?",
                options: ["Yes", "No"],
                answer: 1
            }
        ];
    } else if (topic === 'science2') {
        questions = [
            {
                question: "Should you run in the science room?",
                options: ["Yes", "No"],
                answer: 1
            },
            {
                question: "What should you wear during experiments?",
                options: ["Lab coat", "Swimsuit", "Pajamas"],
                answer: 0
            }
        ];
    }
    
    let score = 0;
    
    questions.forEach((q, i) => {
        const userAnswer = prompt(
            `Question ${i+1}: ${q.question}\n\n${
                q.options.map((opt, idx) => `${idx+1}. ${opt}`).join('\n')
            }`
        );
        
        if (parseInt(userAnswer) - 1 === q.answer) {
            score++;
            alert("Correct! 👍");
        } else {
            alert(`Oops! The correct answer is ${q.options[q.answer]}`);
        }
    });
    
    alert(`Quiz complete! You scored ${score}/${questions.length}`);
}
