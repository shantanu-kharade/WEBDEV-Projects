let boxes = document.querySelectorAll(".box");
let resetBtn = document.querySelector("#reset-btn");
let newBtn = document.querySelector("#new-btn");
let msgContainer = document.querySelector(".msg-container");
let msg = document.querySelector("#msg");

let turnO = true; //playerX, playerO
let moves = 0; // Track the number of moves

const winPatterns = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [3, 4, 5],
    [6, 7, 8],
];

const resetGame = () => {
    turnO = true;
    moves = 0; // Reset moves counter
    enableBoxes();
    msgContainer.classList.add("hide");
    stopAudio();
};

boxes.forEach((box) => {
    box.addEventListener("click", () => {
        if (box.innerText === "") { // Check if box is empty
            if (turnO) {
                //playerO
                box.innerText = "⭕";
                turnO = false;
            } else {
                //playerX
                box.innerText = "❌";
                turnO = true;
            }
            box.disabled = true;
            moves++; // Increment moves counter
            checkWinner();
            checkDraw(); // Check for draw after each move
        }
    });
});

const disabledBoxes = () => {
    for (let box of boxes) {
        box.disabled = true;
    }
};

const enableBoxes = () => {
    for (let box of boxes) {
        box.disabled = false;
        box.innerText = "";
    }
};

const showWinner = (winner) => {
    msg.innerText = `Congratulations, Winner is ${winner}`;
    msgContainer.classList.remove("hide");
    playWinSound();
    disabledBoxes();
};

const checkWinner = () => {
    for (let pattern of winPatterns) {
        let pos1val = boxes[pattern[0]].innerText;
        let pos2val = boxes[pattern[1]].innerText;
        let pos3val = boxes[pattern[2]].innerText;

        if (pos1val != "" && pos2val != "" && pos3val != "") {
            if (pos1val === pos2val && pos2val === pos3val) {
                showWinner(pos1val);
            }
        }

    }
};

const checkDraw = () => {
    // Check if all boxes are filled and there's no winner
        if (moves === 9 && !checkWinner()) {
        msg.innerText = "It's a draw!";
        msgContainer.classList.remove("hide");
        playDrawSound();
        disabledBoxes();
    }
};

function playWinSound() {
    var winSound = document.getElementById('win-sound');
    winSound.play();
}

function playDrawSound() {
    var drawSound = document.getElementById('draw-sound');
    drawSound.play();
}

function stopAudio() {
    var winSound = document.getElementById('win-sound');
    var drawSound = document.getElementById('draw-sound');
    winSound.pause();
    winSound.currentTime = 0;
    drawSound.pause();
    drawSound.currentTime = 0;
}

newBtn.addEventListener("click", resetGame);
resetBtn.addEventListener("click", resetGame);
