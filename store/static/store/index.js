console.log("inside js file");
const openNav = document.querySelector(".open-btn");
const closeNav = document.querySelector(".close-btn");
const menu = document.querySelector(".nav-list");

const menuLeft = menu.getBoundingClientRect().left;
openNav.addEventListener("click", () => {
  if(menuLeft < 0){
    menu.classList.add("show");
  }
});

closeNav.addEventListener("click",() => {
  if(menuLeft < 0){
    menu.classList.remove("show");
  }
});

    // const loginText = document.querySelector(".title-text .login");
    // const loginForm = document.querySelector("form.login");
    // const loginBtn = document.querySelector("label.login");
    // const signupBtn = document.querySelector("label.signup");
    // const signupLink = document.querySelector("form .signup-link a");
    // signupBtn.onclick = (()=>{
    //   loginForm.style.marginLeft = "-50%";
    //   loginText.style.marginLeft = "-50%";
    // });
    // loginBtn.onclick = (()=>{
    //   loginForm.style.marginLeft = "0%";
    //   loginText.style.marginLeft = "0%";
    // });
    // signupLink.onclick = (()=>{
    //   signupBtn.click();
    //   return false;
    // });
