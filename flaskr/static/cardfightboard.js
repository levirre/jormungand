$(document).ready(function(){
	for(let i=0;i< p1.hand.length;i++){
  	var card = document.createElement("div");
  	card.classList.add("card");
		$(".hand").append(card);
    
    
    
    
  }
  $('.card').each(function(i, obj) {
   $(this).css({color: p1.hand[i].color});
   $(this).append('<p>' + p1.hand[i].value+'</p>');
   $(this).append('<p>' + p1.hand[i].suit+'</p>');
   $(this).append('<div class=mirror><p class=flipVH>' + p1.hand[i].suit+'</p>' +'<p class=flipVH>'+p1.hand[i].value+ '</p>'+ '</div');
  
	});
 
});