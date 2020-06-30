/* ######################## JavaScript for index.html ####################### */
window.onscroll = function() {
  maximumTransparency = 0.7;
  heightMaxPercentage = 0.3527;
  startingMarginTop = 20;
  var nav = document.getElementById('navbar');

  ratio = (window.pageYOffset/document.documentElement.clientHeight) / heightMaxPercentage;
  nav.style.backgroundColor = "rgba(35,31,32," + ((ratio < 1 ? ratio : 1) * maximumTransparency).toString() + ")";
  nav.style.marginTop = (startingMarginTop > window.pageYOffset ? (startingMarginTop - window.pageYOffset).toString() : '0') + 'px';
}
function goDownToContent() {
    $('html, body').animate({
        scrollTop: $("#downArrow").offset().top + $("#downArrow").height()
    }, 800 ); //in ms
}
