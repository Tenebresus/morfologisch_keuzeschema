const modal_title = document.getElementById('modal_title');
sub_categories = document.querySelectorAll('.boxieofzo');

sub_categories.forEach(box => {
    box.addEventListener('click', (e) => {
        modal_title.innerText = e.target.innerText;
        const url = e.target.baseURI.substring(0, e.target.baseURI.length - 1) + e.target.getAttribute('url');
        fetch(url)
            .then(response => response.json())
            .then(data => show_modal(data));
    });
});
const modal_items = document.getElementById('modal_items')

function show_modal(data) {
    modal_items.innerHTML = "";
    modal.style.display = 'block';
    data.forEach(l => {
        modal_items.innerHTML += `<div class="modal_item">
        <div class="item_title">
            <p class="title">` + l['leverancier_id__leverancier'] + ' ' + l['type'] + `</p>
            <div class="item_icon" onClick="expand('` + l['productnr'] + `')"><i class="fas fa-chevron-down"></i></div>
        </div>
        <div id="` + l['productnr'] + `" class="item_info">
            <p>Vermogen: ` + l['vermogen'] + `</p>
            <p>Belasting: ` + l['belasting'] + `</p>
            <p>Rendement: ` + l['rendement'] + `</p>
        </div>
        </div>`
    })
}

var span = document.getElementById("close");
var modal = document.getElementById("modal");
span.onclick = function () {
    modal.style.display = "none";
}

function expand(s) {
    item = document.getElementById(s);
    item.style.display = item.style.display === "grid" ? "none" : "grid";
}