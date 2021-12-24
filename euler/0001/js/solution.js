console.log([...Array(1000).keys()].filter(function(idx, el) {
	return el % 3 == 0 || el % 5 == 0 ? el : null;
}).reduce((a, b) => a + b)); // still ridiculous in late 2018.
