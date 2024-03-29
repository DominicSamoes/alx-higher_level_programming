#!/usr/bin/node

const args = process.argv;
let reqURL = args[2];
let request = require('request');
request(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    let todos = JSON.parse(body);
    let dash = {};
    for (let c = 0; c < todos.length; c++) {
      let status = (todos[i]['completed']);
      let key = todos[c]['userId'].toString();
      if (status) {
        if (dash[key]) {
          dash[key]++;
        } else {
          dash[key] = 1;
        }
      }
    }
    console.log(dash);
  }
});
