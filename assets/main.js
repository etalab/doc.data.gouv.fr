;(function() {

  // Add anchors to titles
  [].forEach.call(document.querySelectorAll('.markdown'), function(container) {
    [].forEach.call(container.querySelectorAll('h2,h3,h4,h5,h6'), function(title) {
      const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
      use.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', '#icon-link');

      const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.appendChild(use);

      const anchor = document.createElement('a');
      anchor.href = '#' + title.id;
      anchor.classList.add('anchor');
      anchor.appendChild(svg);

      title.appendChild(anchor);
    });
  });

  // Handle search
  const searchInput = document.getElementById('search-input')

  SimpleJekyllSearch({
    searchInput: searchInput,
    resultsContainer: document.getElementById('search-results-container'),
    json: '/search.json',
    searchResultTemplate: [
      '<div class="search-result">',
      '<h4><a href="{url}">{category} > {title}</a></h4>',
      '<p>{excerpt}</p>',
      '</div>'
    ].join('')
  })

  searchInput.addEventListener('input', function(ev) {
    if (searchInput.value) {
      document.body.classList.add('searching')
      document.getElementById('search-query').innerText = searchInput.value
    } else {
      document.body.classList.remove('searching')
    }
  })
})();
