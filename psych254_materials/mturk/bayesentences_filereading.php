<?php 
	header('Access-Control-Allow-Origin: https://langcog.stanford.edu');
	$filepath = $_GET["w1"]; //gets the dynamically created part of the url specifying which list number selected
	$csvData = file_get_contents($filepath); //gets csvData
	$csvNumRows = $_GET["w2"]; //sets how many chunks for our array; typically number of trials in the experiment
	$data = array_chunk(str_getcsv($csvData, "\n"), $csvNumRows); //chunks the csv data by row (trial) and into the $data var
	echo json_encode($data); //outputs the php var as a javascript var in json format!
?>