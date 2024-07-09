<?php
// URL of the PDF file
$pdfUrl = 'https://hookahtree.ru/catalog_retail_2024_02.pdf';

// Initialize a cURL session
$ch = curl_init();

// Set the URL
curl_setopt($ch, CURLOPT_URL, $pdfUrl);

// Return the transfer as a string
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

// Fetch the PDF content
$pdfContent = curl_exec($ch);

// Close the cURL session
curl_close($ch);

// Set headers to display the PDF in the browser
header('Content-Type: application/pdf');
header('Content-Disposition: inline; filename="catalog_retail_2024_02.pdf"');

// Output the PDF content
echo $pdfContent;
?>