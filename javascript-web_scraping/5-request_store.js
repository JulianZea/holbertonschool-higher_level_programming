#!/usr/bin/node
const fs = require('fs'); 
const request = require('request'); // Import the request module to make HTTP requests

const url = process.argv[2]; // The URL to request, passed as the first command line argument
const filename = process.argv[3]; // The name of the file to write, passed as the second command line argument

// Make an HTTP request to the specified URL and save the response body to a variable
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Write the response body to a file using UTF-8 encoding
    fs.writeFile(filename, body, 'utf8', (error) => {
      if (error) {
        console.error(error);
      } else {
        console.log(`Response body saved to ${filename}`);
      }
    });
  }
});
