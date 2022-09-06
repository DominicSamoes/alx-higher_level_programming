#!/usr/bin/node
const fc = require('fs');
const a = fc.readFileSync(process.argv[2], 'utf8');
const b = fc.readFileSync(process.argv[3], 'utf8');
fc.writeFileSync(process.argv[4], a + b);
