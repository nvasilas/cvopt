function X = lmi2()
    A = [-1,-2,1; 3,2,1; 1,-2,-1];
    B = [1;0;1];
    Q = [1,-1,0; -1,-3,-12; 0,-12,-36];

    setlmis([]); %create a blank LMI framework
    X = lmivar(1,[3 1]); %declare X as a 3x3 symmetrical matrix
    lmiterm([1 1 1 X],A',1,'s'); %(1,1) block, 's' means A^TX + XA
    lmiterm([1 1 1 0],Q); %(1,1) block, plus the constant matrix Q
    lmiterm([1 2 2 0],-1); %(2,2) block, meaning -I
    lmiterm([1 2 1 X],B',1); %(2,1) block, meaning B^TX
    lmis = getlmis; %complete the LMI framework setting
    c = mat2dec(lmis,eye(3));
    options = [1e-5,0,0,0,0]; %set relative accuracy 1e-5
    [copt xopt] = mincx(lmis,c,options); %solve min problem
    X = dec2mat(lmis,xopt,X); %extract the solution matrix X
    Xst = care(A,B,Q,-1); %Riccati solution
    norm(X - Xst) %LMI - Riccati solution
end
