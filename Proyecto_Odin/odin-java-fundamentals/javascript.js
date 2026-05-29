const frase = "Camino antes que destino!";
console.log(frase)

const name = "Ángel";
const greeting = `Hello, ${name}, nice to meet you!`; // Aquí si es importante usar estas comillas de mierda
console.log(greeting);

const one = "Hello, ";
const two = "how are you?";
const joined = `${one}${name}, ${two}`;
console.log(joined); 

console.log(one + name + ", " + two);

const nuevafrase = "Algún día me hartare\nde tanto hacer cosasa raras";
console.log(nuevafrase);

const song = "Hablando en plata";
const score = 8;
const highestscore = 10;
const outpot = `Me gusta la canción ${song}. Le daría una puntación de ${(score/highestscore) * 100}%.`;
console.log(outpot);

const myString = "123";
const myNum = Number(myString);
console.log(typeof myNum);

const myNum2 = "123";
const myString2 = String(myNum2);
console.log(typeof myString2);