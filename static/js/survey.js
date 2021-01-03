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