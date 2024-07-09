<?php
// Specify the PDF file path
$pdfFile = 'https://hookahtree.ru/catalog_retail_2024_02.pdf';

// Set headers to display the PDF in the browser
header('Content-Type: application/pdf');
header('Content-Disposition: inline; filename="catalog_retail_2024_02.pdf"');

// Read and output the PDF file
readfile($pdfFile);
?>
