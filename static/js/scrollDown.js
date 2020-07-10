/* ###################### JavaScript for scrolling down ##################### */
function goDownToContent() {

  // time to scroll down in milliseconds
  scrollDownTime = 800;

  if (window.location.pathname === "/") {
    $('html, body').animate({
      scrollTop: $("iframe").offset().top
    }, scrollDownTime);
  } else {
    $('html, body').animate({
      scrollTop: $("#bigTextOverlay").offset().top + $("#bigTextOverlay").height()
    }, scrollDownTime);
  }
}



const emailSVG = document.getElementById('email-svg');
const emailPopup = document.getElementById('email-popup');

emailSVG.addEventListener('mouseenter', e => {
  emailPopup.style.display = '';
});
emailPopup.addEventListener('mouseleave', e => {
  emailPopup.style.display = 'none';
});

const phoneSVG = document.getElementById('phone-svg');
const phonePopup = document.getElementById('phone-popup');

phoneSVG.addEventListener('mouseenter', e => {
  phonePopup.style.display = '';
});
phonePopup.addEventListener('mouseleave', e => {
  phonePopup.style.display = 'none';
});








// window.onscroll = function() {
//   maximumTransparency = 0.7;
//   heightMaxPercentage = 0.3527;
//   startingMarginTop = 20;
//   var nav = document.getElementById('navbar');
//
//   ratio = (window.pageYOffset/document.documentElement.clientHeight) / heightMaxPercentage;
//   nav.style.backgroundColor = "rgba(35,31,32," + ((ratio < 1 ? ratio : 1) * maximumTransparency).toString() + ")";
//   nav.style.marginTop = (startingMarginTop > window.pageYOffset ? (startingMarginTop - window.pageYOffset).toString() : '0') + 'px';
// }
