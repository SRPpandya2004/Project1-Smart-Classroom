
// Wait for the DOM to load before executing the code.
document.addEventListener("DOMContentLoaded", function () {
  // Initialize Flatpickr if the date input exists
  var dobElem = document.getElementById("dob");
  if (dobElem) {
    flatpickr(dobElem, {
      dateFormat: "Y-m-d",
      maxDate: "today"
    });
  } else {
    console.warn("Date field with id 'dob' not found.");
  }

  // Attach event listener to the registration form if it exists
  var regForm = document.getElementById("studentRegistrationForm");
  if (regForm) {
    regForm.addEventListener("submit", function (e) {
      e.preventDefault();
      // Collect registration form data only if the fields exist
      var userData = {
        name: document.getElementById("name") ? document.getElementById("name").value : "",
        gender: document.getElementById("gender") ? document.getElementById("gender").value : "",
        dob: document.getElementById("dob") ? document.getElementById("dob").value : "",
        enrollment: document.getElementById("enrollment") ? document.getElementById("enrollment").value : "",
        mobile: document.getElementById("mobile") ? document.getElementById("mobile").value : "",
        email: document.getElementById("email") ? document.getElementById("email").value : "",
        password: document.getElementById("password") ? document.getElementById("password").value : ""
      };
      console.log("Registration Data:", userData);
      alert("Registration successful!");
      // Optionally, add redirection logic here
      // window.location.href = "student_signin.html";
    });
  } else {
    console.info("Registration form with id 'studentRegistrationForm' not found on this page.");
  }

  // Attach event listener to the login form if it exists
  var loginForm = document.getElementById("studentLoginForm");
  if (loginForm) {
    loginForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var loginData = {
        username: document.getElementById("username") ? document.getElementById("username").value : "",
        password: document.getElementById("password") ? document.getElementById("password").value : ""
      };
      console.log("Login Data:", loginData);
      alert("Login successful!");
      // Optionally, add redirection logic here
      // window.location.href = "dashboard.html";
    });
  } else {
    console.info("Login form with id 'studentLoginForm' not found on this page.");
  }
});
