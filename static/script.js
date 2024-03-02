/**
 * Setup
 */

const icon_width = 150,
      icon_height = 150,
      num_icons = 60,
      time_per_icon = 50,
      indexes = [0,0,0,0,0];

const roll = (reel, offset = 0, finalPosition, duration, startTime) => {
    // Calculate total distance to move
    const totalDistance = finalPosition * icon_height;

    // Set initial position
    const style = getComputedStyle(reel),
        initialPosition = parseFloat(style.backgroundPositionY);

    // Set transition
    reel.style.transition = 'none';

    // Start spinning
    requestAnimationFrame(function spin(timestamp) {
        const elapsedTime = timestamp - startTime;
        const progress = Math.min(1, elapsedTime / duration);
        reel.style.backgroundPositionY = initialPosition + totalDistance * progress + 'px';

        if (progress < 1) {
            requestAnimationFrame(spin);
        } else {
            // Spin completed
            reel.style.transition = 'none'; // Remove transition
            reel.style.backgroundPositionY = `${finalPosition * icon_height}px`; // Set final position
        }
    });
};

function rollAll(startTime) {
    const duration = 4000; // Total duration of the spin (ms)

    const reelsList = document.querySelectorAll('.slots > .reels');
    [...reelsList].forEach((reel, i) => {
        // Calculate random final position for each reel
        const finalPosition = (i + 2) * num_icons + Math.round(Math.random() * num_icons);
        roll(reel, i, finalPosition, duration, startTime);
    });
}

document.getElementById("startButton").addEventListener("click", function() {
    const startTime = performance.now(); // Define startTime here
    rollAll(startTime);
});

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