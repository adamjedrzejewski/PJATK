function preload() {
  img = loadImage("https://raw.githubusercontent.com/scikit-image/scikit-image/master/skimage/data/astronaut.png");
  img_h=createImage(256,256);
  img_s=createImage(256,256);
  img_v=createImage(256,256);
}
function setup() {
  createCanvas(512,512);
  img.resize(256, 256);
  img.loadPixels();
  img_h.loadPixels();
  img_s.loadPixels();
  img_v.loadPixels();
  for (let i = 0; i < img.width; i++) {
    for (let j = 0; j < img.height; j++) {
      pos=4*(j*img.width+i);
      r=img.pixels[pos]/255;
      g=img.pixels[pos+1]/255;
      b=img.pixels[pos+2]/255;
      
      cmax = Math.max(r,g,b);
      cmin = Math.min(r,g,b);
      l=(cmax+cmin)/2;
      img_v.set(i, j,255*l);
    }
  }
  img.updatePixels();
  img_h.updatePixels();
  img_s.updatePixels();
  img_v.updatePixels();
  image(img_h, 0, 0);
  image(img_s, 256, 0);
  image(img_v, 0, 256);
  image(img, 256, 256);
}
