<?php 
	header('Access-Control-Allow-Origin: https://langcog.stanford.edu');
	$input = $_GET["w1"]; //in filepath for the data file, coming from temp folder
	$output = $_GET["w2"]; //out filepath for the data file, back to turkerTrials folder
	rename($input, $output); //moves the file
	echo json_encode($output); //passes new filepath back
?>
