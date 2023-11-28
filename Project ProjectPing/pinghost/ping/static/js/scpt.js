	$(document).ready(function() {
			
		
		
			$(".slovar").click(function(){
				$(".footer__slovar").slideToggle("slow");
			});
			
			$(".programm").click(function(){
				$(".footer__programm").slideToggle("slow");
			});
			
			
			$(".Menu").click(function(){
				$(".footer__Menu").slideToggle("slow")});
			
		});
		
	function myFunction(x) {
    	x.classList.toggle("change");
    	}
    	
   		function myFunction2() {
    	document.getElementById("myDropdown").classList.toggle("show");
    	}
    	
    	
    	window.onclick = function(event) {
  			if (!event.target.matches('.dropbtn')) {
				var dropdowns = document.getElementsByClassName("dropdown-content");
				var i;
    			for (i = 0; i < dropdowns.length; i++) {
      				var openDropdown = dropdowns[i];
      				if (openDropdown.classList.contains('show')) {
        		openDropdown.classList.remove('show');
      			}
    		}
  		}
		}
    	