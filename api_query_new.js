// import React, { useState } from 'react';
// import {displayWordDef} from "./inkquery_methods_new.js";

let wordLabel;
document.getElementById("wordButton").onclick = function() {
    wordLabel = document.getElementById("wordIn").value;
    document.getElementById("yourWordLabel").textContent = wordLabel;
    // displayWordDef(wordLabel, dictType);
}



