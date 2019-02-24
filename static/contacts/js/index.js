$(function() {

	$('.form--contacts .button--submit').on('click', function(e) {
		$this = $(this);
		var disabled = $this.attr('disabled');

		if (disabled != 'disabled') {
			$this.attr('disabled', 'disabled');

			var form = $this.closest('.form--contacts');
			var form_date = form.serialize();
			var url_send = form.data('url_send');

			$.post(url_send, form_date).done(function(data) {
				console.log(data);

				if (data.status == 'sent') {
					$(form).addClass('form--status_sent');
					$(form).removeClass('form--status_error');
				} else {
					$(form).addClass('form--status_error');
					$(form).removeClass('form--status_sent');

					$('.field .field__errors').empty();
					form.find('.field').removeClass('field--error');
					form.find('.field').addClass('field--valid');

					for (var field in data.errors) {
						errors_list = form.find('.field--' + field + ' .field__errors');
						errors_list.empty();


						form.find('.field--' + field).addClass('field--error');
						form.find('.field--' + field).removeClass('field--valid');

						for (var error in data.errors[field]) {
							error_text = data.errors[field][error];
							$('<li class="field__errors_error">' + error_text + '</li>').appendTo(errors_list);
						}
						console.log(errors_list);
					} // end for data.errors
				}
				$this.removeAttr('disabled');
			}); // end ajax
		} // end disable check

		e.preventDefault();
	}); // end on click


	$('.form--contacts input, .form--contacts textarea').on('change', function(e) {
		$this = $(this);

		var form = $this.closest('.form--contacts');
		var form_date = form.serialize();
		var url_validate = form.data('url_validate');

		$.post(url_validate, form_date).done(function(data) {
			console.log(data);

			if (data.errors.hasOwnProperty($this.attr('name'))) {
				console.log(data.errors[$this.attr('name')]);
				$this.closest('.field').removeClass('field--valid');
				$this.closest('.field').addClass('field--error');

				errors_list = $this.closest('.field').find('.field__errors')
				errors_list.empty();

				for (var error in data.errors[$this.attr('name')]) {
					error_text = data.errors[$this.attr('name')][error];
					$('<li class="field__errors_error">' + error_text + '</li>').appendTo(errors_list);
				}
			} else {
				$this.closest('.field').find('.field__errors').empty();
				$this.closest('.field').removeClass('field--error');
				$this.closest('.field').addClass('field--valid');
			}

			if(! data.errors) {
				form.removeClass('form--status_error');
			}

		}); // end ajax

		e.preventDefault();
	}); // end on click


});
