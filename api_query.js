console.log('Happy developing ✨')

// Access command line arguments
const args = process.argv.slice(2); // Skip the first two elements

// args will now contain only the arguments passed to the script
console.log('Command line arguments:', args);

// Example usage
if (args.length > 0) {
    console.log(`The first argument is: ${args[0]}`);
} else {
    console.log('No arguments provided.');
}

