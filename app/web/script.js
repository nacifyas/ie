document.addEventListener("DOMContentLoaded", function () {
    const dataElement = document.getElementById("data");

    // Function to update the content of the data element and create a graph
    function updateDataAndGraph() {
        // Update data
        dataElement.innerHTML = "<p>This is dynamic data from JavaScript! Updated every 5 seconds.</p>";

        // Sample data (replace with your actual data)
        const labels = ["January", "February", "March", "April", "May", "June", "July"];
        const data = {
            labels: labels,
            datasets: [{
                label: 'My Dataset',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [10, 20, 30, 40, 50, 60, 70],
            }]
        };

        // Create chart
        const ctx = document.getElementById('myChart').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: data,
            options: {}
        });
    }

    // Initial update
    updateDataAndGraph();

    // Set interval to update data and graph every 5 seconds
    setInterval(updateDataAndGraph, 5000);

    // Function to toggle between light and dark mode
    function toggleDarkMode() {
        const body = document.body;
        body.classList.toggle('dark-mode');
    }

    // Event listener for toggling dark mode
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    darkModeToggle.addEventListener('click', toggleDarkMode);
});
