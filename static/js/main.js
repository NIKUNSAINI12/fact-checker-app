// Get DOM elements
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const browseBtn = document.getElementById('browseBtn');
const uploadSection = document.querySelector('.upload-section');
const loadingSection = document.getElementById('loadingSection');
const errorSection = document.getElementById('errorSection');
const errorMessage = document.getElementById('errorMessage');
const tryAgainBtn = document.getElementById('tryAgainBtn');

// Prevent default drag behaviors
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

// Highlight drop zone when dragging over it
['dragenter', 'dragover'].forEach(eventName => {
    dropZone.addEventListener(eventName, () => {
        dropZone.classList.add('drag-over');
    }, false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, () => {
        dropZone.classList.remove('drag-over');
    }, false);
});

// Handle dropped files
dropZone.addEventListener('drop', (e) => {
    const files = e.dataTransfer.files;
    handleFiles(files);
}, false);

// Handle browse button click
browseBtn.addEventListener('click', () => {
    fileInput.click();
});

// Handle click on drop zone
dropZone.addEventListener('click', (e) => {
    if (e.target !== browseBtn) {
        fileInput.click();
    }
});

// Handle file input change
fileInput.addEventListener('change', (e) => {
    handleFiles(e.target.files);
});

// Handle try again button
tryAgainBtn.addEventListener('click', () => {
    resetUploadSection();
});

// Handle file upload
function handleFiles(files) {
    if (files.length === 0) return;

    const file = files[0];

    // Validate file type
    if (!file.name.toLowerCase().endsWith('.pdf')) {
        showError('Please upload a PDF file');
        return;
    }

    // Validate file size (10MB max)
    const maxSize = 10 * 1024 * 1024;
    if (file.size > maxSize) {
        showError('File size must be less than 10MB');
        return;
    }

    // Upload file
    uploadFile(file);
}

// Upload file to server
function uploadFile(file) {
    showLoading();

    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
        .then(response => {
            // Check if response is ok
            if (!response.ok) {
                // Try to get error message from response
                return response.text().then(text => {
                    try {
                        const json = JSON.parse(text);
                        throw new Error(json.error || 'Upload failed');
                    } catch (e) {
                        throw new Error(`Server error: ${response.status} - ${text.substring(0, 100)}`);
                    }
                });
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                showError(data.error);
            } else if (data.success) {
                // Redirect to results page
                window.location.href = data.redirect;
            }
        })
        .catch(error => {
            console.error('Upload error:', error);
            showError(error.message || 'Upload failed. Please try again.');
        });
}

// Show loading state
function showLoading() {
    dropZone.style.display = 'none';
    errorSection.style.display = 'none';
    loadingSection.style.display = 'block';

    // Animate loading text
    let dots = 0;
    const loadingInterval = setInterval(() => {
        dots = (dots + 1) % 4;
        document.getElementById('loadingText').textContent =
            'Processing your document' + '.'.repeat(dots);
    }, 500);

    // Store interval ID for cleanup
    loadingSection.dataset.intervalId = loadingInterval;
}

// Show error state
function showError(message) {
    // Clear loading interval if exists
    const intervalId = loadingSection.dataset.intervalId;
    if (intervalId) {
        clearInterval(parseInt(intervalId));
    }

    dropZone.style.display = 'none';
    loadingSection.style.display = 'none';
    errorSection.style.display = 'block';
    errorMessage.textContent = message;
}

// Reset upload section
function resetUploadSection() {
    dropZone.style.display = 'block';
    loadingSection.style.display = 'none';
    errorSection.style.display = 'none';
    fileInput.value = '';
}
