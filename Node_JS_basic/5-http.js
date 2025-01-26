const http = require('http');
const fs = require('fs');
const path = require('path');

const countStudents = (databasePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(databasePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const headers = lines.shift().split(',');
      const students = lines.map((line) => line.split(','));
      const fields = {};

      students.forEach((student) => {
        const field = student[headers.indexOf('field')].trim();
        const name = student[headers.indexOf('firstname')].trim();

        if (field && name) {
          if (!fields[field]) fields[field] = [];
          fields[field].push(name);
        }
      });

      let result = `Number of students: ${students.length}\n`;
      for (const [field, names] of Object.entries(fields)) {
        result += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      }

      resolve(result.trim());
    });
  });
};

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.setHeader('Content-Type', 'text/plain');
    const databasePath = process.argv[2];

    if (!databasePath) {
      res.end('This is the list of our students\nCannot load the database');
      return;
    }

    try {
      const result = await countStudents(databasePath);
      res.end(`This is the list of our students\n${result}`);
    } catch (err) {
      res.end(`This is the list of our students\n${err.message}`);
    }
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server running on http://localhost:1245');
});

module.exports = app;
