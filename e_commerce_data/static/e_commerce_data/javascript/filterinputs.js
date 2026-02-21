// adding an input field to the DOM when selecting a value from the drop-down list with id js-filterByColumn
document.getElementById("js-filterByColumn").addEventListener("change", function(){
    document.getElementById("js-minValueInput").innerHTML = `<label for="minValueInput">Filter by min value</label>
                                                        <input type="number" id="minValueInput" name="minValueInput">`;
})