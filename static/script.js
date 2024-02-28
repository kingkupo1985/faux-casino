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
