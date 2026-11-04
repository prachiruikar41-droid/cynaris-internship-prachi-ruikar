// Day 3: JavaScript ES6+ Basics

// 1. Arrow Function
const greet = (name) => {
    return `Hello, ${name}! Welcome to Cynaris Internship.`;
};

console.log(greet("Prachi"));

// 2. Array Destructuring
const technologies = ["HTML", "CSS", "JavaScript"];
const [first, second, third] = technologies;

console.log(first, second, third);

// 3. Object Destructuring
const intern = {
    name: "Prachi",
    role: "Full Stack Development Intern",
    company: "Cynaris Solutions"
};

const { name, role, company } = intern;

console.log(`${name} is a ${role} at ${company}.`);

// 4. Array Methods: filter(), map(), reduce()
const numbers = [10, 20, 30, 40, 50];

const filteredNumbers = numbers.filter(num => num > 20);
const doubledNumbers = numbers.map(num => num * 2);
const total = numbers.reduce((sum, num) => sum + num, 0);

console.log("Filtered:", filteredNumbers);
console.log("Doubled:", doubledNumbers);
console.log("Total:", total);

// 5. Interactive Component using Event Listener
const button = document.getElementById("welcomeButton");
const message = document.getElementById("welcomeMessage");

if (button && message) {
    button.addEventListener("click", () => {
        message.textContent = "Welcome! JavaScript ES6+ is working successfully.";
    });
}