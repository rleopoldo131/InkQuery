
// Access command line arguments
const word = process.argv.slice(2); // Skip the first two elements

// args will now contain only the arguments passed to the script
console.log('Word to search:', word[0]);

const axios = require('axios');

const wb_intermediate_key = "a19c9426-51cf-4c68-af55-de3b8229f559";
const url = `https://dictionaryapi.com/api/v3/references/sd3/json/test?key=${wb_intermediate_key}`;

console.log(url)

axios.get(url)
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.error('Error fetching the definition:', error);
    });



