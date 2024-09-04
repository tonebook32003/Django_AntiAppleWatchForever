from django.forms.widgets import ClearableFileInput


class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        attrs["multiple"] = True
        return super().render(name, value, attrs, renderer)
