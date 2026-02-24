let unitPrice = 500;
let quantity = 1;

function increaseQty() {
    quantity++;
    updateTotal();
}

function decreaseQty() {
    if (quantity > 1) {
        quantity--;
        updateTotal();
    }
}

function updateTotal() {
    document.getElementById("quantity").value = quantity;
    document.getElementById("totalPrice").innerText = unitPrice * quantity;
}
