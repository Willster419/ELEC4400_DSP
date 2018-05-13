%quesiton 1
disp('question 1');
d = 5;
t = 0:1:10;
f = heaviside(t-d);
plot(t,f);
xlabel("time");
ylabel("heavyside (t)");
axis([0 10 -.2 1.2]);
title("heavyside function - problem 1");
disp('Press any key to continue...');
pause;

%questino 2
disp('question 2');
t2=0:0.01:10;
f2 = heaviside(t2-d);
plot(t2,f2);
xlabel("time");
ylabel("heavyside (t2)");
axis([0 10 -.2 1.2]);
title("heavyside function - problem 2");
disp('Press any key to continue...');
pause;

%question 3
disp('question 3');
A = 1;
alpha = 0.8;
k = 0:1:100;
T = 0.1;
n = k*T;
stem(n,A*power(alpha,n));
title("exponential sequence - problem 3");
disp('Press any key to continue...');
pause;

%question 4
disp('question 4');
alpha = 1.6;
stem(n,A*power(alpha,n));
title("exponential sequence - problem 4");
disp('Press any key to continue...');
pause;

%question 5
disp('question 5');
A = 1;
alpha = 1.0;
k = 0:1:50;
T = 0.1;
n = k*T;
stem(n,A*power(alpha,n));
title("exponential sequence - problem 5");
disp('Press any key to continue...');
pause;

%question 6
disp('question 6');
T=1;
k=0:1:25;
n=k*T;
n2=cos((pi*n)/4);
plot(n,n2);
title("sinusoid function - problem 6");
disp('Press any key to continue...');
pause;

%question 7
disp('question 7');
T=1;
k=0:1:25;
n=k*T;
n3=cos((pi*(n+8))/4);
plot(n,n3);
title("sinusoid function - problem 7");
disp('Press any key to continue...');
pause;

%question 8
disp('question 8');
%part 1
n4 = cos((3*pi*n)/8);
plot(n,n4);
%part 2
n5 = cos((3*pi*(n+16))/8);
plot(n,n5);
title("sinusoid function - problem 8");
disp('Press any key to continue...');
pause;

%question 9
disp('question 9');
disp('number 8 has a higher frequence shown by the graphs');
disp('due to the 3pi vs pi');
disp('Press any key to continue...');
pause;

%question 10
disp('question 10');
disp('porblem 7 sinusoid = n2/n3');
disp('problem 8 sinusoid = n4/n5');
disp('problem 8 takes more samples within a specified time');
disp('to appear periodic due to the higher frequency of the function');
disp('Press any key to continue...');
pause;
disp('done');