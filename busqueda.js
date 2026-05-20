// Búsqueda en tiempo real
const searchInput = document.getElementById('search-input');
const rows = document.querySelectorAll('.table-row');
const emptyState = document.getElementById('empty-state');
const rowCount = document.getElementById('row-count');

searchInput.addEventListener('input', function () {
    const q = this.value.toLowerCase().trim();
    let visible = 0;
    rows.forEach(row => {
        const text = row.dataset.search || '';
        const show = text.includes(q);
        row.classList.toggle('hidden', !show);
        if (show) visible++;
    });
    rowCount.textContent = visible;
    emptyState.classList.toggle('hidden', visible > 0 || rows.length === 0);
});