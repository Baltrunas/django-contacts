

	def get_form(self, initial=None):
		exclude_field = ['user', 'site', 'config']
		if not self.phone:
			exclude_field.append('phone')
			phone_field = False
		else:
			phone_field = forms.CharField(label=_('Phone'), max_length=200, widget=forms.TextInput(attrs={'required': 'required', 'placeholder': self.phone_placeholder}), required=True)

		if not self.email:
			exclude_field.append('email')
			email_field = False
		else:
			email_field = forms.EmailField(label=_('E-Mail'), max_length=200, widget=forms.TextInput(attrs={'type': 'email', 'required': 'required', 'placeholder': self.email_placeholder}), required=True)

		if not self.comment:
			exclude_field.append('comment')
			comment_field = False
		else:
			comment_field = forms.CharField(label=_('Comment'), widget=forms.Textarea(attrs={'placeholder': self.comment_placeholder}), required=True)

		config_field = forms.CharField(widget=forms.HiddenInput(), initial=self.id)

		class RequestForm(forms.ModelForm):
			config = config_field
			name = forms.CharField(label=_('Name'), max_length=200, widget=forms.TextInput(attrs={'required': 'required', 'placeholder': _('Name')}))

			if phone_field:
				phone = phone_field

			if email_field:
				email = email_field

			if comment_field:
				comment = comment_field

			class Meta:
				model = Request
				exclude = exclude_field

		return RequestForm(initial)
