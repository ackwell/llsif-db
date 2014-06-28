$(function() {
	var appealSuffixMap = {
		score: 'points',
		health: 'HP',
		perfect: 'seconds'
	}

	function updateAppealEffectSuffix() {
		var $this = $(this);
		$this
			.closest('.row')
			.find('.appeal-effect-modifier .suffix')
			.text(appealSuffixMap[$this.val()]);
	}

	// Potentially loaded via ajax, need to hook all events
	$(document).on('change', '.appeal-effect', updateAppealEffectSuffix);

	// Use select2 for large select fields
	$('.select2').select2();
});
