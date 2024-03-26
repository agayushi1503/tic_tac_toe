
const cells = document.querySelectorAll('.cell');

cells.forEach(cell => {
    cell.addEventListener('click', function() {
        const move = cell.getAttribute('data-cell');
        document.getElementById('move').value = move;
        cell.classList.add('clicked');
    });
});
