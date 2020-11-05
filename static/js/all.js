try {
    var userBenefit = document.getElementById("user-benefit");
    var userBenefitData = document.getElementById("user-benefit-data");
    var docBenefit = document.getElementById("doc-benefit");
    var docBenefitData = document.getElementById("doc-benefit-data");
    var userMore = document.getElementById("user-more");
    var docMore = document.getElementById("doc-more");

    window.addEventListener("load", function (e) {
        userBenefitData.style.display = "block";
        docBenefitData.style.display = "none";
    });
    userMore.addEventListener("click", function (e) {
        docBenefitData.style.display = "none";
        userBenefitData.style.display = "block";
    });
    docMore.addEventListener("click", function (e) {
        userBenefitData.style.display = "none";
        docBenefitData.style.display = "block";
    });
} catch (err) {
    console.log("hecne olmuyub")
}


try {
    $(document).ready(function () {
        if ($("#id_gender").val() == "F") {
            $("#female-only-survey").show();
        } else {
            $("#female-only-survey").hide();
        }

        $("#id_gender").change(function () {
            if ($("#id_gender").val() == "F") {
                $("#female-only-survey").show();
            } else {
                $("#female-only-survey").hide();
            }
        })

    });

} catch (err) {
    console.log("survey error");
}


try {
    let url = $("#personForm").attr("data-cities-url");
    $(document).ready(function () {
        if ($("#id_country").val() == 1) {
            $("#city2_country").css("display", "none");
            $("#turkey_based").show();
            $.ajax({
                url: url,
                success: function (data) {
                    $("#id_city").html(data);
                }
            });

        } else {
            $("#turkey_based").hide();
            $("#city_country").css("display", "none").removeAttr('required');
            $("#city2_country").css("display", "block");
        }
        $("#id_country").change(function () {
            if ($("#id_country").val() == 1) {
                $("#turkey_based").show();
                $.ajax({
                    url: url,
                    success: function (data) {
                        $("#id_city").html(data);
                    }
                });
                $("#city2_country").css("display", "none");
                $("#city_country").show();

            } else {
                $("#turkey_based").hide();
                $("#city_country").css("display", "none").removeAttr('required');
                $("#city2_country").css("display", "block");
            }
        })
    });
} catch (err) {
    console.log("shh");
}

try{
    $("#id_city").change(function () {
      var url = $("#personForm").attr("data-districts-url");  // get the url of the `load_cities` view
      var cityID = $(this).val();  // get the selected country ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'city': cityID       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_cities` view function
          $("#id_district").html(data);  // replace the contents of the city input with the data that came from the server
        }
      });

    });
}catch (err){
    console.log("shh");
}