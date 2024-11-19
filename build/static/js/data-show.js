
var filters = {
    model: '',
    dataset: '',
    predlen: ''
};

// Set filter values and apply filter
function setFilter(column, value) {
    filters[column] = value;
    applyFilters();
}

// Apply filters to the table
function applyFilters() {
    var rows = document.querySelectorAll('#tableBody tr');
    rows.forEach(row => {
        var model = row.querySelector('td:nth-child(1)').textContent;
        var dataset = row.querySelector('td:nth-child(2)').textContent;
        var predlen = row.querySelector('td:nth-child(3)').textContent;

        if ((filters.model === '' || filters.model === model) &&
            (filters.dataset === '' || filters.dataset === dataset) &&
            (filters.predlen === '' || filters.predlen === predlen)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}



let sortOrder = {};

function sortTable(columnIndex) {
    const table = document.querySelector('.Table');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr')).filter(row => row.style.display !== 'none');

    // Determine and toggle current sort order
    sortOrder[columnIndex] = sortOrder[columnIndex] === 'asc' ? 'desc' : 'asc';
    const order = sortOrder[columnIndex];

    // Sort rows
    rows.sort((rowA, rowB) => {
        const cellA = rowA.querySelector(`td:nth-child(${columnIndex + 1})`).textContent;
        const cellB = rowB.querySelector(`td:nth-child(${columnIndex + 1})`).textContent;
        const valA = parseFloat(cellA);
        const valB = parseFloat(cellB);

        if (order === 'asc') {
            return valA - valB;
        } else {
            return valB - valA;
        }
    });

    // Append sorted rows
    rows.forEach(row => tbody.appendChild(row));
}


// // Sort table by descending and ascending button
// function sortTable(columnIndex, order) {
//     var table = document.querySelector('.table');
//     var rows = Array.from(table.querySelectorAll('tbody tr')).filter(row => row.style.display !== 'none').sort((rowA, rowB) => {
//         var cellA = rowA.querySelector(`td:nth-child(${columnIndex + 1})`).textContent;
//         var cellB = rowB.querySelector(`td:nth-child(${columnIndex + 1})`).textContent;
//         var valA = parseFloat(cellA);
//         var valB = parseFloat(cellB);
//         if (order === 'asc') {
//             return valA - valB;
//         } else {
//             return valB - valA;
//         }
//     });
//     rows.forEach(row => table.querySelector('tbody').appendChild(row));
// }
