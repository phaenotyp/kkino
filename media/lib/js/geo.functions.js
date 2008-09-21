/**
 * @author phaenotyp
 */

 var MlMup = {
		
		 mapsLoaded: function() {
  	         
                // if lat/long are set in the profile initialy zoom there
                // if not center cologne.
                var lat = document.getElementById("lat").value || 50.940664;
                var lon = document.getElementById("long").value  || 6.959912; 
                         
 
		MlMup.map = new google.maps.Map2(document.getElementById("map"));
 		MlMup.map.setCenter(new google.maps.LatLng(lat, lon), 13);
  		MlMup.map.addControl(new GLargeMapControl());
  		MlMup.map.addControl(new GMapTypeControl());
 		if (google.loader.ClientLocation){
 			MlMup.map.setCenter(
                new google.maps.LatLng(
                    google.loader.ClientLocation.latitude,
                    google.loader.ClientLocation.longitude
                ), 13
            );


 		MlMup.map.addOverlay(new GMarker(new google.maps.LatLng(
                    google.loader.ClientLocation.latitude,
                    google.loader.ClientLocation.longitude)),
					{draggable: true}
					);
					
		document.getElementById('long').value = google.loader.ClientLocation.longitude ;
    	document.getElementById('lat').value =  google.loader.ClientLocation.latitude;
		
		GEvent.addListener(MlMup.map,"click", function(overlay,latlng) {     
          if (latlng) {  
		    
			 
            var myHtml = "The GLatLng value is: " + MlMup.map.fromLatLngToDivPixel(latlng) + " at zoom level " +  MlMup.map.getZoom();
            MlMup.map.openInfoWindow(latlng, myHtml);
			
			document.getElementById('lat').value = latlng.lat();
			document.getElementById('long').value = latlng.lng();
			
          }
        });
        

		
						
					
 }

},
    showLocation: function () {
	  
	
      var address = document.forms[0].q.value;
      MlMup.geocoder.getLocations(address, MlMup.addAddressToMap);
    },

		findLocation: function(address){
			document.forms[0].q.value = address;
      		MlMup.showLocation();
			
		},

		loadMaps: function () {
			
  		google.load("maps", "2", {"callback" : MlMup.mapsLoaded});
		MlMup.geocoder = new GClientGeocoder();
},
    addAddressToMap: function (response) {
		
      MlMup.map.clearOverlays();
      if (!response || response.Status.code != 200) {
        alert("Sorry, we were unable to geocode that address");
      } else {
        place = response.Placemark[0];
        point = new GLatLng(place.Point.coordinates[1],
                            place.Point.coordinates[0]);
		
        marker = new GMarker(point);
        MlMup.map.addOverlay(marker);
		marker.openInfoWindowHtml(place.address + '<br>');
        document.getElementById('long').value = place.Point.coordinates[1] ;
        document.getElementById('lat').value = place.Point.coordinates[0];
      }
    }
		
	};
	








      google.setOnLoadCallback(MlMup.loadMaps);

