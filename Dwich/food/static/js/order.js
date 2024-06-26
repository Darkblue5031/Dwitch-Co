function addBurger(burid) {
    var burgerId = '#bur' + burid;
    var name = document.querySelector(burgerId).innerHTML;
    var radio = 'burger' + burid;
    var price = document.querySelector('input[name="' + radio + '"]:checked').value;

    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    orders.push([name, parseFloat(price)]);
    localStorage.setItem('orders', JSON.stringify(orders));
    total += parseFloat(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    pshoppingCart();
}

function pshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    pcart.innerHTML = '';
    for (let i = 0; i < orders.length; i++) {
        button = '<button class="del" onclick="removeBurger(' + i +')">X</button>';
        pcart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ' €' + button + '</li>';
    }
    ptotal.innerHTML = 'Total: ' + total + ' €';
}

pshoppingCart();

function removeBurger(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][1]);
    orders.splice(n,1);
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    pshoppingCart();
}

function adddwitch(burid) {
    var dwitchId = '#bur' + burid;
    var name = document.querySelector(dwitchId).innerHTML;
    var radio = 'dwitch' + burid;
    var price = document.querySelector('input[name="' + radio + '"]:checked').value;

    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    orders.push([name, parseFloat(price)]);
    localStorage.setItem('orders', JSON.stringify(orders));
    total += parseFloat(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    pshoppingCart();
}

function addfrite(burid) {
    var friteId = '#bur' + burid;
    var name = document.querySelector(friteId).innerHTML;
    var radio = 'frite' + burid;
    var price = document.querySelector('input[name="' + radio + '"]:checked').value;

    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    orders.push([name, parseFloat(price)]);
    localStorage.setItem('orders', JSON.stringify(orders));
    total += parseFloat(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    pshoppingCart();
}

function addsalade(burid) {
    var saladeId = '#bur' + burid;
    var name = document.querySelector(saladeId).innerHTML;
    var radio = 'salade' + burid;
    var price = document.querySelector('input[name="' + radio + '"]:checked').value;

    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    orders.push([name, parseFloat(price)]);
    localStorage.setItem('orders', JSON.stringify(orders));
    total += parseFloat(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    pshoppingCart();
}

function adddessert(burid) {
    var dessertId = '#bur' + burid;
    var name = document.querySelector(dessertId).innerHTML;
    var radio = 'dessert' + burid;
    var price = document.querySelector('input[name="' + radio + '"]:checked').value;

    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    orders.push([name, parseFloat(price)]);
    localStorage.setItem('orders', JSON.stringify(orders));
    total += parseFloat(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    pshoppingCart();
}

