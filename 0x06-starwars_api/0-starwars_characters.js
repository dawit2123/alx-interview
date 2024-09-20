#!/usr/bin/node

const request = require("request");

// Function to handle recursive requests
const req = (arr, i) => {
  if (i === arr.length) return; // Base case: If index i is equal to the length of array, stop recursion

  request(arr[i], (err, response, body) => {
    if (err) {
      console.error(err); // Use console.error for proper error logging
      return;
    }
    // Parse and print the character name
    try {
      const character = JSON.parse(body).name;
      console.log(character);
    } catch (parseError) {
      console.error("Failed to parse character data:", parseError);
    }
    // Recursive call to process the next character
    req(arr, i + 1);
  });
};

// Main request to fetch movie data
request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, // Movie ID passed as argument
  (err, response, body) => {
    if (err) {
      console.error(err); // Log any errors that occur
      return;
    }

    // Parse the body of the movie response
    try {
      const movieData = JSON.parse(body);
      const characters = movieData.characters; // Extract the characters list from the movie data
      req(characters, 0); // Start recursive requests to fetch character names
    } catch (parseError) {
      console.error("Failed to parse movie data:", parseError); // Catch JSON parsing errors
    }
  }
);
