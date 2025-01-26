const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      try {
        const lines = data.trim().split('\n');
        const students = lines.slice(1); // Ignorar la primera línea con los encabezados

        console.log(`Number of students: ${students.length}`);

        const fields = {};

        for (const line of students) {
          const [name, , , field] = line.split(',');

          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(name);
        }

        // Mostrar la cantidad de estudiantes por campo
        for (const field in fields) {
          const names = fields[field];
          console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }

        resolve();
      } catch (error) {
        reject(new Error('Cannot process the database'));
      }
    });
  });
}

module.exports = countStudents;
