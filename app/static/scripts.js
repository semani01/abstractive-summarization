function showSpinner() {
    document.getElementById("loading-spinner").style.display = "block";
}

function hideSpinner() {
    document.getElementById("loading-spinner").style.display = "none";
}

document.getElementById("summarize-text-btn").addEventListener("click", () => {
    const text = document.getElementById("text-input").value;
    if (!text) {
        alert("Please enter some text.");
        return;
    }

    showSpinner();
    fetch("/summarize/text", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
    })
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("summary-output").textContent = data.summary || "Error generating summary.";
        })
        .catch(() => {
            document.getElementById("summary-output").textContent = "An error occurred.";
        })
        .finally(hideSpinner);
});

document.getElementById("summarize-pdf-btn").addEventListener("click", () => {
    const fileInput = document.getElementById("file-input").files[0];
    if (!fileInput) {
        alert("Please upload a PDF file.");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput);

    showSpinner();
    fetch("/summarize/pdf", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("summary-output").textContent = data.summary || "Error generating summary.";
        })
        .catch(() => {
            document.getElementById("summary-output").textContent = "An error occurred.";
        })
        .finally(hideSpinner);
});

document.getElementById("summarize-url-btn").addEventListener("click", () => {
    const url = document.getElementById("url-input").value;
    if (!url) {
        alert("Please enter a URL.");
        return;
    }

    showSpinner();
    fetch("/summarize/url", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
    })
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("summary-output").textContent = data.summary || "Error generating summary.";
        })
        .catch(() => {
            document.getElementById("summary-output").textContent = "An error occurred.";
        })
        .finally(hideSpinner);
});
