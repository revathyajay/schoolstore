from .models import Department, Course, Details
from django import forms




class RegForm(forms.ModelForm):
    MATERIAL_CHOICES = (
        ('1', 'Note Book'),
        ('2', 'Pen'),
        ('3', 'Exam Papers'),
        ('4', 'Drafter'),
        ('5', 'Lab Materials'),
    )
    material_choices = forms.MultipleChoiceField(choices=MATERIAL_CHOICES,
                                         widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = Details
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
