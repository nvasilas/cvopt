function X = lmi1()
    A = [-2,-2,-1; -3,-1,-1; 1,0,-4];
    B = [-1,0; 0,-1; -1,-1];
    Q = [-2,1,-2; 1,-2,-4; -2,-4,-2];
    R = eye(2);

    setlmis([]); %create an LMI framework
    X = lmivar(1,[3 1]); %declare X as a 3x3 symmetrical matrix
    lmiterm([1 1 1 X],A',1,'s'); %(1,1) block, 's' means A^TX + XA
    lmiterm([1 1 1 0],Q); %(1,1) block, plus the constant matrix Q
    lmiterm([1 1 2 X],1,B); %(1,2) block, meaning XB
    lmiterm([1 2 2 0],-1); %(2,2) block, meaning -R
    lmiterm([-2,1,1,X],1,1); %the second inequality meaning X > 0
    lmis = getlmis; %complete the LMI framework setting
    [tmin xfeas] = feasp(lmis); %solve the feasible problem
    X = dec2mat(lmis,xfeas,X); %extract the solution matrix X
end
