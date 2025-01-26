const express = require('express');
const fs = require('fs');

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

const app = express();

app.get('/', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  const databasePath = process.argv[2];

  if (!databasePath) {
    res.send('This is the list of our students\nCannot load the database');
    return;
  }

  try {
    const result = await countStudents(databasePath);
    res.send(`This is the list of our students\n${result}`);
  } catch (err) {
    res.send(`This is the list of our students\n${err.message}`);
  }
});

app.listen(1245, () => {
  console.log('Server running on http://localhost:1245');
});

module.exports = app;
