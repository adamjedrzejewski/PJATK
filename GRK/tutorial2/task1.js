function preload() {
  img = loadImage("https://raw.githubusercontent.com/scikit-image/scikit-image/master/skimage/data/astronaut.png");
  img_r=createImage(256,256);
  img_g=createImage(256,256);
  img_b=createImage(256,256);
}
function setup() {
  createCanvas(512,512);
  img.resize(256, 256);
  img.loadPixels();
  img_r.loadPixels();
  img_g.loadPixels();
  img_b.loadPixels();
  for (let i = 0; i < img.width; i++) {
    for (let j = 0; j < img.height; j++) {
      pos=4*(j*img.width+i);
      r=img.pixels[pos];
      g=img.pixels[pos+1];
      b=img.pixels[pos+2];
      
      img_r.pixels[pos] = r;
      img_g.pixels[pos + 1] = g;
      img_b.pixels[pos + 2] = g;
      img_r.pixels[pos + 3] = img_g.pixels[pos + 3] 
        = img_b.pixels[pos + 3] = 255;
    }
  }
  img.updatePixels();
  img_r.updatePixels();
  img_g.updatePixels();
  img_b.updatePixels();
  image(img_r, 0, 0);
  image(img_g, 256, 0);
  image(img_b, 0, 256);
  image(img, 256, 256);
}
