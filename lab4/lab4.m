%Willard Wider
%5/30/18
%ELEC4400 DSP
%Lab 4
%Problem 1 - Arethmetic Greyscale
%https://www.mathworks.com/help/matlab/import_export/importing-images.html
warning('off','all');
clear;
img = imread('man.jpg');
disp("original image");
imshow(img);
disp("press any key to continue...");
pause;
disp("applying Aithmetic greyscale...");
%https://www.mathworks.com/help/matlab/matlab_prog/loop-control-statements.html
%https://www.mathworks.com/help/matlab/learn_matlab/array-indexing.html
%https://www.mathworks.com/help/matlab/math/multidimensional-arrays.html
%create the new matmrix for this
%https://www.mathworks.com/help/matlab/ref/zeros.html
img1 = zeros(800,1200);
%img1(1,1) = 9;
for x = 1:1200
    for y = 1:800
        %img1(y,x) = 9;
        img1(y,x) = (img(y,x,1)+img(y,x,2)+img(y,x,3))/3;
    end
end
img1 = uint8(img1);
imshow(img1);
disp("press any key to continue...");
pause;
%Problem 2 - geometric greyscale
disp("applying geometric greyscale...");
divideValue = 255^2;
divideValue = divideValue*3;
divideValue = sqrt(divideValue);
img2 = zeros(800,1200);
for x = 1:1200
    for y = 1:800
        %img2(y,x) = sqrt((img(y,x,1)^2)+(img(y,x,2)^2)+(img(y,x,3))^2)/divideValue;
        value1 = double(img(y,x,1));
        value2 = double(img(y,x,2));
        value3 = double(img(y,x,3));
        topPart = (value1^2)+(value2^2)+(value3^2);
        topPartSqrt = sqrt(topPart);
        completePixel = topPartSqrt / divideValue;
        completePixel = completePixel*255;
        img2(y,x)= uint8(completePixel);
        %https://www.mathworks.com/help/matlab/matlab_prog/formatting-strings.html
        %txt = sprintf('value1=%f,value2=%f,value3=%f,topPart=%f,topPartSqrt=%f,completePixel=%f',value1,value2,value3,topPart,topPartSqrt,completePixel);
        %disp(txt);
        %pause;
    end
end
img2 = uint8(img2);
imshow(img2);
disp("press any key to continue...");
pause;
%Problem(s) 3
disp("3.1:");
disp("the arithmetic mean is just adding the 3 value and scaling dividing to get a direct average number");
disp("the geometricmean is also an average but because of the squared property, puts more emphasis on higher values");
disp("thus the pixels are shown with a higher value for when they are originally higher");
disp("this it does a better job of displaying the white (answer for 3.3 as well)");
disp("3.2:");
disp("we scale by the normalization number because it representes the maximum possible number for if all 3 rgb values were at maximum value 255");
disp("3.4: i don't follow baseball but my guess is that he hit a homerun or something to let them win the world series against the yankees");
disp("press any key to continue...");
pause;
%Problem 4 - color effects
disp("original image");
colorImg=imread('WIT2.jpg');
imshow(colorImg);
disp("press any key to continue...");
pause;
disp("displaying cool color effect...");
%hex color code for yello that we want is #F5DA93
%first layer is red, second green, third is blue
red = 245;
green = 218;
blue = 147;
colorImg1 = zeros(1333,2000,3);
for x = 1:2000
    for y = 1:1333
        newR = double((colorImg(y,x,1)));
        newG = double((colorImg(y,x,2)));
        newB = double((colorImg(y,x,3)));
        newR = newR - red;
        newG = newG - green;
        newB = newB - blue;
        newR = newR^2;
        newG = newG^2;
        newB = newB^2;
        distance = sqrt((newR+newG+newB));
        %fprintf('newR=%f,newG=%f,newB=%f,distance=%f\n',newR,newG,newB,distance);
        %pause;
        if(distance > 50)
            %apply geometric greyscaling
            colorValue1 = double(colorImg(y,x,1));
            colorValue2 = double(colorImg(y,x,2));
            colorValue3 = double(colorImg(y,x,3));
            topPart = (colorValue1^2)+(colorValue2^2)+(colorValue3^2);
            topPartSqrt = sqrt(topPart);
            completePixel = topPartSqrt / divideValue;
            completePixel = completePixel*255;
            colorImg1(y,x,1)= uint8(completePixel);
            colorImg1(y,x,2)= uint8(completePixel);
            colorImg1(y,x,3)= uint8(completePixel);
        else
            colorImg1(y,x,1)= colorImg(y,x,1);
            colorImg1(y,x,2)= colorImg(y,x,2);
            colorImg1(y,x,3)= colorImg(y,x,3);
        end
    end
end
colorImg1 = uint8(colorImg1);
imshow(colorImg1);
disp("4.4");
disp("Yes, the yellow color stayed, while all other colors became black and white.");
disp("however, it also kept the yellow that is in the grass and the tree a little");
disp("an improvment could be to define a square boundry to actually perform the operation");