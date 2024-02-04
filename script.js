// static/script.js
function getHIndex() {
    const scholarName = document.getElementById('scholarName').value;

    if (scholarName.trim() === '') {
        alert('Please enter a scholar\'s name.');
        return;
    }

    fetch('/getHIndex', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ scholarName }),
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.textContent = `H-Index: ${data.hIndex}`;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error fetching H-Index. Please try again.');
    });
}