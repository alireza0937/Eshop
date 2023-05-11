from django import forms


class CommentForm(forms.Form):
    message = forms.Textarea()

    def __str__(self):
        return self.message
