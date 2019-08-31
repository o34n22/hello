import question_generator


@app.route('/some_user/some_task')
def task():
	if next_question == True:
		generate new question
	instantiate webform
	if answer submitted:
		if answer == solution:
			log time
			next_question = True
		else: (answer == some crap)
			send answer to Houston and get message
			flash message
			next_question = False
		return redirect to same page
			
	return render_template with webform and question		
