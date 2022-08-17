function preload() {
  img = loadImage("https://raw.githubusercontent.com/scikit-image/scikit-image/master/skimage/data/astronaut.png");
}
const SIZE = 256;
function setup() {
  createCanvas(SIZE,SIZE);
  img.resize(SIZE, SIZE);
  img.filter('gray');
  var arr = new Array(256);
  arr.fill(0);
  img.loadPixels();
  for (let i = 0; i < img.width; i++) {
    for (let j = 0; j < img.height; j++) {
      pos = 4*(j*img.width+i);
      val = img.pixels[pos];
      ++arr[val];
    }
  }
  max_val = Math.max(...arr)
  console.log(arr)
  arr = arr.map(x => Math.trunc(x / max_val * 256))
  for ([i, x] of arr.entries()) {
    line(i, 256, i, 256 - x)
  }
  
   //image(img, 0, 0);
}
