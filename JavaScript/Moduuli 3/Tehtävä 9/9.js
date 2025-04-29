document.getElementById("start").addEventListener("click", function () {
  let result;
  const input = document.getElementById("calculation").value;

  let operator;
  if (input.includes("+")) {
    operator = "+";
  } else if (input.includes("-")) {
    operator = "-";
  } else if (input.includes("*")) {
    operator = "*";
  } else if (input.includes("/")) {
    operator = "/";
  }
  if (!operator) {
    result = "Error";

  } else {
    const numbers = input.split(operator);

    if (numbers.length !== 2) {
      result = "Error";
    } else {
      const num1 = parseFloat(numbers[0]);
      const num2 = parseFloat(numbers[1]);

      switch (operator) {
        case "+":
          result = num1 + num2;
          break;
        case "-":
          result = num1 - num2;
          break;
        case "*":
          result = num1 * num2;
          break;
        case "/":
            if (num2 === 0 || num1 === 0) {
              result = "Cannot divide by zero!";
            } else {
              result = num1 / num2;
            }
            break;
          default:
            result = "Invalid operation.";
        }
    }
  }

  document.getElementById("result").innerHTML = result;
});