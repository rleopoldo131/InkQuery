
// // Access command line arguments
// const word = process.argv.slice(2)[0]; // Skip the first two elements

// // args will now contain only the arguments passed to the script
// console.log('Word to search:', word);

// const axios = require('axios');

// const wb_intermediate_key = "a19c9426-51cf-4c68-af55-de3b8229f559";
// const url = `https://dictionaryapi.com/api/v3/references/sd3/json/${word}?key=${wb_intermediate_key}`;

// console.log(url)

// axios.get(url)
//     .then(response => {
//         console.log(response.data);
//     })
//     .catch(error => {
//         console.error('Error fetching the definition:', error);
//     });


const axios = require('axios');

// Function to fetch a word's definition from a selected dictionary
function fetchWordDefinition(word, dictionary) {
    let url = '';
    const wb_intermediate_key = "a19c9426-51cf-4c68-af55-de3b8229f559"; // intermediate key
    const wb_elemantary_key = "e59d86cd-4e68-4ffc-a389-9945b19a1f32"; // elemantary key
    const wb_spanish_key = "a29aabe7-82a8-4c85-8e27-3b0bb0d722d8"; // Spanish Key
    

    if (dictionary === 'webster-intermediate') {
        url = `https://dictionaryapi.com/api/v3/references/sd3/json/${word}?key=${wb_intermediate_key}`;
    } 
    else if (dictionary === 'webster-elemantary') {
        url = `https://dictionaryapi.com/api/v3/references/sd2/json/${word}?key=${wb_elemantary_key}`;
    
    } 
    else if (dictionary === 'webster-spanish') {
        url = `https://dictionaryapi.com/api/v3/references/spanish/json/${word}?key=${wb_spanish_key}`;
    }
    else {
        console.error('Invalid dictionary selection. Choose either "webster-intermediate, webster-elemantary, or webster-spanish."');
        return;
    }

    console.log(`Word to search: ${word}`);
    console.log(`Fetching definition from ${dictionary}: ${url}`);

    axios.get(url)
        .then(response => {
            if (response.data.length === 0) {
                console.log(`No definitions found for: ${word}`);
            } else {
                console.log(`Definition from ${dictionary}:`, response.data);
            }
        })
        .catch(error => {
            console.error(`Error fetching the definition from ${dictionary}:`, error);
        });
}

// user input
const word = process.argv[2];
const dictionary = process.argv[3]; 

if (!word || !dictionary) {
    console.error('Please provide a word and a dictionary ("webster-intermediate, webster-elemantary, or webster-spanish.)"');
    process.exit(1); 
}

fetchWordDefinition(word, dictionary);