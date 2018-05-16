%problem 1
disp("problem 1");
disp("x=s^2 + 4s +3");
disp("h=s+5");
disp("s^3 + 4s^2 + 3s + 5s^2 + 20s + 15");
disp("s^3 + 9s^2 + 23s + 15");
disp('Press any key to continue...');
pause;

%problem 2
disp("problem 2");
q = [2 4];
v = [5 3];
w = conv(q,v);
disp('Press any key to continue...');
pause;

%problem 3
disp("problem 3");
x = [1 4 3];
h = [1 5];
i = conv(x,h);
disp('Press any key to continue...');
pause;

%problem 4
disp("problem 4");
%setup the time scale step
T = 10^-8;
t2 = 0:T:10^-5;
%building the function
%NOTE: exp(x) = e^x
u = (10^6)*exp((-10^6)*t2);
%heavyside input
y = heaviside(t2)*T;
%convolude
convol = conv(u,y);
%and plot it
plot(t2,convol(1:1001));
title("Problem 4");
xlabel("time (microseconds)");
ylabel("voltage");
disp('Press any key to continue...');
pause;

%problem 5
disp("problem 5");
%time scale
n = 0:0.01:10;
%function
u2 = (exp(-n)).*sin(n).*cos(n);
%input
y = heaviside(n);
%convolude
convol2 = conv(u2,y);
%and plot
plot(n,convol2(1:1001));
title("Problem 5");
xlabel("time (seconds)");
ylabel("voltage");
disp('Press any key to continue...');
pause;
disp("done");