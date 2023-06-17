// Import necessary libraries
const express = require('express');

// Create an express app
const app = express();

// Define a route
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Start the server
app.listen(3000, () => {
  console.log('App listening on port 3000!');
});
