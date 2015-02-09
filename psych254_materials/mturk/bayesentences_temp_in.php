<?php 
	header('Access-Control-Allow-Origin: https://langcog.stanford.edu');
	$pre = "https://langcog.stanford.edu/cgi-bin/NPM_bayesentences/turkerTrials/";
	$oldpath = "turkerTrials/";
	$post = "https://langcog.stanford.edu/cgi-bin/NPM_bayesentences/";
	$newpath = "temp/";
	$files = glob($oldpath . "*.csv");
	$entry = array_values($files)[0];
	$index = strripos($entry,'/',0); //finds the last backslash
	$new = substr($entry,$index+1); //grabs the file name out of the filepath
	$input = $entry;
	$output = $newpath . $new;
	$final = $newpath . $new; //creates a new filepath for the file, now to be in the temp folder
	rename($input, $output);
	echo json_encode($post . $output);
?>