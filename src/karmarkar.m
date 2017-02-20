function [x_opt, f_opt] = karmarkar()
    c = [1; -3; 3];
    A = [1, -3, 2];
    p = struct('a', 0.25, 'q', 100, 'n', size(A, 2),...
	'x_0', [1/size(A, 2); 1/size(A, 2); 1/size(A, 2)]);
    [x_opt, f_opt] = algorithm(A, c, p);
end

function [x_knew, f_opt] = algorithm(A, c, p)
    x_knew = p.x_0;
    while c'*x_knew/(c'*p.x_0) > 2^(-p.q)
	x_k = x_knew;
	x_knew = psi_map(A, c, x_k, p);
	iter = iter + 1;
    end
    f_opt = c'*x_knew;
end

function x_knew = psi_map(A, c, x_k, p)
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
