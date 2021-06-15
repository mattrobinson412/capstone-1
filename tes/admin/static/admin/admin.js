/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    var x = document.getElementById("nav");
    if (x.className === "nav") {
      x.className += " responsive";
    } else {
      x.className = "nav";
    }
  }

// let inquiryBox = document.querySelector("#inquiry")
// let closedSection = document.querySelector(".handled");
// let openSection = document.querySelector(".open");
 
// const closeTodo = openSection.addEventListener("click", function(e) {
//   if (e.target.tagName === 'BUTTON') {
//     e.preventDefault();
  
//     let target = e.target.parentElement;
//     console.log(target);

//     closedSection.appendChild(target);
//     target.setAttribute("class", "closed")
//     console.log(closedSection);
//   }
// });

// const OpenTodo = closedSection.addEventListener("click", function(e) {
//   if (e.target.tagName === 'BUTTON') {
//     e.preventDefault();

//     let target = e.target.parentElement;
//     console.log(target);

//     openSection.appendChild(target);
//     target.removeAttribute("class");
//     target.setAttribute("class", "border");
//     console.log(openSection);
//   }
// });

// const open = localStorage.setItem("open", "border");
// const closed = localStorage.setItem("closed","closed");

// let openInq = document.querySelectorAll(".border");
// let closedInq = document.querySelectorAll(".closed");

// // run these lines of code when page loads! //
// const getOpen = localStorage.getItem("open");
// const getClosed = localStorage.getItem("closed");

// openInq.forEach(inq => {
//   inq.setAttribute("class", getOpen);
//   return inq;
// })

// closedInq.forEach(inq => {
//   inq.setAttribute("class", closed);
//   return inq;
// })