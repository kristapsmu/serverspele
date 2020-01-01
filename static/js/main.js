	let punkti = 0;
	let kludas = 0;
	let jautajums = 1;
	let par;
	let nep;
	let jau;
	let atb; 
	let karogs; 	 
	function sakt(){
		punkti = 0;
		kludas = 0;
		jautajums = 1;
		// atrod visus objektus
		par = document.getElementById("pareizas");
		nep = document.getElementById("nepareizas");
		jau = document.getElementById("jautajums");
		atb = document.getElementById("atbildes"); 
		karogs = document.getElementById("karogs"); 
		document.getElementById("poga").remove();
		jautajumu(); 
	}
	function jautajumu(){
		
		let atbildenoservera = "";
		$.ajax({url: '/jautajums',"method": "GET","dataType":'html', success: function(result){
		    atbildenoservera = JSON.parse(result);
			let pogas = Array();
			let atbtemp = "";
			let atbindekss = "";
			jau.innerHTML =	jautajums+". jautājums <br> "+atbildenoservera.jautajums;
			karogs.innerHTML =	"<img src='"+atbildenoservera.flag+"'>";
			pogas = atbildenoservera.atbildes.split("|");
			console.log(pogas.length);
			for(let sk = 0; sk < pogas.length;sk++){
		 
				atbtemp += "<button id='atb"+(sk+1)+"' onclick='atbilde("+atbildenoservera.j+","+sk+")'>"+(sk+1)+". "+pogas[sk]+"</button> <br>";
			}
			atb.innerHTML = atbtemp;
			renderlaukums();	
			 
		}});
		 
	}
	function atbilde(j,sk){
 
		 $.ajax({url: '/atbilde?j='+j+'&sk='+sk,"method": "POST","dataType":'html', success: function(result){
			if(result == 1){
				punkti++;	
			    pareiza();
			 }else{
				kludas++;
				nepareiza();
			 }
		 }});
		 jautajums++;
		 if(jautajums > 20){
			 spelesbeigas();
		 }else{
			document.getElementById("atb"+(sk+1)).disabled = true;
			setTimeout(function(){
				jautajumu(); 
			}, 1000);
			 
		 }
		 
	 
	}
	function pareiza(){
		var konteineris = document.getElementById("konteiners");
		konteineris.classList.add("pareiza");
		setTimeout(function(){
		   konteineris.classList.remove("pareiza");
		}, 1000);
	}
	function nepareiza(){
		 var konteineris = document.getElementById("konteiners");
		konteineris.classList.add("nepareiza");
		setTimeout(function(){
		   konteineris.classList.remove("nepareiza");
		}, 1000);
		
	}
	function renderlaukums(){
		
		par.innerHTML = "Pareizas atbildes:"+punkti;
		nep.innerHTML = "Nepareizas atbildes:"+kludas;
		
	}
	function spelesbeigas(){
		document.getElementById("konteiners").innerHTML = "";
		document.getElementById("konteiners").innerHTML = "<h1> Spēles beigas! Jūs atbildējāt pareizi uz "+punkti+" jautājumiem, kļūdijāties "+kludas+".</h1> ";
		document.getElementById("konteiners").innerHTML += '<button onClick="window.location.href=window.location.href"> Sākt no jauna</button>';
	 
		
	}
