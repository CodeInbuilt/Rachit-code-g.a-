// scripts.js
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('tv-form').addEventListener('submit', handleFormSubmit);
    document.getElementById('phone-form').addEventListener('submit', handleFormSubmit);
    document.getElementById('rent-form').addEventListener('submit', handleFormSubmit);
    document.getElementById('electricity-form').addEventListener('submit', handleFormSubmit);
    document.getElementById('water-form').addEventListener('submit', handleFormSubmit);

    function handleFormSubmit(event) {
        event.preventDefault();
        const form = event.target;
        const account = form.querySelector('input[type="text"]').value;
        const amount = form.querySelector('input[type="number"]').value;
        alert(`Bill paid successfully!\nAccount: ${account}\nAmount: $${amount}`);
        form.reset();
    }
});
