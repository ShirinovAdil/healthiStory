if (document.getElementById("user-benefit-data")) {

    let userBenefitData = document.getElementById("user-benefit-data");
    let docBenefitData = document.getElementById("doc-benefit-data");
    let userMore = document.getElementById("user-more");
    let docMore = document.getElementById("doc-more");

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
}


try {
    $(document).ready(function () {
        if ($("#id_gender").val() === "F") {
            $("#female-only-survey").show();
        } else {
            $("#female-only-survey").hide();
        }

        $("#id_gender").change(function () {
            if ($("#id_gender").val() === "F") {
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
        if ($("#id_country").val() === "1") {
            $("#city2_country").css("display", "none");
            $("#turkey_based").show();
            $.ajax({
                url: url,
                success: function (data) {
                    $("#id_city").html(data);
                }
            }).done(function () {
                let url = $("#personForm").attr("data-districts-url");
                $.ajax({
                    url: url,
                    data: {
                        'city': $("#id_city").val()
                    },
                    success: function (data) {
                        $("#id_district").html(data);
                    }
                });
            });
        } else {
            $("#turkey_based").hide();
            $("#city_country").css("display", "none");
            $("#city2_country").css("display", "block");
        }
        $("#id_country").change(function () {
            if ($("#id_country").val() === "1") {
                $("#turkey_based").show();
                $("#city2_country").css("display", "none");
                $("#city_country").show();
                $.ajax({
                    url: url,
                    success: function (data) {
                        $("#id_city").html(data);
                    }
                });
            } else {
                $("#turkey_based").hide();
                $("#city_country").css("display", "none");
                $("#city2_country").css("display", "block");
            }
        })
    });
} catch (err) {
    console.log(err);
}

try {
    $("#id_city").change(function () {
        let url = $("#personForm").attr("data-districts-url");
        let cityID = $("#id_city").val();
        $.ajax({
            url: url,
            data: {
                'city': cityID
            },
            success: function (data) {
                $("#id_district").html(data);
            }
        });
    });
} catch (err) {
    console.log(err);
}