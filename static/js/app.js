var modal = document.getElementById('modal_create-account');

var button = document.getElementById('cards-add_card_button');

var span = document.getElementsByClassName('close_button')[0];

// ACTIONS
button.onclick = function() {
    modal.style.visibility = "visible";
    modal.style.opacity = 1;
}

span.onclick = function() {
    modal.style.visibility = "hidden";
    modal.style.opacity = 1;
  }
  
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.visibility = "hidden";
        modal.style.opacity = 1;
    }
}

// Actions
function displayDropdown() {
    document.getElementById("myDropdown").classList.toggle('show');
}

document.onclick = function(event) {
    if (!event.target.matches('.drop-button')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
}
