void main(){
  calculatePerimeter (10, 5);
  calculatePerimeterS (7);
}

void calculatePerimeter(double width, double height){
  double perimeter = (2 * (width + height));
  print("The perimeter of Rectangle: $perimeter");
}

void calculatePerimeterS(double width){
  double perimeter = (4 * width);
  print("The perimeter of Square: $perimeter");
}