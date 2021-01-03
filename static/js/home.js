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
