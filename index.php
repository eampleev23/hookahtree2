<?php
// Path to the local PDF file
$pdfFile = 'catalog_retail_2024_02.pdf';

// Check if the file exists
if (file_exists($pdfFile)) {
    // Set headers to display the PDF in the browser
    header('Content-Type: application/pdf');
    header('Content-Disposition: inline; filename="catalog_retail_2024_02.pdf"');
    
    // Read the file and output its contents
    readfile($pdfFile);
} else {
    echo "The file does not exist.";
}
?>
