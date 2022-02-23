$('.toggle-nav').click(function(e) {
    e.preventDefault();
  
    var $this = $(this);

    $this.find(".icon-dropdown").toggleClass("rotate");
  
    if ($this.next().hasClass('show')) {
        $this.next().removeClass('show');
        $this.next().slideUp(350);
    } else {
        $this.parent().parent().find('li .inner2').removeClass('show');
        $this.parent().parent().find('li .inner2').slideUp(350);
        $this.next().toggleClass('show');
        $this.next().slideToggle(350);
    }
});


function toggleFunc(e) {
    e.classList.toggle("change");
    document.getElementById("btn-toggle")
      .classList
      .toggle("show");
  }



  // for HAMBURGER MENU

const hamburgerMenu = document.querySelector(".hamburger-menu");
const ul = document.querySelector("nav ul");

hamburgerMenu.addEventListener("click", () => {
  hamburgerMenu.classList.toggle("hamburger-rotate");
  ul.classList.toggle("slide-out");
});


let form = document.getElementById('subscribe-form');

let error_section = document.getElementById('error-list');

form.addEventListener('submit',async function (e) {
    e.preventDefault();
    error_section.innerText = '';
    let form_data = {
        'email': form.email.value
    }
    let response = await fetch('http://127.0.0.1:8000/api/email/',{
        headers: {
            'content-type': 'application/json',
            "X-CSRFToken" : form.csrfmiddlewaretoken.value
        },
        method: "POST",
        body: JSON.stringify(form_data)
        
    })
    let response_data = await response.json();
    let status = await response.ok;
    if (status==true){
        form.email.value=''
        alert('You will be contacte');
    }
    else{
        for(let error of response_data.email){
            error_section.innerHTML += `<li class="text-danger">${error}</li>`
        }
    }
    
})