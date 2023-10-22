$(document).ready(function () {
    const cartItems = $("#cart-items");
    const cartTotal = $("#cart-total");
    const applyDiscountButton = $("#apply-discount");

    let cart = [];
    let total = 0;

    // Función para actualizar el carrito
    function updateCart() {
        cartItems.empty();
        total = 0;

        cart.forEach((item) => {
            const cartItem = $("<li>");
            cartItem.html(`${item.name} - $${item.price} <button class="remove-from-cart" data-id="${item.id}">Eliminar</button>`);
            cartItems.append(cartItem);
            total += item.price;
        });

        cartTotal.text(total);
    }

    // Botones "Agregar al Carrito"
    $(".add-to-cart").on("click", function () {
        const product = {
            id: $(this).closest(".product").index(),
            name: $(this).closest(".product").find("h2").text(),
            price: parseFloat($(this).closest(".product").find("p").text().split("$")[1])
        };
        cart.push(product);
        updateCart();
    });

    // Botones "Eliminar del Carrito"
    cartItems.on("click", ".remove-from-cart", function () {
        const itemId = parseInt($(this).attr("data-id"));
        cart = cart.filter((item) => item.id !== itemId);
        updateCart();
    });

    // Aplicar descuento
    applyDiscountButton.on("click", function () {
        const discountAmount = parseFloat(prompt("Ingrese el monto del descuento:"));
        if (!isNaN(discountAmount)) {
            total -= discountAmount;
            cartTotal.text(total);
        }
    });
});
