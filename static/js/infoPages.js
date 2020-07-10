/* ########################### scroll down button ########################### */


// time to scroll down in milliseconds
const scrollDownTime = 800;

// how far down the page it scrolls
scrollDistance =
$("#scrollStopHere").offset().top - parseInt($("#scrollStopHere").css("margin-top"), 10);

goDownToContent = () => $("html, body").animate({
  scrollTop: scrollDistance
}, scrollDownTime);



/* ######################## social media icons hover ######################## */


if (window.location.pathname === "/") {
  var emailSVG, emailPopup, copySVG, emailAddressText, phoneSVG, phonePopup;

  emailSVG =          document.getElementById("email-svg");
  emailPopup =        document.getElementById("email-popup");
  copySVG =           document.getElementById("copy-svg");
  emailAddressText =  document.getElementById("email-address");

  phoneSVG =          document.getElementById("phone-svg");
  phonePopup =        document.getElementById("phone-popup");


  // mouse hovers over email svg icon
  emailSVG.addEventListener("mouseenter", e => {
    emailPopup.style.display = "flex";
    copySVG.style.cursor = "pointer";
  });

  // mouse leaves the email popup
  emailPopup.addEventListener("mouseleave", e => {
    emailPopup.style.display = "none";
    copySVG.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-copy"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>`;
    window.getSelection().removeAllRanges();
  });

  // user clicks the copy icon
  copySVG.addEventListener("click", e => {
    // highlight the text
    var range = document.createRange();
    range.selectNode(emailAddressText);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    // copy the text
    document.execCommand("copy");
    // turn icon into a checkmark
    copySVG.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-check"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
    // cursor back to normal
    copySVG.style.cursor = "auto";
  });


  // mouse hovers over phone svg icon
  phoneSVG.addEventListener("mouseenter", e => {
    phonePopup.style.display = "flex";
  });

  // mouse leaves the phone popup
  phonePopup.addEventListener("mouseleave", e => {
    phonePopup.style.display = "none";
  });
}
