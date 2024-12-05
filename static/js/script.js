// JavaScript for File Upload Preview
const imageUpload = document.getElementById("image-upload");
const uploadLabel = document.querySelector(".upload-label");
const imagePreview = document.getElementById("image-preview");

if (imageUpload) {
    imageUpload.addEventListener("change", () => {
        const fileName = imageUpload.files[0]?.name || "Choose Image";
        uploadLabel.textContent = fileName;
        
        // Display the image preview
        const file = imageUpload.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.style.display = 'block'; // Show the image element
                imagePreview.src = e.target.result;  // Set the preview image source
            };
            reader.readAsDataURL(file);
        } else {
            imagePreview.style.display = 'none'; // Hide the image preview if no file is selected
        }
    });
}

