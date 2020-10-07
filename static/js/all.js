try{
        var userBenefit = document.getElementById("user-benefit");
        var userBenefitData = document.getElementById("user-benefit-data");
        var docBenefit = document.getElementById("doc-benefit");
        var docBenefitData = document.getElementById("doc-benefit-data");
        var userMore = document.getElementById("user-more");
        var docMore = document.getElementById("doc-more");
 
        window.addEventListener("load", function(e){
            userBenefitData.style.display = "block";
            docBenefitData.style.display = "none";
        });
        userMore.addEventListener("click", function(e){
            docBenefitData.style.display = "none";
            userBenefitData.style.display = "block";
        });
        docMore.addEventListener("click", function(e){
            userBenefitData.style.display = "none";
            docBenefitData.style.display = "block";
        }); }
        catch(err){
            console.log("hecne olmuyub")
        }


try{
    $(document).ready(function(){
        if ($("#inputGender").val() == "female"){
            $("#female-only-survey").show();
        }else{
            $("#female-only-survey").hide();
        }

        $("#inputGender").change(function(){
            if ($("#inputGender").val() == "female"){
                $("#female-only-survey").show();
            }else{
                $("#female-only-survey").hide();
            }
        })

    });

    }catch(err){
        console.log("survey error");
    }
    
    