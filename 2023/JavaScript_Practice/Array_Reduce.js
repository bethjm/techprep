// array.reduce()
//reduce an array to a single value

let prices = [5, 10, 15, 20, 25];
let total = prices.reduce(checkOut);

console.log(`the total is ${total}`);

function checkOut(total, element) {
  return total + element;
}
