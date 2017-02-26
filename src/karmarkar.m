function [x_opt, f_opt, iter] = karmarkar(c, A, q, a)
    % Karmarkar's algorith
    % x = karmarkar(___) attempts to solve Karmarkar's restricted problem, that is,
    % a linear programming problem in Karmarkar's canonical form which satisfies
    % the four assumptions, as stated by Karmarkar in his original paper. The
    % form of the problem is as follows:
    % min c'*x subject to: A*x = 0, sum_{i=1}^n x_i = 1, x >=0
    % The inputs of this function is
    % the vector c, the coefficient of the objective function,
    % the matrix A, the matrix coefficient of the constraints,
    % the scalar q > 0, the termination parameter (optional),
    % the scalar 0 < a < 1, the step size (optional).
    % The output of x_opt = karmarkar(___) is the optimal value x^*.
    % The outputs of [x_opt, f_opt] = karmarkar(___) are as above plus
    % the optimal value of the objective f^* (expected to be zero).
    % The outputs of [x_opt, f_opt, iter] = karmarkar(___) are as above plus
    % the number of iterations required to converge to optimal solution.
    % Usage example. Define the problem
    % c = [1;-3; 3];
    % A = [1, -3, 2];
    % and then call from MATLAB command line the function x = karmarkar(c, A).

    if ~exist('q','var')
	% third parameter does not exist, using default value
	q = 100;
    end
    if ~exist('a','var')
	% fourth parameter does not exist, using default value
	a = 0.25;
    end
    p = struct('a', a, 'q', q, 'n', size(A, 2),...
	'x_0', [1/size(A, 2); 1/size(A, 2); 1/size(A, 2)]);
    [x_opt, f_opt, iter] = algorithm(A, c, p);
end

function [x_knew, f_opt, iter] = algorithm(A, c, p)
    % This function implements Karmarkar's algorithm
    iter = 0;
    x_knew = p.x_0;
    while c'*x_knew/(c'*p.x_0) > 2^(-p.q)
	x_k = x_knew;
	x_knew = psi_map(A, c, x_k, p);
	iter = iter + 1;
    end
    f_opt = c'*x_knew;
end

function x_knew = psi_map(A, c, x_k, p)
    % This function finds the next point
    e = ones(p.n, 1);
    D_k = diag(x_k);
    B_k = [A*D_k; e'];

    P_k = eye(p.n) - B_k'*((B_k*B_k')\B_k);
    c_hatk = P_k*D_k*c/norm(P_k*D_k*c);

    r = 1/sqrt(p.n*(p.n - 1));
    d_k = -r*c_hatk;

    xbar = p.x_0 + p.a*d_k;

    x_knew = D_k*xbar/(e'*D_k*xbar);
end
