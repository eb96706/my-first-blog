from django.shortcuts import render

def post_list(request):
	return render(request, 'blog/post_list.html', {})

	'''
	function post_list takes request and return a function render our template blog/post_list.html

	Another error
	This one is easy: TemplateDoesNotExist. 
	Let's fix this bug and create a template in the next chapter!
	'''
