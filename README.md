## Feedback

### trig.py

* Good!
* Minor suggestion: You can make the code slightly cleaner by taking advantage of the python `for`-loop:

		for yi in y:
			counter += dx * yi

### data_analysis.py

* Very good!
* Cool numpy trick to set certain values to zero in one line:

		sorted_y[clean_freq > threshold_freq] = 0
