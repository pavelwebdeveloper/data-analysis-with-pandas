
document.getElementById("js-filterByColumn").addEventListener("change", function(){
    document.getElementById("js-minValueInput").innerHTML = `<label for="minValueInput">Filter by min value</label>
                                                        <input type="number" id="minValueInput" name="minValueInput">`;
})