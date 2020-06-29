/* ######################## JavaScript for index.html ####################### */
window.onscroll = function() {
  console.log(window.pageYOffset);

  var nav = document.getElementById('navbar');
  if (window.pageYOffset/document.documentElement.clientHeight > 0.30) {
    nav.style.backgroundColor = rgba(35, 31, 32, 0.5);
  } else {
    nav.style.backgroundColor = "";
  }
}
