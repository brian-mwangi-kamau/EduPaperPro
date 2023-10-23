    document.addEventListener("DOMContentLoaded", function () {
        var ctx = document.getElementById("educationChart").getContext("2d");

        $.get("/metrics/", function (data) {
            var educationData = data.education_data;

            var labels = Object.keys(educationData);
            var counts = Object.values(educationData);

            var data = {
                labels: labels,
                datasets: [
                    {
                        data: counts,
                        backgroundColor: ["#FF5733", "#33FFB2", "#3360FF"],
                    },
                ],
            };

            var options = {
                responsive: true,
            };

            if (window.educationChart) {
                window.educationChart.data = data;
                window.educationChart.update();
            } else {
                window.educationChart = new Chart(ctx, {
                    type: "pie",
                    data: data,
                    options: options,
                });
            }
        });
    });

