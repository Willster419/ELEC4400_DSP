%Willard Wider
%6/6/18
%lab5
%ELEC4400 DSP
%forward and backward difference stuff
%NOTE: steps 1-5 and 8 are written on paper
clear();
interval = 10^-3;
t = 0:interval:11;
k=1;
T=0;%just to declare it
y = exp(-k.*t);%can be done here, does not change
figure();

%forwared
T=2.1;
fd = (1-(k*T)).^t;
subplot(3,2,1);
plot(t,y);
hold on;
plot(t,fd);
hold off;
title(sprintf("FD T=%.1f, pole=-1.1",T));

T=1.5;
fd = (1-(k*T)).^t;
subplot(3,2,3);
plot(t,y);
hold on;
plot(t,fd);
title(sprintf("FD T=%.1f, pole=-1.1",T));
hold off;

T=0.8;
fd = (1-(k*T)).^t;
subplot(3,2,5);
plot(t,y);
hold on;
plot(t,fd);
title(sprintf("FD T=%.1f, pole=-1.1",T));
hold off;

%backward
T=2.1;
bd = (1+(k*T)).^-t;
subplot(3,2,2);
plot(t,y);
hold on;
plot(t,bd);
title(sprintf("BD T=%.1f, pole=-1.1",T));
hold off;

T=1.5;
bd = (1+(k*T)).^-t;
subplot(3,2,4);
plot(t,y);
hold on;
plot(t,bd);
title(sprintf("BD T=%.1f, pole=-1.1",T));
hold off;

T=0.8;
bd = (1+(k*T)).^-t;
subplot(3,2,6);
plot(t,y);
hold on;
plot(t,bd);
title(sprintf("BD T=%.1f, pole=-1.1",T));
hold off;