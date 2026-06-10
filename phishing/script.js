// script.js

const analyzeBtn = document.getElementById("analyzeBtn");
const resultBox = document.getElementById("resultBox");

analyzeBtn.addEventListener("click", () => {

  resultBox.innerHTML = `
    ⚠️ PHISHING DETECTED<br><br>

    Indicators Found:
    <br>• Fake domain name
    <br>• Urgent language
    <br>• Suspicious verification link
    <br>• Social engineering attempt
  `;
});

const options = document.querySelectorAll(".option");
const quizResult = document.getElementById("quizResult");

options.forEach(option => {

  option.addEventListener("click", () => {

    if(option.innerText.includes("Urgent")){
      quizResult.innerHTML =
        "✅ Correct! Urgency and suspicious links are common phishing signs.";
      quizResult.style.color = "#00ff99";
    }

    else{
      quizResult.innerHTML =
        "❌ Incorrect. Try again.";
      quizResult.style.color = "#ff4d6d";
    }

  });

});
