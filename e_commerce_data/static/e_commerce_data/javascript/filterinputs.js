
document.getElementById("Order ID").addEventListener("click", function(){
    document.getElementById("js-orderId").innerHTML = `<label for="minOrderID">min Order ID</label>
                                                        <input type="number" id="minOrderID" name="minOrderID">
                                                        <label for="maxOrderID">max Order ID</label>
                                                        <input type="number" id="maxOrderID" name="maxOrderID">`;
})