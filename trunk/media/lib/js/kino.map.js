/**
 * @author phaenotyp
 */


var kinoMaps = {
	
			loadMaps: function () {
			
  		google.load("maps", "2", {"callback" : kinoMaps.initialize});
		
	},
	
	initialize: function(){
		
		
		
		
		if (GBrowserIsCompatible()) {
			
			var map = new GMap2(document.getElementById("map"));
			var markers = [];
			map.setCenter(new GLatLng(50.940664, 6.959912), 13);
			map.addControl(new GLargeMapControl());
  			map.addControl(new GMapTypeControl());
			
			
			
			for (var i = 0; i < kinoGeo.kinos.length; i++) {
			
				if (kinoGeo.kinos[i].geo) {
				
					var kinoSpot = new GLatLng(kinoGeo.kinos[i].geo.lat, kinoGeo.kinos[i].geo.lng);
					
					
					map.addOverlay(kinoMaps.createMarker(kinoSpot));

				}
			}
			
		}
	},
	
	       // Creates a marker whose info window displays the letter corresponding
        // to the given index.
     createMarker:   function (point) {
	 	

          var marker = new GMarker(point);

          GEvent.addListener(marker, "click", function() {
            marker.openInfoWindowHtml("Marker <b></b>");
          });
          return marker;
        }
	
}

 
		  
		  
		  
google.setOnLoadCallback(kinoMaps.loadMaps);		  