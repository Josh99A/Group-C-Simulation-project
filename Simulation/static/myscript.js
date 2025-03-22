function openNav() {
  document.getElementById("sidebar").style.width = "250px";
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("sidebar").style.width = "0";
}


function showHideFields() {
    var algorithm = document.getElementById("algorithm").value;
    var priorityGroup = document.getElementById("priority-group");
    var timeQuantumGroup = document.getElementById("time-quantum-group");
    var selectedAlgorithm = document.getElementById("select-algorithm");

    console.log(algorithm);
    console.log(algorithm == 4);
    console.log(timeQuantumGroup);

    if (algorithm == 5 || algorithm == 6) {
      priorityGroup.style.display = "block";
    } else {
      priorityGroup.style.display = "none";
    }

    if (algorithm == 4) {
      timeQuantumGroup.style.display = "block";
      selectedAlgorithm.style.marginTop="13px";
    } else {
      timeQuantumGroup.style.display = "none";
    }
  }