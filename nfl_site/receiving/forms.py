from django import forms


class ReceiveForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)


class AddReceivingPlayForm(forms.Form):
    first_name_add = forms.CharField(max_length=100)
    last_name_add = forms.CharField(max_length=100)


class TopReceiveForm(forms.Form):
    player_num = forms.IntegerField(label='Number of players', max_value=100, min_value=1)
