const http = require('http');

const app = http.createServer((req, res) => {

    res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
});

app.listen(1245, () => {
  console.log('Server is running on http://localhost:1245');
});

module.exports = app;
