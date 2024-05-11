document.addEventListener("DOMContentLoaded", function () {
    const dataElement = document.getElementById("data");

    // Function to update the content of the data element
    function initData() {
        dataElement.innerHTML = "<p>This is dynamic data from JavaScript! Updated every 5 seconds.</p>";
    }

    function updateData() {
        dataElement.innerHTML = "<p>Isn't it cool.</p>";
    }


    // Initial update
    initData();

    // Set interval to update data every 5 seconds
    setInterval(updateData, 5000);
});
