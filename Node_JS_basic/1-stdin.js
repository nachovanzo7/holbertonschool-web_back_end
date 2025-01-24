process.stdout.write("Welcome to Holberton School, what is your name?");

process.stdin.on('data', (data) => {
    const name = data.toString().trim();
    const message = `Your name is: ${name}\n`

    process.stdout.write('\n' + message);

    
    process.stdout.write("This important software is now closing");
    process.exit();
});
