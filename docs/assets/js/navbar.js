document.addEventListener('DOMContentLoaded', function() {
    var navbar = create_navbar();
    document.body.insertBefore(navbar, document.body.firstChild); // Insert the navbar at the top
});

function create_navbar() {
    var navbar = document.createElement('ul');
    
    // Add navbar items
    navbar.appendChild(create_navbar_element('Home', '/'));
    navbar.appendChild(create_navbar_element('Python', '/python/python.html'));
    
    return navbar;
}

function create_navbar_element(text, href) {
    var li = document.createElement('li');
    var a = document.createElement('a');
    
    a.innerHTML = text;
    a.href = get_relative_path(href); // Set the correct path
    
    li.appendChild(a);
    return li;
}

// This function helps adjust relative paths depending on the folder depth
function get_relative_path(href) {
    var current_path = window.location.pathname.split('/').filter(Boolean);
    var target_path = href.split('/').filter(Boolean);

    var common_segments = 0;
    for (var i = 0; i < Math.min(current_path.length, target_path.length); i++) {
        if (current_path[i] === target_path[i]) {
            common_segments++;
        } else {
            break;
        }
    }

    var up_levels = current_path.length - common_segments;
    var relative_path = '../'.repeat(up_levels) + target_path.slice(common_segments).join('/');

    return relative_path;
}
