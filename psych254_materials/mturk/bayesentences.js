//Title: Bayesentence, replication of Gibson, Bergen, and Piantadosi (2013) in PNAS
//Author: Nick Moores, Stanford University LangCog Lab + Phonetics Lab
//Many thanks to Ann Nordmeyer and Michael C. Frank

//Updated as of 2/08/2015

/*---------------INTRODUCTION-------------------*/
/*
Only replicating the first 3 sub-experiments of experiment 1.
So: with the 'base fillers', studying (1.1) Active/Passive, (1.2) Obj-Loc/Subj-Loc, (1.3) Intrans/Trans
Materials: located in target-materials/ and in fillers/ on Github

Naming convention for experiment files is:
bayesentences.filetype :: consisting of:
bayesentences.html (governs structure of experiment)
bayesentences.js (governs user interaction with the experiment)
bayesentences_filereading.php (reading in data for the experiment)
bayesentences_temp_in.php (moving the HIT to a temp/ folder so it is unavailable to others)
bayesentences_temp_out.php (in case the user aborts the HIT)
bayesentences_submit.php (to write the data to the server)
*/

/*---------------- PARAMETERS -----------------------*/

var numTrials = 60; //governs the number of trials in the experiment
var subjectID = turk.workerId;
var data;
var decision;
var inputfilepath = "LocativeList4.csv";
var counter = '/60 trials completed';
var numCSVRows = 61;
var pauseTime = 500; //governs the animation look
var conditions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59];
var experiment_result_array = [];
var result_headers = ["subjectID", "list_number", "alternation","item_number", "utterance", "question", "alt_tag", "syntax_interpretation", "answer", "day", "time"];
experiment_result_array[0] = result_headers; //puts in headers for result file

/*---------------- HELPER FUNCTIONS------------------*/

// show slide function
function showSlide(id) {
	$(".slide").hide(); //jquery - all elements with class of slide - hide
	$("#" + id).show(); //jquery - element with given id - show
	return;
}

//array shuffle function
shuffle = function(o) { //v1.0, takes in an array of items
	for (var j, x, i = o.length; i; j = parseInt(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
	return o;
}

/*Function: getCurrentDate
  Usage: var date = getCurrentDate();
  Params: none
  Returns: string representing date
  Gets date for timestamp*/
getCurrentDate = function() {
	var currentDate = new Date();
	var day = currentDate.getDate();
	var month = currentDate.getMonth() + 1;
	var year = currentDate.getFullYear();
	return (month + "/" + day + "/" + year);
}

/*Function: getCurrentTime
  Usage: var time = getCurrentTime();
  Params: none
  Returns: string representing time
  Gets date for timestamp*/
getCurrentTime = function() {
	var currentTime = new Date();
	var hours = currentTime.getHours();
	var minutes = currentTime.getMinutes();
	if (minutes < 10) minutes = "0" + minutes;
	return (hours + ":" + minutes);
}

/*Function: getRandomInt
  Usage: ID = getRandomInt();
  Params: none
  Returns a value between a and b (typically 1 and 4) representing
  which trial type will be experienced
  Called when determining which version of the experiment to
  display
*/
function getRandomInt(min, max) {
	var ID = Math.floor(Math.random() * (max - min + 1) + min); //returns tag corresponding to one of our lists/conditions
	return ID;
}

/*Function: getDialogueList
  Usage: getDialogueList()
  Params: none
  Returns: the csv data
*/
function getDialogueList() {
	var data_capsule = [];
	$.ajaxSetup({
		async: false
	}); //allows php to execute fully before returning to javascript to update condArray
	var php_url = "https://langcog.stanford.edu/cgi-bin/NPM_bayesentences/bayesentences_filereading.php";
	var php_filename = "?w1=" + inputfilepath; //this first php param will tell it which file to look in
	var php_filesize = "&w2=" + numCSVRows; //this second php param will tell it how many rows to bring back over
	var total_request = php_url + php_filename + php_filesize;
	console.log(total_request)
	$.get(total_request, function(data) {
		data_capsule = data;
	}, "json");
	console.log(data_capsule);
	return data_capsule;
}

/*Function: createCondition
  Usage: createCondition(data)
  Params: data, the multidimensional array containing condition info
  trial_num, the value from the conditions array that has been randomly selected as next
  retrieved from the .csv
  Returns: condArray, the array governing the info for this trial
*/
function createCondition(data, trial_num) {
	var holder = [];
	holder = data[0][trial_num];
	console.log("holder is " + holder);
	var condArray = holder.split(","); //[0][0] gives you the header row
	for (var i = 0; i < condArray.length; i++) {
		condArray[i] = condArray[i].replace(/"/g, "");
		condArray[i] = condArray[i].replace(/\r/g, "");
	}
	return condArray;
}

/*Function: redrawDialogue
  Usage: redrawDialogue(condArray)
  Params: condArray, array containing info governing the current trial
  Returns: none
  Displays the next dialogue chunk in dynamically created html according to specs from the condArray
  */
function redrawDialogue(condArray, trial) {
	var alternation = condArray[0];
	var utterance = condArray[1];
	var question = condArray[2];
	var alternation_tag = condArray[3];
	var item_number = condArray[4];
	var correct = condArray[5];
	var title_string = "What's going on in the sentence?... &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;" + trial + counter + "</th>";
	document.getElementById("utterance").innerHTML = utterance;
	document.getElementById("question").innerHTML = question;
	document.getElementById("title").innerHTML = title_string;
	return;
}

/*Function: submitData
  Usage: submitData()
  Params: none
  Returns: none
  Submits post request to results php script and ends the experiment
*/
function submitData(expdata) {
	var outfilepath = "bayesentences_" + subjectID + "_Exp1results.csv";
	$("#stage").fadeOut(); //fades out the stage slide
	var submiter = $.post("https://langcog.stanford.edu/cgi-bin/NPM_bayesentences/bayesentences_submit.php", {
		result_file_path: outfilepath,
		postresult_array: experiment_result_array,
	}); //posts the results to the server using php
	$.when(submiter).then(function() {
		turk.submit(expdata, true); //submits demo data to turk
	});
	return;
}

/****************MAIN EXPERIMENT FUNCTION**********************/
/*Note that the entire experiment is contained within the 'experiment'
  variable. There are objects, attributes and functions within the experiment
  function that govern its states and behavior. Think OOP!

  Experiment broken into:
  -training: creates and runs practice trial
  -init: checks for valid credentials, gets csv_data from php as 'data', selects subset of data, shuffles trial order
  -run: for each trial, gets the next row from the shuffled csv data and implements accordingly, saving results to server
  -end: displays closing information
  */

var experiment = { //var containing the experiment, though everything is called from within it
	/*
	  Function: init
	  Usage: experiment.init()
	  Params: none
	  Returns: none
	  Called after training when a trial is about to begin during timeout.
	  Decides which list condition to use.*/
	init: function() { //governs which rubric to follow (voice, trial type, etc)
		data = getDialogueList(); //sets up which experiment we use; calls getWordList
		conditions = shuffle(conditions); //randomizes order of the trials
		return false
	}, //finishes declaration of init method

	/*  Function: training
		Usage: experiment.training()
		Params: data, the csv trial data from the server
		Returns: none
		Will call the createDot(x,y,i) function, calls experiment.next()
	*/
	training: function() {
		$("#loading").fadeOut("fast");
		showSlide("instructions1");

		$('#nextInstructions').one('click', function(event) {
			showSlide("training1");
			$("#radioPractice1").buttonset()
		});

		$('#yesPractice1, #noPractice1').on('click', function(event) {
			showSlide("training2");
			$("#radioPractice2").buttonset()
		});

		$('#yesPractice2, #noPractice2').on('click', function(event) {
			experiment.next(data);
		});
	}, //finishes declaration of training method

	/*Function: next
	  Usage: experiment.next(data)
	  Params: data, the csv trial data from the server
	  Returns none
	  Called when need to get a new trial; first called from experiment.init		
	  First called after init, calls itself until counter === numTrials var set at beginning*/
	next: function(data) { //Will be the main display function
		document.body.style.background = "white"; //makes a white screen for run of experiment; change background color here
		var i = 0;
		trial = conditions[i];
		console.log("trial is " + i);
		var condArray = createCondition(data, trial);
		console.log(condArray);
		redrawDialogue(condArray, i);
		$("#training2").fadeOut("slow");
		$("#ready").fadeIn("fast");
		setTimeout(function() {
			$("#ready").fadeOut("fast");
			$("#stage").fadeIn("fast");
			$("#radioNext").buttonset()
		}, pauseTime * 4);
		var trial_result_array = []; //initializes result_string variable that will hold the result of each trial, to be parsed later
		var subjID = 0;
		var list_number = 1;
		var alternation = 2;
		var item_number = 3;
		var utterance = 4;
		var question = 5;
		var alt_tag = 6;
		var syntax_interpretation = 7;
		var answer = 8;
		var day = 9;
		var time = 10;
		$('#yes, #no').on('click', function(event) {
			var decision = $(this).val()
			console.log(decision)
			if (decision == undefined) { //user didn't pick anything! Silly user...
				alert("What happened in the sentence? Please make a selection!");
			} else { //if the user picked something
				i++; //increments the counter (only way the experiment advances, when they click next)
				console.log("user decision is " + decision);
				trial_result_array[subjID] = subjectID;
				trial_result_array[list_number] = condArray[6];
				trial_result_array[alternation] = condArray[0];
				trial_result_array[item_number] = condArray[4];
				trial_result_array[utterance] = condArray[1];
				trial_result_array[question] = condArray[2];
				trial_result_array[alt_tag] = condArray[3];
				trial_result_array[syntax_interpretation] = condArray[5];
				trial_result_array[answer] = decision;
				trial_result_array[day] = getCurrentDate();
				trial_result_array[time] = getCurrentTime();
				experiment_result_array[i] = trial_result_array; //adds this trials results to the overall result array
				trial_result_array = []; //resets the trial array holder
				/***If experiment complete, submit data to server***/
				if (i === numTrials) { //checks for experiment completion
					// submitData(); //posts using php to server, ends experiment
					setTimeout(function() {
						experiment.end()
					}, 500)
				} else {
					$("#stage").fadeOut("slow");
					trial = conditions[i];
					console.log("attempted trial row is " + trial);
					condArray = createCondition(data, trial);
					console.log(condArray);
					setTimeout(function() {
						redrawDialogue(condArray, i);
						$('#radioNext input').removeAttr('checked');
						$("#radioNext").buttonset('refresh');
						$("#stage").fadeIn("slow");
						console.log("trial is " + i);
					}, pauseTime);
				}
			}
		}); //finishes governing of click response
	}, //finishes declaration of next method

	/*Function: abort
	  Usage: experiment.abort()
	  Params: none
	  Returns: none
	  called when the user has prematurely quit the HIT */
	abort: function() {
		var data_report = "";
		var php_url = "https://langcog.stanford.edu/cgi-bin/NPM_bayesentences/bayesentences_temp_out.php";
		var php_filename = "?w1=" + inputfile; //this first php param will tell it which file to look in
		var php_filesize = "&w2=" + abortfile; //this second php param will tell it how many rows to bring back over
		var total_request = php_url + php_filename + php_filesize;
		$.get(total_request, function(data) {
			data_report = data;
		}, "json");
		console.log("User aborted -- file was in " + inputfile + " + now in " + data_report);
	}, //finishes declaration of abort method

	/*Function: end
	  Usage: experiment.end()
	  Params: none
	  Returns: none
	  called when the number of trials is up; everything's over */
	end: function() { //governs how the experiment will end
		showSlide("finish"); //shows the 'finish' slide from the html file
		console.log(experiment_result_array);
		submitData(experiment_result_array);
			// setTimeout(function() {
			// 	turk.submit(experiment, true);
			// }, 1500);
	}, //finishes declaration of end method
}

showSlide("welcome"); //shows the instructions slide and is ready to start the experiment

//Button is disabled if turk is in preview mode
//Button is also disabled if experiment is not done loading
$("#pleaseWait").html("Please wait while the experiment loads...");
$("#startButton").attr("disabled", true);
var wait = true //keep button disabled until wait == false

//if turk is in preview mode, don't load the data
// once turker has accepted HIT, experimentLoad() is run
//Once data is loaded, wait is set to false and the button is disabled
if (turk.previewMode != true) {
	wait = experiment.init();
}

if (wait == false) {
	$("#startButton").attr("disabled", false);
	$("#pleaseWait").html("");
}