/* ######################## JavaScript for index.html ####################### */
window.onscroll = function() {
  var nav = document.getElementById('navbar');

  ratio = (window.pageYOffset/document.documentElement.clientHeight) / 0.3527;
  nav.style.backgroundColor = "rgba(35,31,32," + ((ratio < 1 ? ratio : 1) * 0.7).toString() + ")";
  nav.style.marginTop = (20 > window.pageYOffset ? (20 - window.pageYOffset).toString() : '0') + 'px';
}
