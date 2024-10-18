
var mile = 0;
const maxMile = 6;
while (mile <= maxMile) {
  mile++;
  if (mile % 2 === 0 && mile <= maxMile) {
    console.log(` Pop out a piece of candy!`);
  }
}