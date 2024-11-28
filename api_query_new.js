import wm_getDef from "./inkquery_methods_new.js"


document.getElementById("wordButton").onclick = async function() {

    const intermediateBtn = document.getElementById("intermediateBtn");
    const elementaryBtn = document.getElementById("elementaryBtn");
    const collegiateBtn = document.getElementById("collegiateBtn");
    const spanishBtn = document.getElementById("spanishBtn");

    let checkedBtnInput = "intermediate";

    if (intermediateBtn.checked){
        checkedBtnInput = "intermediate";
    }
    else if (elementaryBtn.checked){
        checkedBtnInput = "elementary";
    }
    else if (collegiateBtn.checked){
        checkedBtnInput = "collegiate";
    }
    else if (spanishBtn.checked){
        checkedBtnInput = "spanish";
    }

    console.log(checkedBtnInput);

    const wordLabel = document.getElementById("wordIn").value;
    document.getElementById("yourWordLabel").textContent = wordLabel;

    try {
        const wordDef = await wm_getDef(wordLabel, checkedBtnInput);
        document.getElementById("defLabel").textContent = wordDef;
        console.log(wordDef);
    }
    catch(error) {
        console.error("Error fetching definition", error);
        document.getElementById("defLabel").textContent = "Error displaying definition.";
    }
}



