document.getElementById("start").addEventListener("click", function () {
  const operation = document.getElementById("operation").value
  const num1 = parseFloat(document.getElementById("num1").value);
  const num2 = parseFloat(document.getElementById("num2").value);

  let result;

  switch (operation) {
          case "add":
            result = num1 + num2;
            break;
          case "sub":
            result = num1 - num2;
            break;
          case "multi":
            result = num1 * num2;
            break;
          case "div":
            if (num2 === 0 || num1 === 0) {
              result = "Cannot divide by zero!";
            } else {
              result = num1 / num2;
            }
            break;
          default:
            result = "Invalid operation.";
        }
  document.getElementById("result").innerHTML = result;
})