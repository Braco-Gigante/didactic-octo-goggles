document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
});


$(document).ready(function(){
    $('.modal').modal();
    $('.chips').chips();
    $('.chips-placeholder').chips({
    	placeholder: 'Digite as tags',
    	secondaryPlaceholder: '+Tag',
  	});
  	
  	maxD = new Date();
  	
    $('.datepicker').datepicker({
    	format: 'yyyy-mm-dd',
    	maxDate: maxD,
    	yearRange: [1950, maxD.getFullYear()],
    });
   
	$('#excluir-links').click(function(){
		$('.open-link').addClass("vanish");
		$('.exclude-link').removeClass("vanish");
		$(this).addClass("vanish");
		$("#voltar-links").removeClass("vanish");
	});
	$('#voltar-links').click(function(){
		$('.open-link').removeClass("vanish");
		$('.exclude-link').addClass("vanish");
		$(this).addClass("vanish");
		$("#excluir-links").removeClass("vanish");
	});

	$('#excluir-lists').click(function(){
		$('.open-list').addClass("vanish");
		$('.exclude-list').removeClass("vanish");
		$(this).addClass("vanish");
		$("#voltar-lists").removeClass("vanish");
	});
	$('#voltar-lists').click(function(){
		$('.open-list').removeClass("vanish");
		$('.exclude-list').addClass("vanish");
		$(this).addClass("vanish");
		$("#excluir-lists").removeClass("vanish");
	});

	$('#excluir-summaries').click(function(){
		$('.open-summary').addClass("vanish");
		$('.exclude-summary').removeClass("vanish");
		$(this).addClass("vanish");
		$("#voltar-summaries").removeClass("vanish");
	});
	$('#voltar-summaries').click(function(){
		$('.open-summary').removeClass("vanish");
		$('.exclude-summary').addClass("vanish");
		$(this).addClass("vanish");
		$("#excluir-summaries").removeClass("vanish");
	});

	$('.erou').children('input').addClass('invalid');
	$('.erou').children('input').focusout(function(){
		$(this).removeClass("valid");
		$(this).parent().children('span').addClass('vanish');
	})
	$('.erou').children('input').focusin(function(){
	 	$(this).removeClass('invalid');
	});
	
	$('li[tabindex = \'0\'].selected').addClass('disabled');	
});
