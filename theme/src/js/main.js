// Main menu dropdowns
;[].forEach.call(document.querySelectorAll('li.dropdown'), function(dropdown) {

    dropdown.addEventListener('mouseover', function() {
        dropdown.classList.add('open');
        dropdown.querySelector('a').setAttribute('aria-expanded', true);
    })
    dropdown.addEventListener('mouseout', function() {
        dropdown.classList.remove('open');
        dropdown.querySelector('a').setAttribute('aria-expanded', false);
    })
});

// Navbar toggle (mobile menu)
document.querySelector('.navbar-toggle').addEventListener('click', function() {
    [].forEach.call(document.querySelectorAll('.navbar-collapse'), function(navbar) {
        navbar.classList.toggle('collapse');
    });
});


// function loadUdataWidgets() {
//     udataScript.loadDatasets();
//     udataScript.loadOrganization();
//     udataScript.loadTerritory();
// }

// <div data-udata-dataset-id="5862206588ee38254d3f4e5e"></div>
// <script src="https://www.data.gouv.fr/static/widgets.js" id="udata" async defer></script>
