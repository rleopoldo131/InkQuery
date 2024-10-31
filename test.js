let wordLabel;

document.getElementById("wordButton").onclick = function() {
    wordLabel = document.getElementById("wordIn").value;
    document.getElementById("yourWordLabel").textContent = wordLabel;
}
