process.stdout.write("Welcome to Holberton School, what is your name?");

process.stdin.on('data', (data) => {
    const name = data.toString().trim();
    const message = `\nYour name is: ${name}\n`

    process.stdout.write(message);

    
    process.stdout.write("This important software is now closing\n");
    process.exit();
});
