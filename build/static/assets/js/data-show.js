document.addEventListener("DOMContentLoaded", function() {
  // 定义获取数据的函数
  function fetchData() {
    fetch('/data')
      .then(response => {
        console.log('Response received');
        return response.json();
      })
      .then(data => {
        console.log('Data:', data); // 查看获取到的数据
        displayData(data); // 调用显示数据的函数
      })
      .catch(error => console.error('Error fetching data:', error));
  }


  // 定义显示数据的函数
  function displayData(data) {
    // 创建MSE表格
    let mseHTML = '<table><tr><th>Dataset-PredLen</th><th>Model</th><th>MSE</th></tr>';
    data.forEach(item => {
      mseHTML += `<tr><td>${item.dataset}-${item.pred_len}</td><td>${item.model_name}</td><td>${item.MSE}</td></tr>`;
    });
    mseHTML += '</table>';

    // 创建MAE表格
    let maeHTML = '<table><tr><th>Dataset-PredLen</th><th>Model</th><th>MAE</th></tr>';
    data.forEach(item => {
      maeHTML += `<tr><td>${item.dataset}-${item.pred_len}</td><td>${item.model_name}</td><td>${item.MAE}</td></tr>`;
    });
    maeHTML += '</table>';

    // 获取data-container元素并设置其内容为刚刚创建的表格HTML
    const container = document.getElementById('data-container');
    container.innerHTML = mseHTML + maeHTML; // 将两个表格的HTML添加到页面中
  }

  // 调用函数获取数据
  fetchData();
});
