const fs = require('fs').promises;

async function countStudents(path) {
    try {
        const data = await fs.readFile(path, 'utf8');
        
        const lines = data.trim().split('\n');

        const students = lines.slice(1).filter(line => line.trim() !== ''); // Ignorar la primera línea (cabecera)

        const totalStudents = students.length;

        console.log(`Number of students: ${totalStudents}`);

        const fields = {};

        students.forEach((student) => {
            const [firstname, field] = student.split(',');
            if (fields[field]) {
                fields[field].push(firstname);
            } else {
                fields[field] = [firstname];
            }
        });

        for (const field in fields) {
            console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
        }
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
