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

	// Use select2 for select fields
	$('select').select2({
		closeOnSelect: false,
		minimumResultsForSearch: 10
	});

	// Tablesorter
	$('table.sortable').tablesorter({
		cssAsc: 'header-sort-up',
		cssDesc: 'header-sort-down'
	});

	// /cards/ popouts
	$('.card-grid .card').click(function() {
		console.log($(this).data('card'));
	});
});
