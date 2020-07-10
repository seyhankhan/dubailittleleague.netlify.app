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
const copySVG = document.getElementById('copy-svg');
const emailAddressText = document.getElementById('email-address');

emailSVG.addEventListener('mouseenter', e => {
  emailPopup.style.display = 'flex';
  copySVG.style.cursor = 'pointer';
});
emailPopup.addEventListener('mouseleave', e => {
  emailPopup.style.display = 'none';
  copySVG.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-copy"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>';
  window.getSelection().removeAllRanges();
});
copySVG.addEventListener('click', e => {
  //highlight the text
  var range = document.createRange();
  range.selectNode(emailAddressText);
  window.getSelection().removeAllRanges();
  window.getSelection().addRange(range);
  // copy the text
  document.execCommand('copy');
  // turn it into a checkmark
  copySVG.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-check"><polyline points="20 6 9 17 4 12"></polyline></svg>';

  copySVG.style.cursor = 'auto';
  console.log('Email is copied!');
});


const phoneSVG = document.getElementById('phone-svg');
const phonePopup = document.getElementById('phone-popup');

phoneSVG.addEventListener('mouseenter', e => {
  phonePopup.style.display = 'flex';
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
