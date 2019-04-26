var dbPromise = idb.open('productos-db', 1, function(upgradeDb) {
	upgradeDb.createObjectStore('productos',{keyPath:'pk'});
});

fetch('http://localhost:8000/getdata').then(function(response){
	return response.json();
}).then(function(jsondata){
	dbPromise.then(function(db){
		var tx = db.transaction('productos', 'readwrite');
		var productosStore = tx.objectStore('productos');
		for(var key in jsondata){
			if (jsondata.hasOwnProperty(key)) {
				productosStore.put(jsondata[key]); 
			}
		}
	});
});
var post="";
dbPromise.then(function(db){
	var tx = db.transaction('productos', 'readonly');
	var productosStore = tx.objectStore('productos');
	return productosStore.openCursor();
}).then(function logItems(cursor) {
	if (!cursor) {
		if (!navigator.onLine) {
			document.getElementById('offlinedata').innerHTML=post;
		}
		return;
	}
	for (var field in cursor.value) {
		if(field=='fields'){
			productosData=cursor.value[field];
			for(var key in productosData){
				if(key =='nombre'){
					var nombre = '<h3>'+productosData[key]+'</h3>';
				}
				if(key =='precio'){
					var precio = productosData[key];
				}
				if(key == 'cantidad'){
					var cantidad = '<p>'+productosData[key]+'</p>';
				} 
			}
			post=post+'<br>'+nombre+'<br>'+precio+'<br>'+cantidad+'<br>';
		}
	}
	return cursor.continue().then(logItems);
});