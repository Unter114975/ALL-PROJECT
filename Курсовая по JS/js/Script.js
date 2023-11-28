	<script>
		
		$(document).ready(function() {
			$(".flip1").click(function(){
				$(".panel1").slideToggle("slow");
			});
			
		});
		//-----------------------------
		$(document).ready(function() {
			$(".flip2").click(function(){
				$(".panel2").slideToggle("slow");
			});
			
		});
		//-----------------------------
		$(document).ready(function() {
			$(".flip3").click(function(){
				$(".panel3").slideToggle("slow");
			});
			
		});
			//-----------------------------
		$(document).ready(function() {
			$(".flip4").click(function(){
				$(".panel4").slideToggle("slow");
			});
			
		});
		//------------------------------------------------
		$(document).ready(function() {
			$(".flip5").click(function(){
				$(".panel5").slideToggle("slow");
			});
			
		});
		//------------------------------------------------
		$(document).ready(function() {
			$(".flip6").click(function(){
				$(".panel6").slideToggle("slow");
			});
			
		});
		//------------------------------------------------
		$(document).ready(function() {
			
			$("button").click(function(){
				$("#nav").slideToggle("slow");
			});
			
		});
		
//-------------------------------------------------------------

			var
				direction1 = document.querySelector('#direction1'),
				direction2 = document.querySelector('#direction2'),
				range = document.querySelector('#range'),
				rasstoyanie = document.querySelector('.rasstoyanie').innerHTML = 6,
				itog = document.querySelector('#itog');
				
				var	prices = {
				1:{1:1, 2:1, 3:1.5, 4:2},
				2:{1:1, 2:1, 3:1.5, 4:2, 5:2.5},
			};	
				
				
				range.onchange = function(){
				rasstoyanie = document.querySelector('.rasstoyanie').innerHTML = range.value;
				console.log(range.value)
				itog.value = range.value*10000;	
				};	
			
				direction1.onchange = function(){
				console.log(prices[1][direction1.value]);
				itog.value = (range.value*10000)*(prices[1][direction1.value]);
				};
			
				direction2.onchange = function(){
				console.log(prices[2][direction2.value]);
				itog.value = (range.value*10000)*(prices[2][direction2.value]);
				};
			
			
			//var sum = 1; /*prices[direction1]+prices[direction2]+;*/
			//total-price.innerHTML = sum;
			
			//direction2.onchange = function{
		   // itog.innerHTML = sum;
			//}	
				
	//</script>
	//<script>
	var Error1 = document.querySelector('#Error1'),
	    Error2 = document.querySelector('#Error2'),
	    Error3 = document.querySelector('#Error3'),
	    Error4 = document.querySelector('#Error4'),
	    Error5 = document.querySelector('#Error5'),
	    Error6 = document.querySelector('#Error6'),
	    Error7 = document.querySelector('#Error7'),
	    itog2 = document.querySelector('#itog2'),
		btn = document.querySelector('#btn');

		btn.onclick = function(){
					var	Err1=0,Err2=0,Err3=0,Err4=0,Err5=0,Err6=0,Err7=0;
					//console.log(num);
					if (Error1.checked){
					     Err1 = 1000;}
					if (Error2.checked){
						 Err2 = 1000;}
					if (Error3.checked){
						 Err3 = 1000;}
					if (Error4.checked){
						 Err4 = 1000;}
					if (Error5.checked){
						 Err5 = 1000;}
					if (Error6.checked){
						 Err6 = 1000;}
					if (Error7.checked){
						 Err7 = 1000;}
					var sum = Err1+Err2+Err3+Err4+Err5+Err6+Err7;
						
					//console.log(sum);
				   itog2.value = sum;
			}

	//</script>
	//<script>
		var $dir = $('#direction3'),
		$itog3 = $('#itog3');
		var ceni = {1:20000, 2:5000, 3:50000, 4:30000};
		
		
		function upd(){	
				var 
				dir = $dir.val();
				$itog3.val(ceni[dir]);
			}
			$dir.on('change', upd);
		
		
	//---------------------------------
		//var image = document.getElementById('.header__blok2');
     //   var images = ['eks8.jpg', 'Home2-1.jpg'];
      //  var a = 0;
 
     //   function SetImage() {
     //       if (a == 0) {
     //          image.setAttribute('src', images[1]);
     //          a = 1;
      //     } 
      //    else {
      //          image.setAttribute('src', images[1]);
      //         a = 0;
      //      }
 
      //  }
 
      //  setInterval(SetImage(), 1000);
		
</script>