function openDeleteModal({
    title = '¿Eliminar registro?',
    name = '',
    url = '#'
}) {

    document.getElementById('delete-title').textContent = title;
    document.getElementById('delete-item-name').textContent = name;
    document.getElementById('delete-confirm-btn')
        .setAttribute('href', url);
    const modal = document.getElementById('delete-modal');

    modal.classList.remove('hidden');
    modal.classList.add('flex');
}

function closeDeleteModal() {
    const modal = document.getElementById('delete-modal');
    modal.classList.add('hidden');
    modal.classList.remove('flex');
}

document.addEventListener('DOMContentLoaded', () => {
    // abrir modal
    document.querySelectorAll('.delete-btn').forEach(btn => {

        btn.addEventListener('click', function (e) {
            e.preventDefault();
            openDeleteModal({
                title: this.dataset.title,
                name: this.dataset.name,
                url: this.href
            });
        });

    });
});