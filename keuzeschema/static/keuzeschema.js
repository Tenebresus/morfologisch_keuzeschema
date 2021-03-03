box = document.getElementsByClassName('boxieofzo');

var loginb = document.getElementById("loginb");
loginb.style.display = "none";

for(var i = 0; i < box.length; i++){
    boxi = box[i];
    boxi.onclick = function(){
        modal.style.display = "block";
    };
}
var span = document.getElementsByClassName("close")[0];
var modal = document.getElementById("modal");
span.onclick = function() {
    modal.style.display = "none";
}

//nav
var nav = document.getElementById("sidebar");
var defaultheight = nav.style.height;


function openNav(){
    if (nav.style.height === "100vh") {
        nav.style.height = defaultheight;
        loginb.style.display = "none";
      } else {
        nav.style.height = "100vh";
        loginb.style.display = "inline";
      }
}