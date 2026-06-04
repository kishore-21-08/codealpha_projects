function correctAnswer(){

    document.getElementById("result").innerHTML =
    "✅ Correct! Never trust unknown email links.";

}

function wrongAnswer(){

    document.getElementById("result").innerHTML =
    "❌ Incorrect! Unknown links may contain phishing attacks.";

}

function showAlert(){

    alert(
        "Phishing awareness helps protect users from cyberattacks."
    );

}
