var imgA;
var imgB; 



function setup() {
    createCanvas(512,512);
    background(255);  
    imgA = createImage(512,512);
    imgB = createImage(512,512);
    imgA.loadPixels();
    imgB.loadPixels();
    var d = pixelDensity();
    for(var i=0; i<512*512*4*d; i+=4) {
      imgA.pixels[i]=240;
      imgA.pixels[i+1]=250;
      imgA.pixels[i+2]=240;
      imgA.pixels[i+3]=255;
      imgB.pixels[i]=240;
      imgB.pixels[i+1]=240;
      imgB.pixels[i+2]=250;
      imgB.pixels[i+3]=255;
    }
    imgA.updatePixels();
    imgB.updatePixels();
}

function draw() {
    if (!keyIsDown(32)) {
      image(imgA,0,0);
      text('Image A',10,20);
    } else {
      image(imgB,0,0);
      text('Image B',10,20);
  }
}

function makeVector(x, y) {
    return [x, y, 1]
}

function drawVector(img, vec) {
    var [x, y, _] = vec;
    img.set(x, y, 0);
    img.updatePixels();
}

function mouseDragged() {
    var vec = makeVector(mouseX, mouseY);
    drawVector(imgA, vec);
}

function makeIdentityMatrix() {
    return [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
}

function makeTranslationMatrix(tx, ty) {
    return [
        [1, 0, tx],
        [0, 1, ty],
        [0, 0,  1]
    ]
}

function makeScalingMatrix(sx, sy) {
    return [
        [sx, 0, 0],
        [0, sy, 0],
        [0,  0, 1]
    ]
}

function makeRotationMatrix(angle_deg) {
    var angle_rad = angle_deg / 180 * Math.PI;
    return [
        [Math.cos(angle_rad), -Math.sin(angle_rad), 0],
        [Math.sin(angle_rad), Math.cos(angle_rad),  0],
        [0,                   0,                    1]
    ]
}

function makeSheerMatrix(shx, shy) {
    return [
        [1,   shx, 0],
        [shy, 1,   0],
        [0,   0,   1]
    ]
}

console.log("identity", makeIdentityMatrix());
console.log("translation (50, 50)", makeTranslationMatrix(50, 50));
console.log("scale (2, 2)", makeScalingMatrix(2, 2));
console.log("rotate 90", makeRotationMatrix(90));
console.log("sheer (5, 5)", makeSheerMatrix(5, 5));