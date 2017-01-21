function [x, fval] = lp2()
    A = [1, 2; 2, -4; -2, 1; -1, 0; 0, -1];
    b = [25; 8; -5; 0; -2];
    f = [-4; -3];
    [x,fval,exitflag,output] = linprog(f,A,b);
    fval = -fval;
end
