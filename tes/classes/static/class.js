
let iframe = document.querySelector('#lecture');
console.log(iframe)
let player = new Vimeo.Player(iframe);
player.on('play', function() {
        console.log('played the player 2.0 video!');
    });