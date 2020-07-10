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
onErrorPage = window.location.pathname === '/error';

if (isMobile && !onErrorPage) {
  redirectTo = '/error'
}
if (onErrorPage && !isMobile) {
  redirectTo = '/'
}

window.open(redirectTo, '_self');
