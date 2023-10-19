$(document).ready(function() {
    updateCircleChart();

    function updateCircleChart() {
        $.get('/metrics/', function(data) {
            var currentUsers = data.total_users;
            var totalUsers = 10;

            var chartData = {
                labels: ['Users', 'Target'],
                datasets: [{
                    data: [currentUsers, totalUsers],
                    backgroundColor: ['#36A2EB', '#E7E7E7'],
                    borderWidth: 0,
                }],
            };

            var chartOptions = {
                cutoutPercentage: 0,
                responsive: false,
                rotation: -Math.PI,
                circumference: 2 * Math.PI,
            };

            var chartCenterText = currentUsers + ' / ' + totalUsers;

            var chart = new Chart(document.getElementById('userCircleChart'), {
                type: 'doughnut',
                data: chartData,
                options: chartOptions,
            });


            var userCountText = document.getElementById('userCountText');
            userCountText.innerText = chartCenterText;
        });
    }

    setInterval(updateCircleChart, 60000);
});