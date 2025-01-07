function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("table");
    switching = true;
    for (count = 0; count < 6; count++) {
        z = table.rows[0].getElementsByTagName("TH")[count];
        z.innerHTML = z.innerHTML.split(" ")[0];
    }
    z = table.rows[0].getElementsByTagName("TH")[n];
    initial = z.innerHTML.split(" ")[0];
    dir = "asc";

    while (switching) {
        switching = false;
        rows = table.rows;

        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;

            // Get the two cells to compare
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];

            if (n === 0) {
                // Parse dates for comparison if column is 'Date'
                var dateX = new Date(x.innerHTML); // Parse Date
                var dateY = new Date(y.innerHTML); // Parse Date

                if (dir == "asc") {
                    if (dateX > dateY) {
                        shouldSwitch = true;
                        z.innerHTML = initial + " ↑";
                        break;
                    }
                } else if (dir == "desc") {
                    if (dateX < dateY) {
                        shouldSwitch = true;
                        z.innerHTML = initial + " ↓";
                        break;
                    }
                }
            } else {
                // Handle other columns as text or numbers
                if (!isNaN(x.innerHTML) && !isNaN(y.innerHTML)) {
                    // Compare numeric values
                    var tempx = parseFloat(x.innerHTML);
                    var tempy = parseFloat(y.innerHTML);

                    if (dir == "asc" && tempx > tempy) {
                        shouldSwitch = true;
                        z.innerHTML = initial + " ↑";
                        break;
                    } else if (dir == "desc" && tempx < tempy) {
                        shouldSwitch = true;
                        z.innerHTML = initial + " ↓";
                        break;
                    }
                } else {
                    // Compare text values
                    if (dir == "asc" && x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                        shouldSwitch = true;
                        z.innerHTML = initial + " ↑";
                        break;
                    } else if (dir == "desc" && x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                        shouldSwitch = true;
                        z.innerHTML = initial + " ↓";
                        break;
                    }
                }
            }
        }

        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}

function searchTable() {
    var filter, tr, td, i, restaurant;
    filter = document.getElementById("myInput").value.toUpperCase();
    tr = document.getElementById("table").getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            restaurant = td.innerText;
            if (restaurant.toUpperCase().indexOf(filter) != -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}