Dropzone.autoDiscover = false;

function init() {
    let dz = new Dropzone("#dropzone", {
        url: "/",
        maxFiles: 1,
        addRemoveLinks: true,
        dictDefaultMessage: "Some Message",
        autoProcessQueue: false,
    });

//This effectively ensures that only one file is allowed in the queue at a time.
dz.on("addfile", function(){
    if(dz.files[1] !=null){
        dz.removeFile(dz.files[0])
    }

});

dz.on("complete", function(file){
    // Extract the data URL
    let converted_image = file.dataURL

    var url = "http://127.0.0.1:5000/classify_image";

    $.post(url, {
        // Converted_image contains based64 string
        images: converted_image
    }, function(data, status){

        console.log(data)
        if(!data || data.length == 0){
            $("#info").show();
            $("#resultHolder").hide();
            $("#divClassTable").hide();
            return;
        }

        let match = null;
        let bestScore = -1;
        let maxScoreForThisClass = null;
        

        for (let i=0; i<data.length; ++i){
            maxScoreForThisClass = Math.max(...data[i].class_probability);
            if (maxScoreForThisClass > bestScore){
                match = data[i]
                bestScore = maxScoreForThisClass
            }
        }
        // Check if there are more than one images
        if (data.length > 1){
            $("#info").hide();
            $("#resultHolder").show();
            $("#divClassTable").show();

            
            sport_person = {}

            
            let combinedHTML = "";

            for (let i = 0; i < data.length; i++) {
                let playerClass = data[i].class;
                let playerHTML = $(`[data-player="${playerClass}"`).html();
                combinedHTML += playerHTML;
            }

            // Add all probability scores
            for (let i in data) {
                for (let name in data[i].class_dictionary) {
                    let index = data[i].class_dictionary[name];
                    let proabilityScore = data[i].class_probability[index];

                    if (!sport_person[name]) {
                        sport_person[name] = [];
                    }
        
                    sport_person[name].push(proabilityScore);
                }
            }
            
            // Retrive all probability scores
            for(let personName in sport_person){
                let proabilityScore = sport_person[personName];
                let score = proabilityScore.join(', ');

                let elementName = "#score_" + personName;
                $(elementName).html(score);
            }

            $("#resultHolder").html(combinedHTML);

        }
        else{
                $("#info").hide();
                $("#resultHolder").show();
                $("#divClassTable").show();
                $("#resultHolder").html($(`[data-player="${match.class}"`).html());
    
                let class_dictionary = match.class_dictionary;
                for(let personName in class_dictionary){
                    let index = class_dictionary[personName];
                    let proabilityScore = match.class_probability[index];
                    
                    let elementName = "#score_" + personName;
                    $(elementName).html(proabilityScore);
                }
        }
    });

});

$("#submitBtn").on('click', function(e){
    // Initiates the uploading of files
    dz.processQueue()
});

}
    
$(document).ready(function(){
    console.log("ready!");
    $("#info").hide();
    $("#resultHolder").hide();
    $("#divClassTable").hide();

    
    init()
});