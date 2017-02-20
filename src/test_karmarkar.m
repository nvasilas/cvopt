function [x, fval] = test_karmarkar()
    Aeq = [1, -3, 2;1, 1, 1];
    beq = [0; 1];
    f = [1, -3, 3];
    lb = [0, 0, 0];
    [x, fval] = linprog(f,[],[],Aeq,beq, lb);
end
