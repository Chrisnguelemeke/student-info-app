from django.shortcuts import render
from .forms import StudentForm


def student_form(request):
    if request.method == 'POST':
        # The user clicked Submit: fill the form with what they entered
        form = StudentForm(request.POST)

        if form.is_valid():
            # Validation passed: collect the values and send them to the results page
            data = form.cleaned_data
            context = {
                'name': data['student_name'],
                'student_id': data['student_id'],
                'major': data['major'] or 'Not selected',
                'standing': data['class_standing'] or 'Not selected',
                'languages': ', '.join(data['languages']) or 'None',
                'grad_year': data['graduation_year'] or 'Not entered',
                'comments': data['comments'] or 'None',
            }
            return render(request, 'students/results.html', context)
        # Validation failed: show the form again with error messages
    else:
        # First visit: show an empty form
        form = StudentForm()

    return render(request, 'students/form.html', {'form': form})