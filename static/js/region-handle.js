function loadRegions() {
    var map = {
        "Europe" : ["UK", "London", "Central", "Ireland", "Scotland", "Holland", "Germany", "Switserland", "Spain", "Russia", "Sweden", "Denmark", "Hong Kong", "South Africa"],
        "Pacific North" : ["Alaska","British Columbia","Idaho","Northern Alberta","Northern California","Northern Nevada","Oregon/Southwest Washington","Southern Alberta","Utah","Washington"],
        "Pacific South" : ["Antilope Valley","Hawaii","Nevada","Online","Central California","Inland Empire","Los Angeles","Orange County","San Diego","San Fernando Valley","San Gabriel/Pomona Valley","Southern Nevada","West Inland"],
        "Atlantic North" : ["Canadian Maritimes","Connecticut","Massachusetts","New York","Northern New England","Eastern Pennsylvania/New Jersey/Delaware","Quebec","Rhode Island","Southern Ontario","Washington, D.C."],
        "Atlantic South" : ["Alabama","Arkansas","Florida","Georgia","North Carolina","Louisiana","Tennessee","South Carolina","Virginia","Peru"],
        "Mid West" : ["llinois","Indiana","Kentucky","Manitoba","Michigan","Minnesota","Missouri","Nebraska","Ohio","Wisconsin"],
        "South West" : ["Arizona","Colorado","Kansas","New Mexico","Oklahoma","North Texas","Texas","South Central Texas","Southern Colorado","Valley Area of Texas"],
    }
    
    var curr_region = [];
    var region_field = document.getElementById('id_region');
    var area_field = document.getElementById('id_area');
    region_field.type = 'select'
    console.log(region_field)
    while (region_field.firstChild) {
        region_field.removeChild(region_field.firstChild);
    }
    for (var key in map) {
        var el = document.createElement("option");
        el.textContent = key;
        el.value = key;
        region_field.appendChild(el)
    }
    function getAreas() {
        curr_region = map[region_field.value];
        console.log(curr_region)
        while (area_field.firstChild) {
            area_field.removeChild(area_field.firstChild);
        }
        for(var i = 0; i < curr_region.length; i++) {
            var el = document.createElement("option");
            el.textContent = curr_region[i];
            el.value = curr_region[i];
            area_field.appendChild(el)
        }
    }
    getAreas();
    region_field.onchange = function() {
        getAreas();
    }


    console.log("Run")
}


window.onload = setTimeout(function() {
    loadRegions();
}, 1000)