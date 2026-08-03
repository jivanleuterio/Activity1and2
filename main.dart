import 'dart:io';
void main() {
  //this is where student can enter their name
  stdout.write('Enter student name: ');
  String? name = stdin.readLineSync();

  quiz_compute();
  
}

void quiz_compute() {
  // this are the inputs, age, q1 to q3
  stdout.write('\nEnter age: ');
  int? age = int.tryParse(stdin.readLineSync() ?? '');
  
  stdout.write('Enter quiz 1: ');
  int? q1 = int.tryParse(stdin.readLineSync() ?? '');

  stdout.write('Enter quiz 2: ');
  int? q2 = int.tryParse(stdin.readLineSync() ?? '');

  stdout.write('Enter quiz 3: ');
  int? q3 = int.tryParse(stdin.readLineSync() ?? '');

  if (age == null || q1 == null || q2 == null || q3 == null) {
    print("Invalid Numbers!!!");
    return;
  }

  double average = (q1 + q2 + q3)/3;

  stdout.write('\nAverage: ${average.toInt()}\n\nStatus: ');

  // this will will identify the average if the student is pass or not
  if(average >= 75) {
    print('Passed');
    print('\nRemark: Good job, keep it up!');
  } else if (average < 75) {
    print('Failed');
    print('\nRemark: Your Failed!');
  } else {
    print('Error');
  }
}