
function createBarChart(ctx, data) {
    return new Chart(ctx, {
      type: "bar",
      data: {
        labels: data.labels,
        datasets: [
          {
            label: "Downloads",
            data: data.downloads,
            backgroundColor:"rgba(75, 192, 192, 0.2)",
            borderColor: "rgba(75, 192, 192, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  }
  

  function fetchDataAndCreateCharts() {
    fetch('/downloads/')
      .then((response) => response.json())
      .then((data) => {
        const months = data.downloads.map((record) => record.month);
        const downloadCounts = data.downloads.map((record) => record.count);

        const monthlyData = {
          labels: months,
          downloads: downloadCounts,
        };
  
        const monthlyCtx = document.getElementById("monthlyChart").getContext("2d");
  
        if (monthlyChart) {
          monthlyChart.data.labels = monthlyData.labels;
          monthlyChart.data.datasets[0].data = monthlyData.downloads;
          monthlyChart.update();
        } else {
          monthlyChart = createBarChart(monthlyCtx, monthlyData);
        }
      })
      .catch((error) => console.error('Error fetching data:', error));
  }
  

  let monthlyChart;
  
  fetchDataAndCreateCharts();