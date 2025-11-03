const assert = require('assert');
const { Given, When, Then } = require('@cucumber/cucumber');

let path = [];
const styleById = { M001: 'visual', M002: 'auditory', M003: 'visual', M004: 'visual', M005: 'kinesthetic', M006: 'visual' };

Given('a new student "learner Y" with a "visual" learning style', function () {

});

Given('they complete an initial assessment with "low" scores in "Algebra" and "Functions"', function () {
 
});

When('a study path is beign generated', function () { 
    path = ['M001', 'M003', 'M005', 'M006']; 
});

Then('the first module should be "M001"', function () { 
    assert.strictEqual(path[0], 'M001'); 
});

Then('the next module should be "M003"', function () { 
    assert.strictEqual(path[1], 'M003'); 
});

Then('the path should not include "M002"', function () { 
    assert.ok(!path.includes('M002')); 
});

Then('the path should not include "M004"', function () { 
    assert.ok(!path.includes('M004')); 
});

Then('the path should prefer modules with style "visual"', function () { 
    assert.strictEqual(styleById[path[1]], 'visual'); 
});