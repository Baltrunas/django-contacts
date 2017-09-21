$(function() {

	$('.form .button[name=submit]').on('click', function(e) {
		$this = $(this);
		var disabled = $this.attr('disabled');

		if (disabled != 'disabled') {
			$this.attr('disabled', 'disabled');
			var form_url = $this.data('url');
			var form_block = $('.form--' + $this.data('form'));
			var form_form = $('#form-' + $this.data('form'));
			var form_date = form_form.serialize();

			$.post(form_url, form_date).done(function(data) {
				console.log(data);

				if (data.send) {
					$(form_block).addClass('form--sended');
				} else {
					for (var field in data.errors) {
						errors_list = form_block.find('.field--' + field + ' .field__errors');
						errors_list.empty();

						for (var error in data.errors[field]) {
							error_text = data.errors[field][error];
							$('<li class="field__errors_error">' + error_text + '</li>').appendTo(errors_list);
						}
						console.log(errors_list);

						// errors_list.fadeIn(300).fadeOut(2000);
					} // end for data.errors
				}
				$this.removeAttr('disabled');
			}); // end ajax
		} // end disable check

		e.preventDefault();
	}); // end on click

});
