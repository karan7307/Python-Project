document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const data = {
        study_hours: parseFloat(document.getElementById('study_hours').value),
        stress_level: parseFloat(document.getElementById('stress_level').value),
        sleep_hours: parseFloat(document.getElementById('sleep_hours').value),
        extracurricular_activities: parseFloat(document.getElementById('extracurricular_activities').value)
    };

    const submitBtn = e.target.querySelector('button');
    submitBtn.innerText = 'Analyzing...';
    submitBtn.disabled = true;

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        
        if (result.burnout_score !== undefined) {
            const scorePercent = (result.burnout_score * 100).toFixed(1);
            document.getElementById('scoreValue').innerText = `${scorePercent}%`;
            document.getElementById('result').style.display = 'block';
            
            // Scroll to result
            document.getElementById('result').scrollIntoView({ behavior: 'smooth' });
        } else {
            alert('Error: ' + (result.error || 'Unknown error'));
        }
    } catch (error) {
        alert('Failed to connect to AI service');
    } finally {
        submitBtn.innerText = 'Analyze Burnout';
        submitBtn.disabled = false;
    }
});
