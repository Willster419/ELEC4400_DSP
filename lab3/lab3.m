%lab3
%question 5
clear
load("lab3_complete.mat");
imshow(imageOfInterest);%nice meme, it's you
disp("press any key to continue...");
pause();
%question 6
q6Ans = conv2(imageOfInterest,kernalFrom1,'valid');
q6Ans2 = uint8(q6Ans);
imshow(q6Ans2);%blurs the image
disp("press any key to continue...");
pause();
%question 7
q7Ans = conv2(imageOfInterest,kernalFrom2,'valid');
q7Ans2 = uint8(q7Ans);
imshow(q7Ans2);%edge detection
disp("press any key to continue...");
pause();
%question 8
q8Ans = conv2(imageOfInterest,kernalq8,'valid');
q8Ans2 = uint8(q8Ans);
imshow(q8Ans2);%more blur
disp("press any key to continue...");
pause();
%question 9
q9Ans = conv2(imageOfInterest,kernalq9,'valid');
q9Ans2 = uint8(q9Ans);
imshow(q9Ans2);%sharpen
disp("done");