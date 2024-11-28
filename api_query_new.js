import wm_getDef from "./inkquery_methods_new.js"


let wordDef;
let wordLabel;
document.getElementById("wordButton").onclick = async function() {
    wordLabel = document.getElementById("wordIn").value;
    document.getElementById("yourWordLabel").textContent = wordLabel;

    try {
        wordDef = await wm_getDef(wordLabel);
        document.getElementById("defLabel").textContent = wordDef;
        console.log(wordDef);
    }
    catch(error) {
        console.error("Error fetching definition", error);
    }
}



