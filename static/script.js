/**
 * Setup
 */

const icon_width = 150,
      icon_height = 150,
      num_icons = 60,
      time_per_icon = 50,
      indexes = [0,0,0,0,0];


console.log(symbols_positions)
const roll = (reel, offset = 0) => {
    const delta = (offset + 2) * num_icons + Math.round(Math.random() * num_icons);
    const style = getComputedStyle(reel),
        backgroundPositionY = parseFloat(style.backgroundPositionY);

    return new Promise((resolve, reject) => {
        reel.style.transition = `background-position-y ${8 + delta * time_per_icon}ms`;
        reel.style.backgroundPositionY = `${backgroundPositionY + delta * icon_height}px`;

        setTimeout(() => {
            resolve(delta%num_icons);
        }, 8 + delta * time_per_icon);
    }); // Added closing parenthesis here
};

function rollAll() {
    const reelsList = document.querySelectorAll('.slots > .reels');
    Promise
        .all( [... reelsList].map((reel, i) => roll(reel, i)) )
        .then((deltas) => {
            deltas.forEach((delta, i) => indexes[i] = (indexes[i] += delta)%num_icons);
            console.log(deltas)
        })
//    [...reelsList].forEach((reel, i) => {
//        console.log(reel,1);
//        roll(reel, i).then((delta) => { console.log(delta) })
//    });
}

document.getElementById("startButton").addEventListener("click", rollAll);

// Old scripting below for SlotMachine.html works no repeat image
function startSlotMachine() {
    console.log("Start button clicked");
    // Start sliding animation for each reel
    //for (let i = 1; i <= 5; i++) {
    //    slideReel('reel' + i);
    //}
}

function startSlotMachine() {
    // Start sliding animation for each reel
    for (let i = 1; i <= 5; i++) {
        slideReel('reel' + i);
    }
}

function slideReel(reelId) {
    const reel = document.getElementById(reelId);
    const symbolHeight = reel.children[0].offsetHeight; // Height of one symbol
    const totalSymbols = reel.children.length;
    const totalHeight = symbolHeight * totalSymbols; // Total height of all symbols
    const animationDuration = Math.random() * (totalHeight * 0.1) + totalHeight * 0.1; // Random duration based on total height

    reel.style.transition = 'transform ' + animationDuration + 'ms cubic-bezier(0.1, 0.65, 0.1, 1)';
    reel.style.transform = 'translateY(-' + totalHeight + 'px)';
}