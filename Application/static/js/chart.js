

function createBarChart(ctx, data) {
    return new Chart(ctx, {
      type: "bar",
      data: {
        labels: data.labels,
        datasets: [
          {
            label: "Downloads",
            data: data.downloads,
            backgroundColor: "rgba(75, 192, 192, 0.2)",
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
        const dates = data.downloads.map((record) => record.date);
        const downloadCounts = data.downloads.map((record) => record.count);
  
        const weeklyData = {
          labels: dates,
          downloads: downloadCounts,
        };
  
  
        const monthlyData = {
  
        };
  
        const weeklyCtx = document.getElementById("weeklyChart").getContext("2d");
        const monthlyCtx = document.getElementById("monthlyChart").getContext("2d");
  
  
        if (weeklyChart) {
          weeklyChart.data.labels = weeklyData.labels;
          weeklyChart.data.datasets[0].data = weeklyData.downloads;
          weeklyChart.update();
        } else {
          weeklyChart = createBarChart(weeklyCtx, weeklyData);
        }
  
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
  
  
  let weeklyChart;
  let monthlyChart;
  
  fetchDataAndCreateCharts();