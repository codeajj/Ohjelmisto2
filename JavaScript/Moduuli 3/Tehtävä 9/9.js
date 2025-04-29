document.getElementById("start").addEventListener("click", function () {
  const input = document.getElementById("calculation").value;

  let result;
  let calculate;

  if (input.includes("+")) {
    calculate = "+";
  } else if (input.includes("-")) {
    calculate = "-";
  } else if (input.includes("*")) {
    calculate = "*";
  } else if (input.includes("/")) {
    calculate = "/";
  }
  if (!calculate) {
    result = "Error";

  } else {
    const numbers = input.split(calculate);

    if (numbers.length !== 2) {
      result = "Error";
    } else {
      const num1 = parseFloat(numbers[0]);
      const num2 = parseFloat(numbers[1]);

      switch (calculate) {
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
            result = "Invalid calculation.";
        }
    }
  }

  document.getElementById("result").innerHTML = result;
});