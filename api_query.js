
const { displayWord } = require('./inkquery_methods.js');


// user input
let word;
let dictType;

word = process.argv[2];

if (process.argv.length > 3) {
    dictType = process.argv[3];
}

if (!word) {
    // console.error('Please provide a word and a dictionary. "wb-i", "wb-e", or "wb-s)"');//add last dictionary
    console.error('Please provide a word.')
    process.exit(1);
}


displayWord(word, dictType);