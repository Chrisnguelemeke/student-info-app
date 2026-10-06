from django import forms

MAJOR_CHOICES = [
    ('', '-- Select a major --'),
    ('Computer Science', 'Computer Science'),
    ('Information Technology', 'Information Technology'),
    ('Cybersecurity', 'Cybersecurity'),
    ('Business', 'Business'),
    ('Nursing', 'Nursing'),
]

STANDING_CHOICES = [
    ('Freshman', 'Freshman'),
    ('Sophomore', 'Sophomore'),
    ('Junior', 'Junior'),
    ('Senior', 'Senior'),
]

LANGUAGE_CHOICES = [
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('C++', 'C++'),
    ('JavaScript', 'JavaScript'),
    ('SQL', 'SQL'),
]


class StudentForm(forms.Form):
    student_name = forms.CharField(
        label='Student Name',
        max_length=100,
        widget=forms.TextInput(),
        error_messages={'required': 'Student Name cannot be blank.'},
    )
    student_id = forms.CharField(
        label='Student ID',
        max_length=20,
        widget=forms.TextInput(),
        error_messages={'required': 'Student ID cannot be blank.'},
    )
    major = forms.ChoiceField(
        label='Major',
        choices=MAJOR_CHOICES,
        required=False,
        widget=forms.Select(),
    )
    class_standing = forms.ChoiceField(
        label='Class Standing',
        choices=STANDING_CHOICES,
        required=False,
        widget=forms.RadioSelect(),
    )
    languages = forms.MultipleChoiceField(
        label='Programming Languages Known',
        choices=LANGUAGE_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple(),
    )
    graduation_year = forms.IntegerField(
        label='Expected Graduation Year',
        required=False,
        min_value=2024,
        max_value=2040,
        widget=forms.NumberInput(),
    )
    comments = forms.CharField(
        label='Comments',
        required=False,
        widget=forms.Textarea(attrs={'rows': 4}),
    )