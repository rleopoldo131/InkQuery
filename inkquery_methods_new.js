import axios from 'axios';

// Function to fetch a word's definition from a selected dictionary
function fetchWordDefinition(word, dictType = "wb-i") {
    let url = '';
    let data;
    const wb_intermediate_key = "a19c9426-51cf-4c68-af55-de3b8229f559"; // intermediate key
    const wb_elementary_key = "e59d86cd-4e68-4ffc-a389-9945b19a1f32"; // elemantary key
    const wb_spanish_key = "a29aabe7-82a8-4c85-8e27-3b0bb0d722d8"; // Spanish Key


    if (dictType === 'wb-i' || dictType === null) {
        url = `https://dictionaryapi.com/api/v3/references/sd3/json/${word}?key=${wb_intermediate_key}`;
    }
    else if (dictType === 'wb-e') {
        url = `https://dictionaryapi.com/api/v3/references/sd2/json/${word}?key=${wb_elementary_key}`;

    }
    else if (dictType === 'wb-s') {
        url = `https://dictionaryapi.com/api/v3/references/spanish/json/${word}?key=${wb_spanish_key}`;
    }
        //Input last dictionary here
        //else if (dictionary === '') {
    //url = ``;
    else {
        console.error('Invalid dictionary selection. Choose either "wb-i", "wb-e", or "wb-s."');  //add last dictionary
        return;
    }

    console.log(`\nFetching definition from ${dictType}: ${url}`);

    data = axios.get(url).then(response => response.data);
    return data;
}


export function displayWordDef(word, dictType) {
    fetchWordDefinition(word, dictType)
        .then(data => {
            //Returns the very first result (most popular)
            console.log("| | |\n| | |\nV V V");
            //Converts wordID into the actual word
            let word = data[0].meta.id.split(":")[0];
            //Capitalizes first letter
            word = word.charAt(0).toUpperCase() + word.slice(1);
            let wordDef = data[0].shortdef[0]
            wordDef = wordDef.charAt(0).toUpperCase() + wordDef.slice(1) + '.';
            //Prints the following:
            //Word, Type (noun, verb, adj, etc)
            console.log(`\nYour Word: ${word}, (${data[0].fl})\n`);
            //Definition(s)
            console.log("Definitions:\n");
            console.log(wordDef, "\n");
        })
        .catch(err => console.log(err))
}
