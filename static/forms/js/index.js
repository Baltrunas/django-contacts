$(function() {

	$(document).on('click', '.b-form__submit', function(e) {
		$this = $(this);
		var disabled = $this.attr('disabled');

		if (disabled != 'disabled') {
			$this.attr('disabled', 'disabled');
			var url = $this.data('url');
			var form = $this.data('form');
			var form_date = $(form).serialize();

			$.post(url, form_date).done(function(data) {
				console.log(data);
				if (data.send) {
					$(form).hide();
					$(form).next('.b-form__tnx_message').show();
				} else {

					for (var field in data.errors) {
						errors_list = $(form + ' #id_' + field)
							.parent()
							.parent()
							.find('.b-field__errors');

						errors_list.empty();


						for (var error in data.errors[field]) {
							error_text = data.errors[field][error];
							$('<li class="b-field__errors_error">' + error_text + '</li>').appendTo(errors_list);
						}

						errors_list.fadeIn(300).fadeOut(2000);
					} // end for data.errors
				}
				$this.removeAttr('disabled');
			}); // end ajax
		} // end disable check

		e.preventDefault();
	}); // end on click

});
