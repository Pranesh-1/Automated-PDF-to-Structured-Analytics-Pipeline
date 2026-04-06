const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const resultsSection = document.getElementById('results-section');
const uploadSection = document.getElementById('upload-section');
const loader = document.getElementById('loader');

// Drag and drop events
dropZone.addEventListener('click', () => fileInput.click());
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('hover');
});
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('hover'));
dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('hover');
    handleFiles(e.dataTransfer.files);
});

fileInput.addEventListener('change', (e) => handleFiles(e.target.files));

async function handleFiles(files) {
    if (files.length === 0) return;
    const file = files[0];
    if (file.type !== 'application/pdf') {
        alert('Please upload a PDF file.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    loader.style.display = 'flex';

    try {
        const response = await fetch('/extract', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.success) {
            renderResults(result.data);
            showResults();
        } else {
            alert('Extraction failed: ' + result.error);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during extraction.');
    } finally {
        loader.style.display = 'none';
    }
}

function renderResults(data) {
    document.getElementById('job-title').value = data.job_title || '';
    document.getElementById('company-name').value = data.company_name || '';
    document.getElementById('location').value = data.location || '';
    document.getElementById('experience-level').value = data.experience_level || '';
    document.getElementById('compensation').value = data.compensation || '';
    
    // Confidence Meter
    const confidence = (data.confidence_score * 100).toFixed(0);
    document.getElementById('confidence-fill').style.width = confidence + '%';
    
    // Detailed Info
    document.getElementById('must-have-skills').value = (data.must_have_skills || []).join(', ');
    document.getElementById('bonus-points').value = (data.bonus_points || []).join(', ');
    document.getElementById('responsibilities').value = JSON.stringify(data.responsibilities || [], null, 2);
    
    // Email Tags
    const emailList = document.getElementById('email-tags');
    emailList.innerHTML = '';
    (data.contact_emails || []).forEach(email => {
        const span = document.createElement('span');
        span.className = 'tag';
        span.textContent = email;
        emailList.appendChild(span);
    });
}

function showResults() {
    uploadSection.style.display = 'none';
    resultsSection.classList.add('visible');
    resultsSection.style.display = 'grid';
}

function resetUI() {
    uploadSection.style.display = 'block';
    resultsSection.classList.remove('visible');
    resultsSection.style.display = 'none';
    fileInput.value = '';
}

function exportCSV() {
    const data = {
        job_title: document.getElementById('job-title').value,
        company_name: document.getElementById('company-name').value,
        location: document.getElementById('location').value,
        experience_level: document.getElementById('experience-level').value,
        compensation: document.getElementById('compensation').value,
        must_have_skills: document.getElementById('must-have-skills').value,
        bonus_points: document.getElementById('bonus-points').value,
    };

    const csvContent = "data:text/csv;charset=utf-8," 
        + Object.keys(data).join(",") + "\n"
        + Object.values(data).map(v => `"${v}"`).join(",");

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `extracted_jd_${Date.now()}.csv`);
    document.body.appendChild(link);
    link.click();
}
