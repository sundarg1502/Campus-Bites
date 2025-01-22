function updateQuantity(productId, change) {
    // console.log(productId)
    const input = document.getElementById("item"+productId);
    const price = document.getElementById("price"+productId);
    const total = document.getElementById("totalAmount");
    let newValue = parseInt(input.value) + change;
    newValue = Math.max(1, newValue); // Prevent negative values
    console.log("newValue"+newValue*price.textContent)
    document.getElementById("sub"+productId).textContent = newValue*price.textContent;
    input.value = newValue;
    // console.log("TOTal Amount"+parseInt(total.textContent)+(newValue*price.textContent)-(newValue+(change)*price.textContent))
}
