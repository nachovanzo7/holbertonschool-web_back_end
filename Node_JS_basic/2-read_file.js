const fs = require('fs');

function countStudents(path) {
  try {
    // Leer el archivo y convertirlo a texto
    const fileContent = fs.readFileSync(path, 'utf8').trim();

    const lines = fileContent.split('\n');
    const students = lines.slice(1);

    console.log(`Number of students: ${students.length}`);

    const fields = {};

    for (const line of students) {
      const [name, , , field] = line.split(',');

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(name);
    }

    // Mostrar la cantidad de estudiantes
    for (const field in fields) {
      const names = fields[field];
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
