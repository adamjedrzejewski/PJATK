// https://editor.p5js.org/
function setup() {
    createCanvas(512,512);
    background(255);
  }
  
  var x0=-1;
  var y0=-1;
  var x1=-1;
  var y1=-1;
  
  function draw() {
    //background(220);
  }
  
  function mousePressed() {
      x0=mouseX;
      y0=mouseY;
  }
  
  function mouseDragged() {  
      x1=mouseX;
      y1=mouseY;  
      background(255);
      noStroke();
      fill('red');
      ellipse(x0-3,y0-3,6);
      fill('green');  
      ellipse(x1-3,y1-3,6);
  }
  
  function mouseReleased() {
    background(255);
    loadPixels();
    draw_line();
    updatePixels();
  }
  
  function set_pixel(x,y,c) {
      idx=(y*512+x)*4;
      pixels[idx]=c;
      pixels[idx+1]=c;
      pixels[idx+2]=c;
      pixels[idx+3]=255;
  }
  
  function draw_line() {
    const a = (y1 - y0) / (x1 - x0);
    const b = y0 - a * x0;
    const direct = (x) => Math.round(a * x + b)
    
    const [start, end] = x0 < x1 ? [x0, x1] : [x1, x0];
    for (i = start; i <= end; i += 0.01) {
      j = direct(i)
      set_pixel(Math.trunc(i), Math.trunc(j), 0)
    }
    updatePixels();
  }