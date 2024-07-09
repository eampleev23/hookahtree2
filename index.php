<?php
// URL of the PDF file
$pdfUrl = 'https://hookahtree.ru/catalog_retail_2024_02.pdf';

// Set headers to display the PDF in the browser
header('Content-Type: application/pdf');
header('Content-Disposition: inline; filename="catalog_retail_2024_02.pdf"');

// Use file_get_contents or curl to fetch the PDF content
$pdfContent = file_get_contents($pdfUrl);

// Output the PDF content
echo $pdfContent;
?>
