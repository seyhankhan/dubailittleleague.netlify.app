const toMatch = [
    /Android/i,
    /webOS/i,
    /iPhone/i,
    /iPad/i,
    /iPod/i,
    /BlackBerry/i,
    /Windows Phone/i
];

isMobile = toMatch.some((toMatchItem) => {navigator.userAgent.match(toMatchItem)});
onErrorPage = window.location.pathname == '/error';

if (onErrorPage && !isMobile) {
  window.open('/','_self');
}
if (isMobile && !onErrorPage) {
  window.open('/error','_self');
}
