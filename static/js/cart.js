function updateQuantity(productId, change) {
    console.log(productId)
    // const input = document.querySelector(`input[data-product-id="${productId}"]`);
    const input = document.getElementById("item1");
    const price = document.getElementById("price");
    // const total = document.getElementById("totoalAmount");
    let newValue = parseInt(input.value) + change;
    newValue = Math.max(1, newValue); // Prevent negative values
    console.log("newValue"+newValue*price.textContent)
    document.getElementById("sub").textContent = newValue*price.textContent;
    input.value = newValue;
    // console.log(total.textContent)
    // total.textContent = total.textContent+(newValue*price.textContent)
}