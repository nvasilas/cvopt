function [x, fval] = qp()
    H = [1 -1; -1 2]; 
    f = [-2; -6];
    A = [1 1; -1 2; 2 1];
    b = [2; 2; 3];
    lb = zeros(2,1);
    options = optimoptions('quadprog',...
	'Algorithm','interior-point-convex','Display','off');
    [x,fval,exitflag,output,lambda] = ...
	quadprog(H,f,A,b,[],[],lb,[],[],options);
    x1 = [-10:0.1:10];
    x2 = [-10:0.1:10];
    [X, Y] = meshgrid(x1, x2);
    Z = 0.5*X.^2 + Y.^2 - X.*Y -2*X -6*Y;
    hold on;
    meshc(X, Y, Z);
    scatter3(x(1),x(2),fval,'*', 'm');
end
