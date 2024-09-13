function submitRandom() {
    const form = document.getElementById('preferenceForm');
    const randomValue = Math.random() < 0.5 ? 'geometric' : 'floral';
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'preference';
    input.value = randomValue;
    form.appendChild(input);
    form.submit();
}

function resetForm() {
    document.getElementById("preference-form").reset();  // Resets the form
}

document.getElementById('flip-button').addEventListener('click', function() {
    const image = document.getElementById('result-image');
    image.classList.toggle('flipped'); // Toggle the 'flipped' class
});